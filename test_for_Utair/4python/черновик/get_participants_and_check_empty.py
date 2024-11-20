import json

def get_participants_and_check_empty():
    with open('families.json', 'r') as users_file:
        #принимат строку с данными в формате json, функция load() принимает файловый объект и возвращает его десериализованное содержимое.
        users_data = json.load(users_file)
        # получаем отдельные json объекты для последжующей обработки, каждая i является отдельным json-объектом
        for i in users_data:
            # проверяем participants на пустоту
            if len(i['participants']) == 0:
                # Возвращаем объект с пустыми участниками
                yield i

# выводим на экран id полученных в get_participants_and_check_empty
for empty_family in get_participants_and_check_empty():
    print(empty_family['_id'])
