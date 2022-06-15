import hashlib


def check_password(pwd):
    return (
        hashlib.sha256(pwd.encode("utf-8")).hexdigest()
        == "fb68cc8c2401d4939d3b1f1a66d713f8b78e89f99a3837e340af289db3f1402b"
    )
