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
        == 'a8df85f48fda63ef483c4b9c784254e34198036a2aeb44553020ca654acdab46'
    ), f"incorrect passphrase: {passphrase}"
