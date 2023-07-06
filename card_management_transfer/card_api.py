from main import app


# Add Card
@app.post('/add-user-card')
async def add_user_card(user_id: int,cardholder: str, card_name: str, card_number: int, exp_date: int, otp: int):
    pass


# Generation of checking code
@app.get('/one-time-password')
async def get_one_time_password(transfer_id: int):
    pass


# Money Transfer
@app.post('/transfer-user-money')
async def transfer_money_api(card_from: int, card_to: int, otp: int):
    pass


# Delete Card
@app.delete('/delete-user-card')
async def delete_user_card(card_id: int, user_id: int):
    pass


# Get Card
@app.get('/get-user-cards')
async def get_exact_or_all_cards(user_id: int, card: int = 0):
    pass


# Get history of the card
@app.get('/get-card-monitoring')
async def get_exact_all_card_monitoring(user_id: int, card: int = 0):
    pass

