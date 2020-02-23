from ChatBot import BOT, INTRO_MESSAGE
from Logger import logger
import sys
from Util import *

# 자원 폴더 확인
if not os.path.exists('resource'):
    os.mkdir('resource')

# token 획득, 없으면 종료
TOKEN = load('resource/token.txt')
if (not TOKEN) or (TOKEN == ''):
    logger.info('No Token. Program exit.')
    sys.exit(0)
else:
    # token 유효성 확인
    try:
        BOT.setToken(TOKEN)
    except Exception as e:
        logger.info(f'Error: {e}')
        sys.exit(0)

# name 획득, 없으면 기본 이름
NAME = load('resource/name.txt')
if (not NAME) or (NAME == ''):
    logger.info('No name. Set default name')
    BOT.setName('준식')
else:
    BOT.setName(NAME)

# user_chat_id 획득, 없으면 메세지를 받아 획득
CHAT_ID = load('resource/user_chat_id.txt')
if CHAT_ID:
    BOT.setChatID(CHAT_ID)
else:
    logger.info('No resource/user_chat_id.txt')
    BOT.hello()
    id = BOT.chat_id()
    save('resource/user_chat_id.txt', id)

# channel_id 획득, 없으면 무시
CHANNEL_ID = load('resource/channel_id.txt')
if (CHANNEL_ID is not None) or (not CHANNEL_ID == ''):
    BOT.setChannelID(CHANNEL_ID)
    # channel_id 유효한지 확인
    try:
        BOT.sendTo(CHANNEL_ID, INTRO_MESSAGE)
    except Exception as e:
        logger.info(f'Invaild Channel id: {e}')
        file = 'resource/channel_id.txt'
        if os.path.isfile(file):
            logger.info(f'remove file: \'{file}\'')
            os.remove(file)
else:
    logger.info(f'No channel id')


from CommandFunction import *
BOT.add_handler('help', help)
BOT.add_handler('h', help)
BOT.add_handler('link', linkChannel)
BOT.add_handler('unlink', unlinkChannel)
BOT.add_handler('rename', setName)
BOT.add_handler('broadcast', broadcast)
BOT.add_handler('b', broadcast)
BOT.add_handler('echo', echo)

BOT.start()