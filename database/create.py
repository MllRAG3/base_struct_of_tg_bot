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
