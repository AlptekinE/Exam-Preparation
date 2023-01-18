from typing import List, Tuple

from utils.database_connection import DatabaseConnection

Topic = Tuple[int, str, str, int]


def create_topics_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS topics (id integer primary key, name text, lecture text, read integer default 0)')


def get_all_topics() -> List[Topic]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM topics')
        topics = cursor.fetchall()
    return topics


def insert_topic(name: str, lecture: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO topics (name, lecture) VALUES (?, ?)', (name, lecture))


def confident_level(name: str, percentage: int) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE topics SET read=? WHERE name=?', (percentage,name))


def delete_topic(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM topics WHERE name=?', (name,))