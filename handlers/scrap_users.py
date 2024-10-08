from config import INST_USERNAME, INST_PASSWORD, TARGET_USERNAME, FOLLOWERS_COUNT, DB_NAME, TABLE_NAME

from db import Database

from utils import insta_connect, get_users_info


def parse_users():
    """Парсим пользователей."""
    Loader = insta_connect(INST_USERNAME, INST_PASSWORD)
    users_data = get_users_info(Loader, TARGET_USERNAME, FOLLOWERS_COUNT)
    db_layer = Database(DB_NAME)
    db_layer.connect()
    db_layer.create_table(TABLE_NAME)
    db_layer.insert_data(TABLE_NAME, users_data)
    db_layer.disconnect()
