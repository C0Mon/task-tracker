import sys, json, os
from datetime import datetime

# add delete task command

def updateJson(file: dict) -> None:
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)

def getJson() -> dict:
    if os.path.exists('data.json'):
        with open('data.json', 'r') as file:
            data = json.load(file)
    else:
        data = {'tasks': []}
    return data

def add(args: list[str]) -> None:
    file = getJson()
    data = {
        'id': len(file['tasks']),
        'description': args[1],
        'status': "todo",
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    file['tasks'].append(data)
    updateJson(file)

def getTasksByStatus(file: dict, status: str) -> dict:
    newFile = { 'tasks': [] }
    for task in file['tasks']:
        if task['status'] == status:
            newFile['tasks'].append(task)
    return newFile

def listTasks(args: list[str]) -> None:
    file = getJson()
    if len(args) == 2:
        file = getTasksByStatus(file, args[1])
    for task in file['tasks']:
        print(f'{ task['id'] }    { task['description'] }\n')

def updateStatus(args: list) -> None:
    status = args[0].split('-', 1)
    update(int(args[1]), 'status', status[1])

def getTaskIndex(tasks: list[dict], id: int) -> int:
    low = 0
    high = len(tasks) - 1
    while low <= high:
        mid = (high + low) // 2
        if tasks[mid]['id'] == id:
            return mid
        elif tasks[mid]['id'] > id:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def updateDescription(args: list) -> None:
    update(int(args[1]), 'description', args[2])

def update(id: int, property: str, value: str) -> None:
    file = getJson()
    taskIndex = getTaskIndex(file['tasks'], id)
    if taskIndex == -1:
        print('Task Not Found')
    else:
        file['tasks'][taskIndex][property] = value
    updateJson(file)

def main() -> None:
    for name in commands:
        if name == sys.argv[1]:
            commands[name](sys.argv[1:])

commands = {
    'add': add,
    'list': listTasks,
    'mark-in-progress': updateStatus,
    'mark-done': updateStatus,
    'update': updateDescription
}

if __name__ == "__main__":
    main()