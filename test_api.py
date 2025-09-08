import json
import time
import subprocess
import sys
from pathlib import Path

import requests


API_URL = "http://localhost:8000"


def wait_for_health(timeout_seconds: int = 15) -> None:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        try:
            r = requests.get(f"{API_URL}/health", timeout=2)
            if r.status_code == 200 and r.json().get("status") == "ok":
                return
        except Exception:
            pass
        time.sleep(0.5)
    raise RuntimeError("API did not become healthy in time")


def main() -> None:
    # Start server only if not already running
    server_proc = None
    try:
        try:
            requests.get(f"{API_URL}/health", timeout=1)
            server_running = True
        except Exception:
            server_running = False

        if not server_running:
            # Start uvicorn in a subprocess
            server_proc = subprocess.Popen(
                [sys.executable, "-m", "uvicorn", "app:app", "--host", "localhost", "--port", "8000"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            wait_for_health()

        # Fetch debug info to verify feature expectations
        dbg = requests.get(f"{API_URL}/debug", timeout=5)
        if dbg.ok:
            print("/debug:", dbg.json())
        else:
            print("/debug non-200:", dbg.status_code, dbg.text)

        # Build a valid example payload (matches InputData example)
        payload = {
            "RhythmScore": 0.42,
            "AudioLoudness": -7.3,
            "VocalContent": 0.61,
            "AcousticQuality": 0.35,
            "InstrumentalScore": 0.18,
            "LivePerformanceLikelihood": 0.05,
            "MoodScore": 0.72,
            "TrackDurationMs": 210000.0,
            "Energy": 0.8,
        }

        resp = requests.post(f"{API_URL}/predict_json", json=payload, timeout=10)
        if resp.status_code != 200:
            print("Non-200 response:", resp.status_code)
            try:
                print("Body:", resp.json())
            except Exception:
                print("Body (text):", resp.text)
            resp.raise_for_status()
        data = resp.json()
        prediction = data.get("prediction")
        assert isinstance(prediction, (int, float)), "Prediction must be a number"
        print("Prediction:", prediction)

    finally:
        if server_proc is not None:
            try:
                server_proc.terminate()
            except Exception:
                pass


if __name__ == "__main__":
    main()


