from utils import database


USER_CHOICE = """

Enter:

'a' to add a new topic
'l' to list all topics
'c' to rate the level of confidence in the topic
'd' to delete a topic
'q' to quit

Your choice: """


def menu():
    database.create_topics_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_topic()
        elif user_input == 'l':
            list_topics()
        elif user_input == 'c':
            topic_confidence()
        elif user_input == 'd':
            prompt_delete_topic()

        user_input = input(USER_CHOICE)


def prompt_add_topic():
    topic = input('Enter the new topic name: ')
    lecture = input('Enter the lecture name of the topic: ')

    database.insert_topic(topic, lecture)


def list_topics():
    for topic in database.get_all_topics():
        done = 'YES!!!' if topic[3] == 100 else topic[3]
        print(f'{topic[1]} on {topic[2]} — Confident: {done}')


def topic_confidence():
    name = input('Enter the name of the topic you want to rate: ')
    percentage = input('How confident you are in this topic: ')
    database.confident_level(name, percentage)


def prompt_delete_topic():
    name = input('Enter the name of the topic you wish to delete: ')

    database.delete_topic(name)


menu()



