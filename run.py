"""Run this file to start bot"""
from bot import client
from database.create import create_tables
from client_handlers import active_handlers


def add_handlers() -> None:
    for handler in active_handlers:
        client.add_handler(handler().de_pyrogram_handler)
    print("Все обработчики успешно добавлены!")


def run_bot() -> None:
    add_handlers()
    create_tables()
    try:
        client.run()
    except Exception as e:
        print(f"Невозможно запустить клиента! {e}")


if __name__ == "__main__":
    run_bot()
