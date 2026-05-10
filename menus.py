from telegram import KeyboardButton, ReplyKeyboardMarkup


# ---------------- القائمة الرئيسية ----------------
def main_menu():

    keyboard = [
        [KeyboardButton("🎬 الموسم الاول")],
        [KeyboardButton("🎬 الموسم الثاني")],
        [KeyboardButton("🎬 الموسم الثالث")],
        [KeyboardButton("🎬 الموسم الرابع")],
        [KeyboardButton("🎬 الموسم الخامس")]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

# ---------------- حلقات الموسم الاول ----------------
def season1_menu():

    keyboard = [
        [KeyboardButton("S1E1"), KeyboardButton("S1E2")],
        [KeyboardButton("S1E3"), KeyboardButton("S1E4")],
        [KeyboardButton("S1E5"), KeyboardButton("S1E6")],
        [KeyboardButton("S1E7"), KeyboardButton("S1E8")],
        [KeyboardButton("🔙 رجوع")]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

# ---------------- حلقات الموسم الثاني ----------------
def season2_menu():

    keyboard = [
        [KeyboardButton("S2E1"), KeyboardButton("S2E2")],
        [KeyboardButton("S2E3"), KeyboardButton("S2E4")],
        [KeyboardButton("S2E5"), KeyboardButton("S2E6")],
        [KeyboardButton("S2E7"), KeyboardButton("S2E8")],
        [KeyboardButton("🔙 رجوع")]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

# ---------------- حلقات الموسم الثالث ----------------
def season3_menu():

    keyboard = [
        [KeyboardButton("S3E1"), KeyboardButton("S3E2")],
        [KeyboardButton("S3E3"), KeyboardButton("S3E4")],
        [KeyboardButton("S3E5"), KeyboardButton("S3E6")],
        [KeyboardButton("S3E7"), KeyboardButton("S3E8")],
        [KeyboardButton("S3E9"), KeyboardButton("S3E10")],
        [KeyboardButton("🔙 رجوع")]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

# ---------------- حلقات الموسم الرابع ----------------
def season4_menu():

    keyboard = [
        [KeyboardButton("S4E1"), KeyboardButton("S4E2")],
        [KeyboardButton("S4E3"), KeyboardButton("S4E4")],
        [KeyboardButton("S4E5"), KeyboardButton("S4E6")],
        [KeyboardButton("S4E7"), KeyboardButton("S4E8")],
        [KeyboardButton("S4E9"), KeyboardButton("S4E10")],
        [KeyboardButton("🔙 رجوع")]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

# ---------------- حلقات الموسم الخامس ----------------
def season5_menu():

    keyboard = [
        [KeyboardButton("S5E1"), KeyboardButton("S5E2")],
        [KeyboardButton("S5E3"), KeyboardButton("S5E4")],
        [KeyboardButton("S5E5"), KeyboardButton("S5E6")],
        [KeyboardButton("S5E7"), KeyboardButton("S5E8")],
        [KeyboardButton("S5E9"), KeyboardButton("S5E10")],
        [KeyboardButton("🔙 رجوع")]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
