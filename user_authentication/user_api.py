from main import app
from database import register_user_db, check_password_db, get_user_cabinet_db
from datetime import datetime


# User Registration
@app.post('/register-user')
async def register_user_api(phone_number: int, name: str, pincode: int, password: str):
    result = register_user_db(phone_number=phone_number,
                              name=name,
                              password=password,
                              pincode=pincode,
                              reg_date=datetime.now())

    return {'status': 1, 'message': result}


# Log Into Account
@app.get('/login')
async def login_user_api(phone_number: int, password: str):
    result = check_password_db(phone_number=phone_number, password=password)
    return {'status': 1, 'message': result}


# User Info
@app.get('/user-cabinet')
async def get_user_cabinet_api(user_id: int):
    result = get_user_cabinet_db(user_id=user_id)
    return {'status': 1, 'message': result}


# Get cards from phone number
@app.get('/get-user-cards-by-phone')
async def get_user_card_by_phone_number_api(phone_number: int):
    pass
