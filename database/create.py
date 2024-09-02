from pyrogram.types import Message, User, Chat

from database.models import active_models
from database.db_init import db


def create_tables() -> None:
    """Database models to tables"""
    if not active_models:
        print("Нет активных моделей баз данных.")
        return
    with db:
        db.create_tables(active_models)
    print("Модели базы данных успешно созданы!")


class GetOrCreate:
    def __init__(
            self,
            *,
            request: Message | None = None,
            chat: Chat | None = None,
            user: User | None = None
    ) -> None:
        if not (request or (chat and user)):
            raise Exception("Не хватает аргументов! (Вызвано классом database/create/GetOrCreate)")
        self.user: User = request.from_user if user is None else user
        self.chat: Chat = request.chat if chat is None else chat

