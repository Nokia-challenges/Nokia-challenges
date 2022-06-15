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
        == "fb68cc8c2401d4939d3b1f1a66d713f8b78e89f99a3837e340af289db3f1402b"
    ), f"incorrect passphrase: {passphrase}"
