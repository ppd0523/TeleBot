from Logger import logger
import telegram
from telegram.ext import Updater, CommandHandler
import sys

logger.debug(f'Telegram-bot version-{telegram.__version__}')

class TelegramBot:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kwargs):
        cls.__instance = cls(*args, **kwargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def __init__(self):
        self._name = 'Junsik'
        self._chat_id = None
        self._channel_id = None
        self._core = None
        self._updater = None
        self._token = None
        logger.info('Bot create!')

    def hello(self):
        import time
        sec = 180
        while sec >= 0:
            logger.info('Waiting to get chat_id...')
            updates = self._core.getUpdates()
            if updates:
                message = updates[-1].message
                logger.info(f'Get user msg :{message.text}')
                id = message.chat.id
                self.setChatID(id)
                break
            time.sleep(5)
            sec = sec - 5
        logger.info('Not arrived user msg. CANNOT set chat_id')
        sys.exit(0)



    def setToken(self, token):
        self._token = token
        self._core = telegram.Bot(token=token)
        self._updater = Updater(token, use_context=True)
        logger.debug(f'Set token: {token}')


    def name(self):
        return self._name

    def setName(self, name):
        logger.debug(f'Set name: {name}')
        self._name = name

    def chat_id(self):
        return self._chat_id

    def setChatID(self, id):
        self._chat_id = id
        logger.debug(f'Set chat_id: {id}')

    def setChannelID(self, channel_id):
        self._channel_id = channel_id
        logger.debug(f'Set channel_id: {channel_id}')


    def sendTo(self, id, text, *args, **kwargs):
        logger.info(f'Send To \'{id}\', msg:\'{text}\'')
        if id:
            return self._core.sendMessage(chat_id=id, text=text)
        else:
            raise Exception(f"Send fail. (Invailed chat_id: '{id}')")


    def send(self, text, *args, **kwargs):
        return self.sendTo(self._chat_id, text, *args, **kwargs)


    def broadcast(self, text, *args, **kwargs):
        return self.sendTo(self._channel_id, text, *args, **kwargs)


    def start(self):
        logger.info(f'{self._name} Start!')
        self._updater.start_polling()
        self._updater.idle()

    def stop(self):
        logger.info(f'{self._name} Stop!')
        self._updater.dispatcher.stop()
        self._updater.job_queue.stop()
        self._updater.stop()

    def add_handler(self, cmd, func):
        logger.debug(f'Set CMD "/{cmd}" - Function <{func.__name__}>')
        self._updater.dispatcher.add_handler(CommandHandler(cmd,func))

BOT = TelegramBot.instance()
INTRO_MESSAGE = f"Hello. This is {BOT.name()}. I announce information something now."