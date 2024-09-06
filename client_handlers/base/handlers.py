from pyrogram.handlers.handler import Handler
from pyrogram import filters, types
from pyrogram import Client

request_type = types.Message | types.CallbackQuery  # add some types here if you need:3


class BaseHandler:
    """Базовый обработчик-исполнитель"""
    __name__ = ""
    HANDLER: Handler = Handler
    FILTER: filters.Filter | None = None

    async def func(self, client: Client, request: request_type):
        raise NotImplementedError

    @property
    def de_pyrogram_handler(self):
        return self.HANDLER(self.func, self.FILTER)
