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
        == 'dfe94209aa98b895a98cf0f1da1dc73b026c59318cee3a4cbe81f62096c93c2c'
    ), f"incorrect passphrase: {passphrase}"

