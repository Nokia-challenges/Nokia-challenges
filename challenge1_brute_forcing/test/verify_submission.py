import os
from pathlib import Path

challenge_dir = Path(os.path.dirname(__file__)).parent
solution_file = challenge_dir / "solutions/passphrase.txt"

if __name__ == '__main__':
    with open(solution_file, "r") as f:
        passphrase = f.read()

    assert passphrase == str(42)
