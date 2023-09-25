import os
import json
import csv
import pickle

def get_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total


def folder(way):
    result = []
    for dirpath, dirnames, filenames in os.walk(way):
        for name_file in filenames:
            full_path = os.path.join(dirpath, way)
            result.append({'parent_directory': dirpath,
                        'is_file': True,
                        'name': name_file,
                        'size_in_bytes': os.path.getsize(full_path)})

        for name in dirnames:
            full_path = os.path.join(dirpath, name)
            result.append({'parent_directory': dirpath,
                        'is_file': False,
                        'name': name_file,
                        'size_in_bytes': get_size(full_path)})
    
    with open('output.json', 'w') as file_json:
        json.dump(result, file_json)

    with open('output.csv', 'w') as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=result[0].keys())
        writer.writeheader()
        writer.writerows(result)

    with open('output.pickle', 'wb') as file_pickle:
        pickle.dump(result, file_pickle)
folder(input('введите путь к файлам: '))