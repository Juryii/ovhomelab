import argparse
import json

def remove_pk_from_json(input_file):
    # Открываем файл JSON с дампом данных
    with open(input_file, 'r', encoding="utf-8") as file:
        data = json.load(file)

    # Удаляем поле 'pk' из каждого объекта в списке
    for obj in data:
        if 'pk' in obj:
            del obj['pk']

    # Записываем измененные данные обратно в файл
    output_file = input_file.replace('.json', '_without_pk.json')
    with open(output_file, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f'File "{input_file}" processed. Result saved in "{output_file}".')

if __name__ == '__main__':
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Remove "pk" field from a JSON dump file')
    parser.add_argument('input_file', help='Input JSON file name')
    args = parser.parse_args()

    remove_pk_from_json(args.input_file)
