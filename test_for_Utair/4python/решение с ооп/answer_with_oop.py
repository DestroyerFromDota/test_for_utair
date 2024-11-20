import json

class Analiz:
    __missing_users = []
    __only_owner = []

    @staticmethod
    def __get_all_ids():
        with open('families.json', 'r') as users_file:
            users_data = json.load(users_file)
            for family in users_data:
                # Получаем участников
                participants = family.get('participants', [])
                for participant in participants:
                    yield participant.get('participant')
                # Получаем _id
                yield family.get('_id')

    @staticmethod
    def __do_missing_users():
        with open('users.json', 'r') as users_file:
            content = users_file.read()
            existing_users = set(content.splitlines())  # Сохраняем существующих пользователей в set для быстрого поиска

        for user_id in Analiz.__get_all_ids():
            if user_id not in existing_users:
                Analiz.__missing_users.append(user_id)

        with open('missing_users.json', 'w') as file:
            json.dump(Analiz.__missing_users, file)

    @staticmethod
    def __get_participants_and_check_empty():
        with open('families.json', 'r') as users_file:
            users_data = json.load(users_file)
            for family in users_data:
                if not family.get('participants'):  # Проверяем на пустоту
                    yield family

    @staticmethod
    def __do_only_owner():
        for empty_family in Analiz.__get_participants_and_check_empty():
            Analiz.__only_owner.append(empty_family.get('_id'))

        with open('only_owner.json', 'w') as file:
            json.dump(Analiz.__only_owner, file)

    @staticmethod
    def call_func():
        Analiz.__do_only_owner()
        Analiz.__do_missing_users()

# Вызов метода для выполнения анализа
Analiz.call_func()

