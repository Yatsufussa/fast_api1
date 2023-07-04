from main import app


# User Registration
@app.post('/register-user')
async def register_user_api(phone_number: int, name: str, pincode: int, password: str):
    pass


# Log Into Account
@app.get('/login')
async def login_user_api(phone_number: int, password: str):
    pass


# User Info
@app.get('/user-cabinet')
async def get_user_cabinet_api(user_id: int):
    pass


# Get cards from phone number
@app.get('/get-user-cards-by-phone')
async def get_user_card_by_phone_number_api(phone_number: int):
    pass
