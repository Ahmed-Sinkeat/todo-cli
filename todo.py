import json, sys, os

FILE = os.environ.get("TODO_FILE", "tasks.json")


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)


def save(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add(text):
    tasks = load()
    tasks.append({"text": text, "done": False})
    save(tasks)


def main(argv):
    if len(argv) >= 3 and argv[1] == "add":
        add(" ".join(argv[2:]))
    else:
        print("usage: todo.py add <text>")


if __name__ == "__main__":
    main(sys.argv)
