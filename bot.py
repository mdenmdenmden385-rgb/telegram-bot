from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8241049762:AAGOFBBYAObQAOEC9JAYTTF2E1SJjBW18nw"
CHANNEL_ID = "@series6781"
CHANNEL_ID_2 = "-1003878027999"


# 🔹 /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_ID, user_id)

        if member.status in ["member", "administrator", "creator"]:

            keyboard = [
                [InlineKeyboardButton("🎬 الموسم الأول", callback_data="season1")],
                [InlineKeyboardButton("🎬 الموسم الثاني", callback_data="season2")],
                [InlineKeyboardButton("🎬 الموسم الثالث", callback_data="season3")],
                [InlineKeyboardButton("🎬 الموسم الرابع", callback_data="season4")],
            ]

            await update.message.reply_text(
                "اختر الموسم 👇",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        else:
            await update.message.reply_text(f"❌ لازم تشترك أولاً:\nhttps://t.me/series6781")

    except:
        await update.message.reply_text("\nhttps://t.me/series6781  ❌ اشترك بالقناة أولاً")


# 🔹 إرسال رسائل من القناة مباشرة
async def send_episode(update: Update, context: ContextTypes.DEFAULT_TYPE, msg_id):
    query = update.callback_query
    await query.answer()

    await context.bot.copy_message(
        chat_id=query.message.chat_id,
        from_chat_id=CHANNEL_ID,
        message_id=msg_id
    )


# 🔹 الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    # 🎬 الموسم الأول (الرسائل 4-7)
    if query.data == "season1":
        await query.answer()
        await query.message.reply_text("🎬 الموسم الأول:")

        for msg_id in range(19, 27):
            await context.bot.copy_message(
                chat_id=query.message.chat_id,
                from_chat_id=CHANNEL_ID_2,
                message_id=msg_id
            )

    # 🎬 الموسم الثاني
    elif query.data == "season2":
        await query.answer()
        await query.message.reply_text("🎬 الموسم الثاني:")

        for msg_id in range(27, 35):
            await context.bot.copy_message(
                chat_id=query.message.chat_id,
                from_chat_id=CHANNEL_ID_2,
                message_id=msg_id
            )

    # 🎬 الموسم الثالث
    elif query.data == "season3":
        await query.answer()
        await query.message.reply_text("🎬 الموسم الثالث:")

        for msg_id in range(35, 45):
            await context.bot.copy_message(
                chat_id=query.message.chat_id,
                from_chat_id=CHANNEL_ID_2,
                message_id=msg_id
            )

    # 🎬 الموسم الرابع
    elif query.data == "season4":
        await query.answer()
        await query.message.reply_text("🎬 الموسم الرابع:")

        for msg_id in range(45, 55):
            await context.bot.copy_message(
                chat_id=query.message.chat_id,
                from_chat_id=CHANNEL_ID_2,
                message_id=msg_id
            )


# 🔹 تشغيل البوت
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
