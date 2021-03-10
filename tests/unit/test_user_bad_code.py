from app.user_bad_code import User


def test_user_get_full_name():
    user = User("Alex", "Alexxx", 300)
    assert user.get_full_name() == "Alex 111"
    assert user.age == 300
