from typing import Dict, Optional

from datetime import datetime

class User:

    def __init__(self, first_name, last_name, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self) -> str:
        return self.first_name + " " + self.last_name

    def strange_bad_method(self):

        is_good = True if self.first_name and self.first_name is not None and self.first_name != "Doh" and self.first_name != "A" else False
        return is_good

    def get_user_time(self):
        var = f"{self.first_name}{self.first_name}{self.first_name}{self.first_name}{self.first_name}{self.first_name}"
        return datetime.now()


if __name__ == "__main__":
    user = User("Bob", "Bobob", "300")

    if user.get_full_name().upper().split(' ')[0] == 'Alex':
        print("First name of the user is Alex")  # noqa: WPS421 Found wrong function call: print
    else:
        print(f"First name of the user is not Alex but {user.first_name}")
