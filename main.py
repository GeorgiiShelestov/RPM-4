import os

dictionary = {}


def input_path():
    path_to_directory = str(input('Введите путь к папке: '))
    return path_to_directory


def create_dict(path):
    for filename in os.listdir(path):
        try:
            path_to_file = os.path.join(path, filename)
            if os.path.isdir(path_to_file):
                create_dict(path_to_file)
            else:
                dictionary[path_to_file] = os.path.getsize(path_to_file)
        except PermissionError:  # Ошибка доступа
            pass
    return dictionary


def analyze_dict(dictionary):
    names = []  # Список имён
    weight = []  # Список веса файлов
    for k in dictionary.keys():
        names.append(os.path.basename(k))
    for v in dictionary.values():
        weight.append(v)
    doubles = {}
    for i in range(len(names)):
        count = 0
        for j in range(len(names)):
            if names[i] == names[j]:  # Сравниваем имена файлов
                if weight[i] == weight[j]:  # Сравниваем вес файлов, если всё совпало - дубликат
                    count += 1
                doubles[names[i]] = count
    return doubles


def duplicate_files(doubles):
     for k, v in dict.items(doubles):
        if v > 1:
            print(k + ': ' + str(v))

if __name__ == '__main__':
    duplicate_files(analyze_dict(create_dict(input_path())))