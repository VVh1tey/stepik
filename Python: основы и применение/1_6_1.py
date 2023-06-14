classes = dict()

def add(string: str, dictionary: dict) -> None:
    class_description = string.split()
    class_name = class_description[0]
    class_parents = class_description[2:]
    if class_name not in dictionary:
        dictionary[class_name] = []
    dictionary[class_name].extend(class_parents)
    for parent in class_parents:
        if parent not in classes:
            classes[parent] = []

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

n = int(input())
while n:
    add(input(),classes)
    n-=1
n = int(input())
while n:
    c1,c2 = input().split()
    print(define(c1,c2,classes))
    n-=1