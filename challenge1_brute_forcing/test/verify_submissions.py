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
        == "44aeafa65f8b10498c3de32e5789633cdd73732a09494cd4baf7ec2197af33b7"
    ), f"incorrect passphrase: {passphrase}"
