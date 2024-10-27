import sys
# add repl loop
# add add task command
# add list task command
# add update task command
# add delete task command

def add(name: list[str]) -> None:
    print(name[1])

def main() -> None:
    for name in commands:
        if name == sys.argv[1]:
            commands[name](sys.argv[1:])
commands = {
    "add": add
}

main()