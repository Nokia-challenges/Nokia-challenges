import os
from pathlib import Path

challenge_dir = Path(os.path.dirname(__file__)).parent
solution_file = challenge_dir / "solutions/passphrase.txt"
assert solution_file.exists(), "No solution file found"

if __name__ == "__main__":
    pass
