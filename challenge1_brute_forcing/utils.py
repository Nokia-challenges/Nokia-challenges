import hashlib


def check_password(pwd):
    return hashlib.sha224(pwd.encode("utf-8")).hexdigest() == "33624935aa346e032eaa4b634f76b1e4a2f5b4b52f5d4b49d4b466c7"
