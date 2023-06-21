exceptions = {}
thrown_exceptions = []
unused_exceptions = []


def add_exception(exception_name, exception_dict):
  if exception_name not in exception_dict:
    exception_dict[exception_name] = []


def define(parent, child, dictionary):
  path = [child]
  while path:
    current = path.pop()
    if current == parent:
      return True
    if current not in dictionary:
      continue
    path.extend(dictionary[current])
  return False


n = int(input())
for _ in range(n):
  class_name, *parent_classes = input().split()
  add_exception(class_name, exceptions)
  exceptions[class_name].extend(parent_classes)

n = int(input())
for _ in range(n):
  throwing = input()
  for thrown_exception in thrown_exceptions:
    if define(thrown_exception, throwing, exceptions):
      unused_exceptions.append(throwing)
      break
  thrown_exceptions.append(throwing)

for unused_exception in unused_exceptions:
  print(unused_exception)