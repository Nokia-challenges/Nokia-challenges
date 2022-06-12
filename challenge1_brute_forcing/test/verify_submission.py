import hashlib
import os
from pathlib import Path

challenge_dir = Path(os.path.dirname(__file__)).parent
solution_file = challenge_dir / "solutions/passphrase.txt"

if __name__ == "__main__":
    with open(solution_file, "r") as f:
        passphrase = f.read()

    assert (
        hashlib.sha224(passphrase.encode('utf-8')).hexdigest() == "33624935aa346e032eaa4b634f76b1e4a2f5b4b52f5d4b49d4b466c7"
    ), f"incorrect passphrase: {passphrase}"
