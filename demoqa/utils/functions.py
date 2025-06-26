from tests_data.user_info import User


def valid_info(user: User):

    return [
        f"Name:{user.full_name}",
        f"Email:{user.email}",
        f"Current Address :{user.current_address}",
        f"Permananet Address :{user.permanent_address}",
    ]
