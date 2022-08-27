"""
Base tests
"""


from src.main import password_generator


def test_password_generator():
    """
    Test password length
    """
    strong = 10
    password = password_generator(strong)
    assert len(password) == strong * 2
