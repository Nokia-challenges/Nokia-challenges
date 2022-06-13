import hashlib
import os
from pathlib import Path

challenge_dir = Path(os.path.dirname(__file__)).parent
solution_file = challenge_dir / "passphrase.txt"
assert solution_file.exists(), "No solution file found"

if __name__ == "__main__":
    with open(solution_file, "r") as f:
        passphrase = f.read()

    assert len(passphrase) > 0, "Empty passphrase"
    assert (
        hashlib.sha256(passphrase.encode("utf-8")).hexdigest()
        == '8b01e15594a3790356409c685c434520bf88b2dbc71e20192f84e497b63dfaf5'
    ), f"incorrect passphrase: {passphrase}"
