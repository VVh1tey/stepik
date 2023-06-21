import json

def define(parent: str, child: str, dictionary: dict) -> str:
    path = [child]
    while path:
        current = path.pop()
        if current == parent:
            return 'Yes'
        if current not in dictionary:
            continue
        path.extend(dictionary[current])
    return 'No'

def count_descendants(inp:dict) -> dict:
    dictionary = {}
    for item in inp:
        dictionary[item["name"]] = item["parents"]

    result = {}
    for class_name in dictionary:
        count = 0
        for child in dictionary:
            if define(class_name, child, dictionary) == 'Yes':
                count += 1
        result[class_name] = count

    return result

inp = json.loads(input())

descendants = count_descendants(inp)

for class_name, count in sorted(descendants.items()):
    print(f"{class_name} : {count}")