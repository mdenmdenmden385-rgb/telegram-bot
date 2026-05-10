from telegram import Update
from telegram.ext import ContextTypes
from menus import main_menu, season1_menu, season2_menu, season3_menu, season4_menu, season5_menu


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
    

# ---------------- التعامل مع الازرار ----------------

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    # تحقق اشتراك عند أي ضغط زر
    if not await is_subscribed(user_id, context.bot):

        await update.message.reply_text(
            f"❌ يجب الاشتراك بالقناة أولاً:\nhttps://t.me/series6781"
        )

        return

    text = update.message.text

    # الموسم الاول
    if text == "🎬 الموسم الاول":

        await update.message.reply_text(
            "اختر الحلقة 👇",
            reply_markup=season1_menu()
        )

    # رجوع
    elif text == "🔙 رجوع":

        await update.message.reply_text(
            "رجعنا للقائمة الرئيسية 👇",
            reply_markup=main_menu()
        )

    # الحلقة 1
    elif text == "S1E1":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=19
        )

    # الحلقة 2
    elif text == "S1E2":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=20
        )

    # الحلقة 3
    elif text == "S1E3":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=21
        )

    # الحلقة 4
    elif text == "S1E4":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=22
        )

    # الحلقة 5
    elif text == "S1E5":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=23
        )

    # الحلقة 6
    elif text == "S1E6":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=24
        )

    # الحلقة 7
    elif text == "S1E7":
        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=25
        )

    # الحلقة 8
    elif text == "S1E8":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=26
        )




    # الموسم الثاني
    elif text == "🎬 الموسم الثاني":

        await update.message.reply_text(
            "اختر الحلقة 👇",
            reply_markup=season2_menu()
        )

    # رجوع
    elif text == "🔙 رجوع":

        await update.message.reply_text(
            "رجعنا للقائمة الرئيسية 👇",
            reply_markup=main_menu()
        )

    # الحلقة 1
    elif text == "S2E1":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=27
        )

    # الحلقة 2
    elif text == "S2E2":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=28
        )

    # الحلقة 3
    elif text == "S2E3":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=29
        )

    # الحلقة 4
    elif text == "S2E4":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=30
        )

    # الحلقة 5
    elif text == "S2E5":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=31
        )

    # الحلقة 6
    elif text == "S2E6":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=32
        )

    # الحلقة 7
    elif text == "S2E7":
        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=33
        )

    # الحلقة 8
    elif text == "S2E8":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=34
        )


    
    # الموسم الثالث
    elif text == "🎬 الموسم الثالث":

        await update.message.reply_text(
            "اختر الحلقة 👇",
            reply_markup=season3_menu()
        )

    # رجوع
    elif text == "🔙 رجوع":

        await update.message.reply_text(
            "رجعنا للقائمة الرئيسية 👇",
            reply_markup=main_menu()
        )

    # الحلقة 1
    elif text == "S3E1":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=35
        )

    # الحلقة 2
    elif text == "S3E2":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=36
        )

    # الحلقة 3
    elif text == "S3E3":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=37
        )

    # الحلقة 4
    elif text == "S3E4":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=38
        )

    # الحلقة 5
    elif text == "S3E5":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=39
        )

    # الحلقة 6
    elif text == "S3E6":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=40
        )

    # الحلقة 7
    elif text == "S3E7":
        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=41
        )

    # الحلقة 8
    elif text == "S3E8":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=42
        )

    # الحلقة 9
    elif text == "S3E9":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=43
        )

    # الحلقة 10
    elif text == "S3E10":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=44
        )


    # الموسم الرابع
    elif text == "🎬 الموسم الرابع":

        await update.message.reply_text(
            "اختر الحلقة 👇",
            reply_markup=season4_menu()
        )

    # رجوع
    elif text == "🔙 رجوع":

        await update.message.reply_text(
            "رجعنا للقائمة الرئيسية 👇",
            reply_markup=main_menu()
        )

    # الحلقة 1
    elif text == "S4E1":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=45
        )

    # الحلقة 2
    elif text == "S4E2":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=46
        )

    # الحلقة 3
    elif text == "S4E3":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=47
        )

    # الحلقة 4
    elif text == "S4E4":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=48
        )

    # الحلقة 5
    elif text == "S4E5":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=49
        )

    # الحلقة 6
    elif text == "S4E6":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=50
        )

    # الحلقة 7
    elif text == "S4E7":
        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=51
        )

    # الحلقة 8
    elif text == "S4E8":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=52
        )

    # الحلقة 9
    elif text == "S4E9":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=53
        )

    # الحلقة 10
    elif text == "S4E10":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=54
        )



    # الموسم الخامس
    elif text == "🎬 الموسم الخامس":

        await update.message.reply_text(
            "اختر الحلقة 👇",
            reply_markup=season5_menu()
        )

    # رجوع
    elif text == "🔙 رجوع":

        await update.message.reply_text(
            "رجعنا للقائمة الرئيسية 👇",
            reply_markup=main_menu()
        )

    # الحلقة 1
    elif text == "S5E1":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=55
        )

    # الحلقة 2
    elif text == "S5E2":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=56
        )

    # الحلقة 3
    elif text == "S5E3":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=57
        )

    # الحلقة 4
    elif text == "S5E4":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=58
        )

    # الحلقة 5
    elif text == "S5E5":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=59
        )

    # الحلقة 6
    elif text == "S5E6":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=60
        )

    # الحلقة 7
    elif text == "S5E7":
        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=61
        )

    # الحلقة 8
    elif text == "S5E8":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=62
        )

    # الحلقة 9
    elif text == "S5E9":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=63
        )

    # الحلقة 10
    elif text == "S5E10":

        await context.bot.copy_message(
            chat_id=update.message.chat_id,
            from_chat_id=CHANNEL_ID_2,
            message_id=64
        )

    
