from typing import Dict, Optional

from datetime import datetime

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def get_full_name(self) -> str:
        return self.first_name + " " + self.last_name

    def is_first_name_good(self):
        is_good = True if self.first_name and self.first_name is not None and self.first_name != "Doh" and self.first_name != "A" else False
        return is_good

    def user_time(self):
        var = f"{self.first_name}{self.first_name}{self.first_name}{self.first_name}{self.first_name}{self.first_name}"
        return datetime.now()

user = User("Bob", "Bobob")

if user.get_full_name().upper().split(' ')[0] == 'Alex':
    print("Some important logic")
