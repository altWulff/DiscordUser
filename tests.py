import secrets
from src.main import password_generator


def test_password_generator():
    strong = 10
    password = password_generator(strong)
    assert len(password) == strong * 2


def test_user_create():
    pass


def test_user_login():
    pass
