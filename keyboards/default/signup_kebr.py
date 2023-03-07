from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

signup_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Kontakt", request_contact=True)
        ]
    ]
)