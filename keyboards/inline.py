from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_yes_no = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text="Да", callback_data="Yes"),
                                          InlineKeyboardButton(text="Нет", callback_data="No")
                                      ]
                                  ])

ikb_note_yes_no = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(text="Да", callback_data="Note_yes"),
                                               InlineKeyboardButton(text="Нет", callback_data="Note_no")
                                           ]
                                       ])
