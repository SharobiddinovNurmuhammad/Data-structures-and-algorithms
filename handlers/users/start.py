import sqlite3

from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.signup_kebr import signup_keyboard
from states.signup import Signup
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}!"
                         f"\nBotdan to'liq foydalanish uchun kontaktingizni botga ulashing!",
                         reply_markup=signup_keyboard)
    await state.update_data(
        {'user_id': message.from_user.id,
         'full_name': message.from_user.full_name
         }
    )
    await Signup.phone_number.set()

@dp.message_handler(state=Signup.phone_number, content_types='contact')
async def signup_fullname(message: Message, state: FSMContext):
    contact = message.contact
    await state.update_data(
        {'kontakt': message.contact.phone_number}
    )
    data = await state.get_data()
    user_id = data.get('user_id')
    full_name = data.get('full_name')
    kontakt = data.get('kontakt')
    await message.answer(f"{user_id} {full_name} {kontakt}")
    try:
        db.add_user(user_id, full_name, kontakt)
    except:
        pass
    users = db.select_all_users()
    print(users)
    await state.finish()

