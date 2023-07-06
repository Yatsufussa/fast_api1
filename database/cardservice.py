from database.models import Card, User, Transaction
from database import get_db


# Add Card into database
def add_user_card_db(**kwargs):
    db = next(get_db())
    card_number = kwargs.get('card_number')

    # Checking the addition of the card into database
    checker = db.query(Card).filter_by(card_number=card_number).first()

    if checker:
        return 'Card is already in base'

    new_card = Card(**kwargs)
    db.add(new_card)
    db.commit()

    return "Card Successfully Added"


# Transfer from card to card                    HW
def transfer_money_db(card_from, card_to, date):
    pass


# Delete card from service
def delete_user_card_db(card_id, user_id):
    pass


# Get all cards from phone number flter_by(all)
def get_user_cards_by_phone_number_db(phone_number):
    pass


# Get specific Info about card
def get_exact_user_card_db(user_id, card_id):
    pass


# get all transactions by exact card,or by all if 0 all,else
def get_all_cards_or_exact_transaction(user_id, card_id):
    db = next(get_db())
    if card_id == 0:
        card_monitor = db.query(Transaction).filter_by(user_id=user_id).all()

    else:
        card_monitor = db.query(Transaction).filter_by(user_id=user_id, card_id=card_id).all()

    return card_monitor