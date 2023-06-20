import hashlib


def check_password(pwd):
    return (
        hashlib.sha256(pwd.encode("utf-8")).hexdigest()
        == "44aeafa65f8b10498c3de32e5789633cdd73732a09494cd4baf7ec2197af33b7"
    )
