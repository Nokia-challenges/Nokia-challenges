import os
from pathlib import Path

import requests

challenge_dir = Path(os.path.dirname(__file__)).parent
solution_file = challenge_dir / "solution.py"
assert solution_file.exists(), "No solution file found"

if __name__ == "__main__":
    from challenge2_ISS_apis.solution import run

    calculated_speed = run()
    assert (
        calculated_speed
    ), "empty response from run method, are you returning anything?"
    real_speed = requests.get("https://api.wheretheiss.at/v1/satellites/25544").json()[
        "velocity"
    ]
    assert (
        real_speed * 0.9 < calculated_speed < real_speed * 1.1
    ), f"incorrect speed: {calculated_speed}"
