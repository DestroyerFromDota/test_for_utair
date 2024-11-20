import json

def get_all_id():
    with open('families.json', 'r') as users_file:
        # принимат строку с данными в формате json, функция load() принимает файловый объект и возвращает его десериализованное содержимое.
        users_data = json.load(users_file)
        # получаем отдельные json объекты для последжующей обработки, каждая i является отдельным json-объектом
        for i in users_data:
            # получаем вложенные объекты в ключ participants
            for j in (i['participants']):
                # получаем participant'ов
                yield j['participant']
            # Получаем _id
            yield i['_id']


# проверяем на вхождение всех строк полученных из get_all_id на наличие в users.json
for id in get_all_id():
    with open('users.json', 'r') as users:
        # читаем файл для последующей проверки вхождения строки в подстроку
        content = users.read()
        # при отсутствии совпадения выводим эти строки
        if id not in content:
            print(id)

