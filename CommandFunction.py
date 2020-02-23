from ChatBot import BOT, INTRO_MESSAGE
from Logger import logger
import os

def help(update, context):
    text = f"Command list\n" \
           f"/help : Show command list\n" \
           f"/link <CHANNEL>: {BOT.name()} is linked to the channel <CHANNEL>\n" \
           f" ex)\n" \
           f"'/link junsik_chan' means that Bot is linked 't.me/junsik_chan'.\n" \
           f"The channel 'junsik_chan' should be PUBLIC. And {BOT.name()} is a MEMBER of it\n" \
           f"/unlink : {BOT.name()} is unlinked\n" \
           f"/rename <NAME>: Rename {BOT.name()} to <NAME>\n" \
           f"/broadcast <TEXT> : {BOT.name()} broadcasts <TEXT> on the channel"
    update.message.reply_text(text)


def setName(update, context):
    text = update.message.text
    name = text.replace("/rename ", "")
    BOT.setName(name)
    with open('resource/name.txt', 'w') as file:
        file.write(str(name))
    update.message.reply_text(f"Set bot name '{BOT.name()}'")


def linkChannel(update, context):
    text = update.message.text
    link = text.split()[-1]

    try:
        data = BOT.sendTo(f'@{link}', INTRO_MESSAGE)
        channel_id = data['chat']['id']
        if channel_id:
            BOT.setChannelID(channel_id)
            with open('resource/channel_id.txt', 'w') as file:
                file.write(str(channel_id))
        update.message.reply_text(f"{BOT.name()} is linked 't.me/{link}'")
    except Exception as e:
        errorMessage = f"CANNOT link 't.me/{link}'. ({e})\n" \
                       f"1. Is the channel PUBLIC?\n" \
                       f"2. Is the channel NAME CORRECT?\n" \
                       f"3. Is {BOT.name()} a MEMBER of the channel?"
        logger.info(errorMessage)
        update.message.reply_text(errorMessage)


def unlinkChannel(update, context):
    file = 'resource/channel_id.txt'
    resultMessage = f"{BOT.name()} unlinked the channel"

    if os.path.isfile(file):
        os.remove(file)
        BOT.setChannelID(None)
        logger.info(resultMessage)
        update.message.reply_text(resultMessage)
    else:
        update.message.reply_text('No link')


def broadcast(update, context):
    text = update.message.text
    index = text.find(" ")
    data = text[index:]
    try:
        BOT.broadcast(data)
        update.message.reply_text(f"Broadcast is successful")
    except Exception as e:
        logger.info(f"{e}")
        try:
            BOT.send(f"Broadcast failed. Channel unlinked")
        except Exception as e:
            logger.info(f"{e}")


def echo(update, context):
    text = update.message.text
    data = text.replace("/echo ", "")
    try:
        BOT.send(data)
    except Exception as e:
        logger.info(f"{e}")


from telegram import InlineKeyboardButton, InlineKeyboardMarkup
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i+n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.insert(footer_buttons)
    return menu


def get_command(update, context):
    print("get")
    showList = [InlineKeyboardButton("On", callback_data="on")]
    a = build_menu(showList, 1)
    showMarkup = InlineKeyboardMarkup(a)
    update.message.reply_text("원하는 값을 선택하세요", reply_markup=showMarkup)


def get_command2(update, context):
    print("get2")
    showList = [InlineKeyboardButton("Ona", callback_data="ona")]
    showMarkup = InlineKeyboardMarkup([showList])
    update.message.reply_text("원하는 값을 선택하세요up=showMarkup)", reply_markup=showMarkup)