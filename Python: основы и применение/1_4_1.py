n = int(input())
# scopes = {'name':{parent:val,child:val}}
scopes = {'None':{'parent':None, 
                  'variables':set()},
         'global':{'parent' : None,
                   'variables':set()}
         }
scopes['None']['variables'].add('global')
def create(namespace,parent):
    scopes[parent]['variables'].add(namespace)
    scopes.update({namespace:{'parent':parent,'variables':set()}})

def add(namespace,variable):
    scopes[namespace]['variables'].add(variable)

def get(namespace,variable):
    if namespace == None:
        print("None")
        return
    if namespace not in scopes:
        print("None")
        return
    if variable in scopes[namespace]['variables']:
        print(namespace)
        return
    if scopes[namespace]['parent'] != "None":
        get(scopes[namespace]['parent'],variable)
        return
    else:
        print("None")
while n:
    cmd, namesp, var = input().split()
    if cmd=="create":
        create(namesp,var)
    elif cmd=="add":
        add(namesp,var)
    elif cmd=="get":
        get(namesp,var)
    n-=1