"""
Automatically creates a discord account and login
into it, after receiving an authorization token
from the headers "authorization"
"""
import argparse
import secrets
from time import sleep

from pyfiglet import Figlet
from rich.console import Console

from .user import SeleniumUser

TITLE = "User Generator"


def password_generator(strong: int = 10) -> str:
    """
    Password generator, for new user
    """
    password = secrets.token_hex(strong)
    return password


def parse_args():
    """
    Args from command line,
    Email, and Nickname
    """
    parser = argparse.ArgumentParser(
        description="Nickname and Email for new discord account."
    )
    parser.add_argument(
        "-username",
        dest="username",
        type=str,
        help="User name of new discord account",
        required=True,
    )
    parser.add_argument(
        "-email",
        dest="email",
        type=str,
        help="Email name of new discord account",
        required=True,
    )

    args = parser.parse_args()
    return args.username, args.email


def main():
    """
    Start function,
    call's functions
    """
    console = Console()
    custom_fig = Figlet(font="colossal")
    console.print(custom_fig.renderText(TITLE))

    args = parse_args()
    user_name, email = args
    password = password_generator()
    console.print(f"User: {user_name}\nEmail: {email}\nPassword: {password}")
    user = SeleniumUser(email, user_name, password)
    user.register()
    sleep(30)
    console.print(f"User has token: {user.get_token()}")
    console.print("Press Enter or Return to exit ...")


if __name__ == "__main__":
    main()
    input()
