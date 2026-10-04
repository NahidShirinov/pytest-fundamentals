import os


def greet(name):
    print(f"Salam, {name}!")


def save_lines(path, lines):
    with open(path, "w") as f:
        f.write("\n".join(lines))


def read_lines(path):
    with open(path) as f:
        return f.read().splitlines()


def get_env_mode():
    return os.getenv("APP_MODE", "dev")
