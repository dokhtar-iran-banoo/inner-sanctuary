import telebot
from telebot import types

# توکن ربات شما
TOKEN = "8821918492:AAEfFkeaXju6G-zwGzPXE1Fj2oZeMl9iaZc"
bot = telebot.TeleBot(TOKEN)


# دستور شروع و منوی اصلی
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
  btn1 = types.KeyboardButton("🏠 خانه آرامش")
  btn2 = types.KeyboardButton("📝 تأمل روزانه")
  btn3 = types.KeyboardButton("🎶 موسیقی و سکوت")
  markup.add(btn1, btn2, btn3)

  welcome_text = (
      "✨ *پناهگاه درون (Inner Sanctuary)* ✨\n\nبه فضای امن خودت خوش آمدی. اینجا"
      " جایی برای آرامش، مکث و بازیافتن انرژی توست.\nاز منوی زیر یکی را انتخاب"
      " کن:"
  )
  bot.send_message(
      message.chat.id,
      welcome_text,
      parse_mode="Markdown",
      reply_markup=markup,
  )


# مدیریت انتخاب‌های منو
@bot.message_handler(func=lambda message: True)
def handle_message(message):
  if message.text == "🏠 خانه آرامش":
    markup = types.InlineKeyboardMarkup()
    btn_good = types.InlineKeyboardButton(
        "حالم خوب شد 🌸", callback_data="feeling_good"
    )
    markup.add(btn_good)

    text = (
        "🌱 *یک نفس عمیق بکش...*\n\n* دستت را روی قلبت بگذار.\n* آرام از طریق"
        " بینی نفس بکش... و به آرامی بیرون بده.\n* تو در این لحظه کاملاً امن"
        " هستی."
    )
    bot.send_message(
        message.chat.id, text, parse_mode="Markdown", reply_markup=markup
    )

  elif message.text == "📝 تأمل روزانه":
    bot.send_message(
        message.chat.id,
        "✍️ امروز چه حسی داری؟ هر چه در دل داری بنویس (پیام خود را بفرست):",
    )
    bot.register_next_step_handler(message, save_user_reflection)

  elif message.text == "🎶 موسیقی و سکوت":
    text = (
        "🎧 *لحظه‌ای سکوت و آرامش*\n\nچشمانت را ببند و چند لحظه به صدای"
        " نفس‌هایت گوش بده.\n\n[سفر به درون -"
        " تصویر](https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80)"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

  else:
    bot.send_message(
        message.chat.id, "لطفاً از دکمه‌های پایین صفحه یکی را انتخاب کن 🌸"
    )


# دریافت متن یادداشت کاربر
def save_user_reflection(message):
  user_text = message.text
  if user_text:
    bot.send_message(
        message.chat.id,
        "حست اینجا امن و محفوظ ماند. ممنون که با خودت مهربانی. 🤍",
    )
  else:
    bot.send_message(message.chat.id, "لطفاً چند کلمه‌ای بنویس.")


# مدیریت دکمه‌های شیشه‌ای
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  if call.data == "feeling_good":
    bot.answer_callback_query(call.id, "خوشحالم که حالت خوبه! 🌸")
    bot.send_message(
        call.chat.id, "🎈 لبخند تو زیباترین بخش این فضاست! 🌸"
    )


# اجرای ربات
print("Bot is running...")
bot.infinity_polling()
