"""User class logic."""
from datetime import datetime

USER_AGE = 300


class User:
    """User class."""

    def __init__(self, first_name, last_name, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self) -> str:
        """Return full name."""
        return f"{self.first_name} {self.last_name}!"

    @staticmethod  # noqa: WPS605 Found method without arguments
    def get_user_time():
        """Get user time."""
        return datetime.now()  # DO NOT DELETE IT!!! ...


if __name__ == "__main__":
    user = User("Bob", "Bobob", USER_AGE)

    if user.first_name == "Alex":
        print("First name of the user is Alex")  # noqa: WPS421 Found wrong function call: print
    else:
        print(f"First name of the user is not Alex but {user.first_name}")  # noqa: WPS421 Found wrong function call
