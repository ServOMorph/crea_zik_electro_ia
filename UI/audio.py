import threading

import numpy as np
import sounddevice as sd

BLOCKSIZE = 256
MASTER_GAIN = 0.35

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


def synth_snare(sample_rate, duration=0.15):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    noise = np.random.normal(0, 0.3, len(t))
    amp_env = np.exp(-12.0 * t)
    wave = noise * amp_env

    fade_len = int(sample_rate * 0.005)
    fade = np.linspace(1.0, 0.0, fade_len)
    wave[-fade_len:] *= fade

    return (wave * 0.7).astype(np.float32)


def synth_hihat(sample_rate, duration=0.08):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    noise = np.random.normal(0, 0.25, len(t))
    amp_env = np.exp(-25.0 * t)
    wave = noise * amp_env

    fade_len = int(sample_rate * 0.002)
    fade = np.linspace(1.0, 0.0, fade_len)
    wave[-fade_len:] *= fade

    return (wave * 0.5).astype(np.float32)


def _callback(outdata, frames, time_info, status):
    out = np.zeros(frames, dtype=np.float32)
    with _lock:
        survivors = []
        for samples, pos, gain in _voices:
            chunk = samples[pos:pos + frames]
            n = len(chunk)
            out[:n] += chunk * gain
            new_pos = pos + n
            if new_pos < len(samples):
                survivors.append([samples, new_pos, gain])
        _voices[:] = survivors
    out *= MASTER_GAIN
    np.tanh(out, out=out)
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

kick_params = {"duration": 0.4, "f_start": 150.0, "f_end": 50.0, "amp_decay": 8.0}
snare_params = {"duration": 0.15, "amp_decay": 12.0}
hihat_params = {"duration": 0.08, "amp_decay": 25.0}

_KICK = synth_kick(SAMPLE_RATE, **{k: v for k, v in kick_params.items() if k != "amp_decay"})
_SNARE = synth_snare(SAMPLE_RATE)
_HIHAT = synth_hihat(SAMPLE_RATE)


def update_kick(**kwargs):
    global _KICK
    kick_params.update(kwargs)
    t = np.linspace(0, kick_params["duration"], int(SAMPLE_RATE * kick_params["duration"]), endpoint=False)
    pitch_env = kick_params["f_end"] + (kick_params["f_start"] - kick_params["f_end"]) * np.exp(-30.0 * t)
    phase = 2 * np.pi * np.cumsum(pitch_env) / SAMPLE_RATE
    amp_env = np.exp(-kick_params["amp_decay"] * t)
    wave = np.sin(phase) * amp_env
    fade_len = int(SAMPLE_RATE * 0.01)
    wave[-fade_len:] *= np.linspace(1.0, 0.0, fade_len)
    new = (wave * 0.9).astype(np.float32)
    with _lock:
        _KICK = new


def update_snare(**kwargs):
    global _SNARE
    snare_params.update(kwargs)
    t = np.linspace(0, snare_params["duration"], int(SAMPLE_RATE * snare_params["duration"]), endpoint=False)
    noise = np.random.normal(0, 0.3, len(t))
    wave = noise * np.exp(-snare_params["amp_decay"] * t)
    fade_len = int(SAMPLE_RATE * 0.005)
    wave[-fade_len:] *= np.linspace(1.0, 0.0, fade_len)
    new = (wave * 0.7).astype(np.float32)
    with _lock:
        _SNARE = new


def update_hihat(**kwargs):
    global _HIHAT
    hihat_params.update(kwargs)
    t = np.linspace(0, hihat_params["duration"], int(SAMPLE_RATE * hihat_params["duration"]), endpoint=False)
    noise = np.random.normal(0, 0.25, len(t))
    wave = noise * np.exp(-hihat_params["amp_decay"] * t)
    fade_len = int(SAMPLE_RATE * 0.002)
    wave[-fade_len:] *= np.linspace(1.0, 0.0, fade_len)
    new = (wave * 0.5).astype(np.float32)
    with _lock:
        _HIHAT = new


def play_kick(gain: float = 1.0):
    with _lock:
        _voices.append([_KICK, 0, gain])


def play_snare(gain: float = 1.0):
    with _lock:
        _voices.append([_SNARE, 0, gain])


def play_hihat(gain: float = 1.0):
    with _lock:
        _voices.append([_HIHAT, 0, gain])
