import json
import os
import sys
from pathlib import Path

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QDial,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtCore import Qt

import audio
from audio import play_kick, play_snare, play_hihat

STEP_COUNT = 16
DEFAULT_BPM = 120
SAV_DIR = Path(__file__).resolve().parent.parent / "SAV"

LABEL_STYLE = "color: #aaaaaa; font-size: 10px;"
PANEL_STYLE = "background-color: #3a3a3a; border-radius: 4px;"


def _make_slider(min_val, max_val, value, on_change):
    s = QSlider(Qt.Orientation.Horizontal)
    s.setRange(min_val, max_val)
    s.setValue(value)
    s.setFixedHeight(18)
    s.valueChanged.connect(on_change)
    return s


def _param_row(label_text, slider):
    row = QHBoxLayout()
    row.setSpacing(6)
    lbl = QLabel(label_text)
    lbl.setFixedWidth(80)
    lbl.setStyleSheet(LABEL_STYLE)
    val_lbl = QLabel(str(slider.value()))
    val_lbl.setFixedWidth(30)
    val_lbl.setStyleSheet(LABEL_STYLE)
    slider.valueChanged.connect(lambda v: val_lbl.setText(str(v)))
    row.addWidget(lbl)
    row.addWidget(slider)
    row.addWidget(val_lbl)
    return row


def _build_kick_panel():
    w = QWidget()
    w.setStyleSheet(PANEL_STYLE)
    layout = QVBoxLayout(w)
    layout.setContentsMargins(8, 6, 8, 6)
    layout.setSpacing(4)

    def on_f_start(v):
        audio.update_kick(f_start=float(v))
    def on_f_end(v):
        audio.update_kick(f_end=float(v))
    def on_duration(v):
        audio.update_kick(duration=v / 100.0)
    def on_decay(v):
        audio.update_kick(amp_decay=float(v))

    layout.addLayout(_param_row("Freq début (Hz)", _make_slider(50, 400, 150, on_f_start)))
    layout.addLayout(_param_row("Freq fin (Hz)",   _make_slider(20, 200,  50, on_f_end)))
    layout.addLayout(_param_row("Durée (×10ms)",   _make_slider(10, 200,  40, on_duration)))
    layout.addLayout(_param_row("Decay amp",        _make_slider(1,  40,   8, on_decay)))
    return w


def _build_snare_panel():
    w = QWidget()
    w.setStyleSheet(PANEL_STYLE)
    layout = QVBoxLayout(w)
    layout.setContentsMargins(8, 6, 8, 6)
    layout.setSpacing(4)

    def on_duration(v):
        audio.update_snare(duration=v / 100.0)
    def on_decay(v):
        audio.update_snare(amp_decay=float(v))

    layout.addLayout(_param_row("Durée (×10ms)", _make_slider(5, 100, 15, on_duration)))
    layout.addLayout(_param_row("Decay amp",      _make_slider(1,  60, 12, on_decay)))
    return w


def _build_hihat_panel():
    w = QWidget()
    w.setStyleSheet(PANEL_STYLE)
    layout = QVBoxLayout(w)
    layout.setContentsMargins(8, 6, 8, 6)
    layout.setSpacing(4)

    def on_duration(v):
        audio.update_hihat(duration=v / 100.0)
    def on_decay(v):
        audio.update_hihat(amp_decay=float(v))

    layout.addLayout(_param_row("Durée (×10ms)", _make_slider(2, 50,  8, on_duration)))
    layout.addLayout(_param_row("Decay amp",      _make_slider(5, 80, 25, on_decay)))
    return w


class StepButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setCheckable(True)
        self.setFixedSize(22, 28)
        self._playhead = False
        self.toggled.connect(lambda _: self._refresh())
        self._refresh()

    def set_playhead(self, active: bool):
        self._playhead = active
        self._refresh()

    def _refresh(self):
        on = self.isChecked()
        if self._playhead:
            color = "#ffcc44" if on else "#ffffff"
        else:
            color = "#e08a2b" if on else "#3a3a3a"
        self.setStyleSheet(
            "QPushButton {"
            f"background-color: {color};"
            "border: 1px solid #1e1e1e;"
            "border-radius: 2px;"
            "}"
        )


class ChannelRack(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("crea_zik - Channel Rack")
        self.setStyleSheet("background-color: #5a5a5a;")

        self._tracks = {
            "kick":  {"steps": [], "play_fn": play_kick,  "mute_btn": None, "vol_dial": None, "edit_btn": None},
            "snare": {"steps": [], "play_fn": play_snare, "mute_btn": None, "vol_dial": None, "edit_btn": None},
            "hihat": {"steps": [], "play_fn": play_hihat, "mute_btn": None, "vol_dial": None, "edit_btn": None},
        }
        self._current_step = 0
        self._playing = False
        self._open_panel: str | None = None

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(6)

        # --- header ---
        header_layout = QHBoxLayout()
        header_layout.setSpacing(4)

        self._play_btn = QPushButton("▶")
        self._play_btn.setFixedSize(28, 28)
        self._play_btn.setCheckable(True)
        self._play_btn.setStyleSheet(
            "QPushButton { background-color: #2b2b2b; color: #dddddd;"
            "border: 1px solid #1e1e1e; border-radius: 3px; }"
            "QPushButton:checked { background-color: #2db52d; color: white; }"
        )
        self._play_btn.toggled.connect(self._toggle_play)
        header_layout.addWidget(self._play_btn)

        bpm_label = QLabel("BPM")
        bpm_label.setStyleSheet("color: #dddddd; font-size: 11px;")
        header_layout.addWidget(bpm_label)

        self._bpm_spin = QSpinBox()
        self._bpm_spin.setRange(60, 300)
        self._bpm_spin.setValue(DEFAULT_BPM)
        self._bpm_spin.setFixedSize(54, 28)
        self._bpm_spin.setStyleSheet(
            "QSpinBox { background: #2b2b2b; color: #dddddd;"
            "border: 1px solid #1e1e1e; border-radius: 2px; }"
        )
        self._bpm_spin.valueChanged.connect(self._update_bpm)
        header_layout.addWidget(self._bpm_spin)

        for label, slot in [("Save", self._save_pattern), ("Load", self._load_pattern)]:
            btn = QPushButton(label)
            btn.setFixedSize(54, 28)
            btn.setStyleSheet(
                "QPushButton { background-color: #2b2b2b; color: #dddddd;"
                "border: 1px solid #1e1e1e; border-radius: 3px; }"
                "QPushButton:pressed { background-color: #444444; }"
            )
            btn.clicked.connect(slot)
            header_layout.addWidget(btn)

        header_layout.addStretch()
        main_layout.addLayout(header_layout)

        # --- tracks ---
        panels = {"kick": _build_kick_panel(), "snare": _build_snare_panel(), "hihat": _build_hihat_panel()}

        for track_name in ["kick", "snare", "hihat"]:
            track_layout = QHBoxLayout()
            track_layout.setSpacing(4)

            edit_btn = QPushButton("▾")
            edit_btn.setFixedSize(20, 28)
            edit_btn.setCheckable(True)
            edit_btn.setStyleSheet(
                "QPushButton { background-color: #2b2b2b; color: #888888;"
                "border: 1px solid #1e1e1e; border-radius: 3px; font-size: 10px; }"
                "QPushButton:checked { background-color: #4a6fa5; color: #ffffff; }"
            )
            edit_btn.toggled.connect(lambda checked, n=track_name: self._toggle_panel(n, checked))
            self._tracks[track_name]["edit_btn"] = edit_btn
            track_layout.addWidget(edit_btn)

            track_label = QLabel(track_name.upper())
            track_label.setFixedWidth(40)
            track_label.setStyleSheet("color: #dddddd; font-size: 11px;")
            track_layout.addWidget(track_label)

            track_btn = QPushButton("●")
            track_btn.setFixedSize(28, 28)
            track_btn.setStyleSheet(
                "QPushButton { background-color: #2b2b2b; color: #dddddd;"
                "border: 1px solid #1e1e1e; border-radius: 3px; }"
                "QPushButton:pressed { background-color: #444444; }"
            )
            track_btn.clicked.connect(
                lambda _, n=track_name: self._tracks[n]["play_fn"](self._tracks[n]["vol_dial"].value() / 100.0)
            )
            track_layout.addWidget(track_btn)

            mute_btn = QPushButton("M")
            mute_btn.setFixedSize(24, 28)
            mute_btn.setCheckable(True)
            mute_btn.setStyleSheet(
                "QPushButton { background-color: #2b2b2b; color: #888888;"
                "border: 1px solid #1e1e1e; border-radius: 3px; font-size: 10px; }"
                "QPushButton:checked { background-color: #993333; color: #ffffff; }"
            )
            self._tracks[track_name]["mute_btn"] = mute_btn
            track_layout.addWidget(mute_btn)

            vol_dial = QDial()
            vol_dial.setRange(0, 100)
            vol_dial.setValue(50)
            vol_dial.setFixedSize(28, 28)
            vol_dial.setNotchesVisible(False)
            vol_dial.setStyleSheet("QDial { background-color: #2b2b2b; }")
            self._tracks[track_name]["vol_dial"] = vol_dial
            track_layout.addWidget(vol_dial)

            for i in range(STEP_COUNT):
                step = StepButton()
                self._tracks[track_name]["steps"].append(step)
                track_layout.addWidget(step)
                if i % 4 == 3 and i != STEP_COUNT - 1:
                    track_layout.addSpacing(6)

            track_layout.addStretch()
            main_layout.addLayout(track_layout)

            panel = panels[track_name]
            panel.setVisible(False)
            self._tracks[track_name]["panel"] = panel
            main_layout.addWidget(panel)

    def _toggle_panel(self, track_name: str, checked: bool):
        if checked and self._open_panel and self._open_panel != track_name:
            self._tracks[self._open_panel]["edit_btn"].setChecked(False)
        self._tracks[track_name]["panel"].setVisible(checked)
        self._open_panel = track_name if checked else None
        self.adjustSize()

    def _toggle_play(self, playing: bool):
        self._playing = playing
        self._play_btn.setText("■" if playing else "▶")
        if playing:
            self._current_step = 0
            self._timer.start(self._step_ms())
        else:
            self._timer.stop()
            for track in self._tracks.values():
                for step in track["steps"]:
                    step.set_playhead(False)

    def _tick(self):
        prev = (self._current_step - 1) % STEP_COUNT
        for track in self._tracks.values():
            track["steps"][prev].set_playhead(False)
            track["steps"][self._current_step].set_playhead(True)
            if track["steps"][self._current_step].isChecked() and not track["mute_btn"].isChecked():
                track["play_fn"](track["vol_dial"].value() / 100.0)
        self._current_step = (self._current_step + 1) % STEP_COUNT

    def _save_pattern(self):
        os.makedirs(SAV_DIR, exist_ok=True)
        path, _ = QFileDialog.getSaveFileName(
            self, "Sauvegarder le pattern", os.path.join(SAV_DIR, "pattern.json"), "JSON (*.json)"
        )
        if not path:
            return
        data = {
            "bpm": self._bpm_spin.value(),
            "tracks": {
                name: {
                    "steps": [s.isChecked() for s in track["steps"]],
                    "muted": track["mute_btn"].isChecked(),
                    "volume": track["vol_dial"].value(),
                }
                for name, track in self._tracks.items()
            },
            "kick_params":  dict(audio.kick_params),
            "snare_params": dict(audio.snare_params),
            "hihat_params": dict(audio.hihat_params),
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def _load_pattern(self):
        os.makedirs(SAV_DIR, exist_ok=True)
        path, _ = QFileDialog.getOpenFileName(
            self, "Charger un pattern", SAV_DIR, "JSON (*.json)"
        )
        if not path:
            return
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        self._bpm_spin.setValue(data.get("bpm", DEFAULT_BPM))
        for name, track_data in data.get("tracks", {}).items():
            if name not in self._tracks:
                continue
            track = self._tracks[name]
            for i, checked in enumerate(track_data.get("steps", [])):
                if i < len(track["steps"]):
                    track["steps"][i].setChecked(bool(checked))
            track["mute_btn"].setChecked(bool(track_data.get("muted", False)))
            track["vol_dial"].setValue(int(track_data.get("volume", 50)))
        if "kick_params" in data:
            audio.update_kick(**data["kick_params"])
        if "snare_params" in data:
            audio.update_snare(**data["snare_params"])
        if "hihat_params" in data:
            audio.update_hihat(**data["hihat_params"])

    def _update_bpm(self, _: int):
        if self._playing:
            self._timer.setInterval(self._step_ms())

    def _step_ms(self) -> int:
        return int(60000 / self._bpm_spin.value() / 4)


def main():
    app = QApplication(sys.argv)
    window = ChannelRack()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
