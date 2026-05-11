from telegram import (
    Update,
    BotCommand
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

from menus import main_menu, season1_menu
from handlers import handle_message

TOKEN = "8241049762:AAGOFBBYAObQAOEC9JAYTTF2E1SJjBW18nw"

# قناة الاشتراك الاجباري
CHANNEL_ID = "@series6781"

# قناة الحلقات
CHANNEL_ID_2 = "-1003878027999"


# ---------------- التحقق من الاشتراك ----------------

async def is_subscribed(user_id, bot):

    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)

        return member.status in [
            "member",
            "administrator",
            "creator"
        ]

    except:
        return False

# ---------------- START ----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    # تحقق اشتراك
    if not await is_subscribed(user_id, context.bot):

        await update.message.reply_text(
            f"❌ يجب الاشتراك بالقناة أولاً:\nhttps://t.me/series6781"
        )

        return

    await update.message.reply_text(
        "اختر الموسم 👇",
        reply_markup=main_menu()
    )

# ---------------- تشغيل البوت ----------------

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
)


# ---------------- أوامر المينو ----------------

async def post_init(application):

    await application.bot.set_my_commands([
        BotCommand("start", "تشغيل البوت")
    ])

app.post_init = post_init


print("Bot Running...")

app.run_polling()
