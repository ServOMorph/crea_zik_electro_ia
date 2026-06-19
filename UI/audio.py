import threading

import numpy as np
import sounddevice as sd

BLOCKSIZE = 256

_voices: list[list] = []
_lock = threading.Lock()


def synth_kick(sample_rate, duration=0.4, f_start=150.0, f_end=50.0):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    pitch_env = f_end + (f_start - f_end) * np.exp(-30.0 * t)
    phase = 2 * np.pi * np.cumsum(pitch_env) / sample_rate
    amp_env = np.exp(-8.0 * t)
    wave = np.sin(phase) * amp_env

    fade_len = int(sample_rate * 0.01)
    fade = np.linspace(1.0, 0.0, fade_len)
    wave[-fade_len:] *= fade

    return (wave * 0.9).astype(np.float32)


def _callback(outdata, frames, time_info, status):
    out = np.zeros(frames, dtype=np.float32)
    with _lock:
        survivors = []
        for samples, pos in _voices:
            chunk = samples[pos:pos + frames]
            n = len(chunk)
            out[:n] += chunk
            new_pos = pos + n
            if new_pos < len(samples):
                survivors.append([samples, new_pos])
        _voices[:] = survivors
    np.clip(out, -1.0, 1.0, out=out)
    outdata[:, 0] = out


def _pick_device():
    for host in sd.query_hostapis():
        if "WASAPI" in host["name"]:
            dev = host["default_output_device"]
            if dev >= 0:
                return dev
    return None


def _open_stream():
    device = _pick_device()
    sample_rate = None
    if device is not None:
        sample_rate = int(sd.query_devices(device)["default_samplerate"])
    try:
        stream = sd.OutputStream(
            samplerate=sample_rate,
            channels=1,
            dtype="float32",
            blocksize=BLOCKSIZE,
            device=device,
            latency="low",
            callback=_callback,
        )
        stream.start()
        return stream
    except Exception:
        stream = sd.OutputStream(
            samplerate=None,
            channels=1,
            dtype="float32",
            blocksize=BLOCKSIZE,
            latency="low",
            callback=_callback,
        )
        stream.start()
        return stream


_stream = _open_stream()
SAMPLE_RATE = int(_stream.samplerate)
_KICK = synth_kick(SAMPLE_RATE)


def play_kick():
    with _lock:
        _voices.append([_KICK, 0])
