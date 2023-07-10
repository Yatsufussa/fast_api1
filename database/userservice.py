from database.models import User, Password
from database import get_db


# User Registration
def register_user_db(**kwargs):
    db = next(get_db())
    phone_number = kwargs.get('phone_number')

    # Phone Number Checker
    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return "User with such number already exist"
    # If no such user in database then registration
    new_user = User(**kwargs)
    db.add(new_user)
    db.commit()

    # Create password
    new_user_password = Password(user_id=new_user.user_id, **kwargs)
    db.add(new_user_password)

    return "User successfully added into database"


# Password checker
def check_password_db(phone_number, password):
    db = next(get_db())
    checker = db.query(Password).filter_by(phone_number=phone_number).first()

    if checker and checker.password == password:
        return checker.user_id

    elif not checker:
        return "Number error"

    elif checker.password != password:
        return "Something get wrong"


# Getting User Info
def get_user_cabinet_db(user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(user_id=user_id).first()

    if checker:
        return checker
    return "Data Error"
