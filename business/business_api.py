from main import app


# Business category registration
@app.post('/register-business-category')
async def register_business_category_api(name: str):
    pass


# Business registration
@app.post('/register_business')
async def register_business_api(category_id: int, name: str, card_number: int):
    pass


# All Categories
@app.get('/get-all-categories')
async def get_business_categories(exact_category_id: int = 0):
    pass


# Вывод Услуг
@app.get('/get-business')
async def get_exact_business_api(business_id: int, category_id: int):
    pass


# Оплата Услуг
@app.post('/pay-service')
async def pay_for_service(business_id: int, from_card: int, amount: float):
    pass


# Delete business
@app.delete('/delete-business')
async def delete_business_api(business_id: int):
    pass


# Delete category
@app.delete('/delete-business')
async def delete_business_api(category_id: int):
    pass
