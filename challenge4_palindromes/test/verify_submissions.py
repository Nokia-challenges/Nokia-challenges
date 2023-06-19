import os
from pathlib import Path

challenge_dir = Path(os.path.dirname(__file__)).parent
solution_file = challenge_dir / "solution.py"
assert solution_file.exists(), "No solution file found"

if __name__ == "__main__":
    from challenge4_palindromes.solution import run

    tests = {
        "nokiaikchallenges": ["kiaik"],
        "babad": ["bab", "aba"],
        "cbbd": ["bb"],
        "racecarsarace": ["racecar"],
        "abcdefggfedcba": ["abcdefggfedcba"],
        "abcracecarxyz": ["racecar"],
        "abcdefggfedcbaxyz": ["abcdefggfedcba"],
        "hannahlikespython": ["hannah"],
        "programmingisfun": ["mm"],
        "nevergonnagiveyouup": ["eve"],
        "pythonista": ["p", "y", "t", "h", "o", "n", "i", "s", "a"],
        "aibohphobia": ["aibohphobia"],
        "anurseissomeonewhosewhatisadequatetostheneedsorcircumstancesofapatient": [
            "tet"
        ],
        "pythoniscoolbutcodingchallengesareevenbetter": ["ette"],
        "testingapalindromefunctionforallpossiblescenarios": ["apa"],
        "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba": [
            "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba"
        ],
        "loremipsumdolorsitametconsecteturadipiscingelit": ["olo", "tet", "ipi"],
        "codingchallengestestyourskillsandimproveyourlogic": ["ll"],
        "pythonprogrammersareawesomeandcreative": ["mm"],
    }
    for test in tests:
        res = run(s=test)
        assert res, "empty response from run method, are you returning anything?"
        assert res in tests[test], f"wrong response for s = {test}"
