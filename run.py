import subprocess
import sys
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

UI_DIR = Path(__file__).parent / "UI"
ENTRY = [sys.executable, str(UI_DIR / "main.py")]
DEBOUNCE = 0.5


class _ReloadHandler(FileSystemEventHandler):
    def __init__(self, proc: list[subprocess.Popen]):
        self._proc = proc
        self._last = 0.0

    def on_modified(self, event):
        if not str(event.src_path).endswith(".py"):
            return
        now = time.monotonic()
        if now - self._last < DEBOUNCE:
            return
        self._last = now
        print(f"[run] change: {Path(event.src_path).name} — reloading")
        self._proc[0].terminate()
        self._proc[0].wait()
        self._proc[0] = subprocess.Popen(ENTRY)


def main():
    proc: list[subprocess.Popen] = [subprocess.Popen(ENTRY)]
    handler = _ReloadHandler(proc)
    observer = Observer()
    observer.schedule(handler, str(UI_DIR), recursive=False)
    observer.start()
    print(f"[run] watching {UI_DIR}  — Ctrl+C to stop")
    try:
        while proc[0].poll() is None:
            time.sleep(0.5)
        observer.stop()
    except KeyboardInterrupt:
        observer.stop()
        proc[0].terminate()
    observer.join()


if __name__ == "__main__":
    main()
