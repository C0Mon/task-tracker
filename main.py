import sys, json, os
from datetime import datetime
# add repl loop
# add add task command
# add list task command
# add update task command
# add delete task command

def getJson() -> dict:
    if os.path.exists('data.json'):
        with open('data.json', 'r') as file:
            data = json.load(file)
    else:
        data = {'taskDetails': []}
    return data

def add(name: list[str]) -> None:
    file = getJson()
    data = {
        'id': len(file['taskDetails']),
        'description': name[1],
        'status': "todo",
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    file['taskDetails'].append(data)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)

def main() -> None:
    for name in commands:
        if name == sys.argv[1]:
            commands[name](sys.argv[1:])
commands = {
    "add": add
}

if __name__ == "__main__":
    main()