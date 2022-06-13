import hashlib


def check_password(pwd):
    return (
        hashlib.sha256(pwd.encode("utf-8")).hexdigest()
        == "8b01e15594a3790356409c685c434520bf88b2dbc71e20192f84e497b63dfaf5"
    )
