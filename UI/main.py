import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSpinBox,
    QWidget,
)

from audio import play_kick

STEP_COUNT = 16
DEFAULT_BPM = 120


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

        self._steps: list[StepButton] = []
        self._current_step = 0
        self._playing = False

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(4)

        self._play_btn = QPushButton("▶")
        self._play_btn.setFixedSize(28, 28)
        self._play_btn.setCheckable(True)
        self._play_btn.setStyleSheet(
            "QPushButton { background-color: #2b2b2b; color: #dddddd;"
            "border: 1px solid #1e1e1e; border-radius: 3px; }"
            "QPushButton:checked { background-color: #2db52d; color: white; }"
        )
        self._play_btn.toggled.connect(self._toggle_play)
        layout.addWidget(self._play_btn)

        bpm_label = QLabel("BPM")
        bpm_label.setStyleSheet("color: #dddddd; font-size: 11px;")
        layout.addWidget(bpm_label)

        self._bpm_spin = QSpinBox()
        self._bpm_spin.setRange(60, 300)
        self._bpm_spin.setValue(DEFAULT_BPM)
        self._bpm_spin.setFixedSize(54, 28)
        self._bpm_spin.setStyleSheet(
            "QSpinBox { background: #2b2b2b; color: #dddddd;"
            "border: 1px solid #1e1e1e; border-radius: 2px; }"
        )
        self._bpm_spin.valueChanged.connect(self._update_bpm)
        layout.addWidget(self._bpm_spin)

        layout.addSpacing(8)

        kick_btn = QPushButton("Kick")
        kick_btn.setFixedSize(70, 28)
        kick_btn.setStyleSheet(
            "QPushButton { background-color: #2b2b2b; color: #dddddd;"
            "border: 1px solid #1e1e1e; border-radius: 3px; }"
            "QPushButton:pressed { background-color: #444444; }"
        )
        kick_btn.clicked.connect(play_kick)
        layout.addWidget(kick_btn)

        layout.addSpacing(8)

        for i in range(STEP_COUNT):
            step = StepButton()
            self._steps.append(step)
            layout.addWidget(step)
            if i % 4 == 3 and i != STEP_COUNT - 1:
                layout.addSpacing(6)

        layout.addStretch()

    def _toggle_play(self, playing: bool):
        self._playing = playing
        self._play_btn.setText("■" if playing else "▶")
        if playing:
            self._current_step = 0
            self._timer.start(self._step_ms())
        else:
            self._timer.stop()
            for step in self._steps:
                step.set_playhead(False)

    def _tick(self):
        prev = (self._current_step - 1) % STEP_COUNT
        self._steps[prev].set_playhead(False)
        self._steps[self._current_step].set_playhead(True)
        if self._steps[self._current_step].isChecked():
            play_kick()
        self._current_step = (self._current_step + 1) % STEP_COUNT

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
