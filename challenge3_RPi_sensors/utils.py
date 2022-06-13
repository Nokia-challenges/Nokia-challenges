import hashlib


def check_password(pwd):
    return (
            hashlib.sha256(pwd.encode("utf-8")).hexdigest()
            == 'a8df85f48fda63ef483c4b9c784254e34198036a2aeb44553020ca654acdab46'
    )
