# main.py
def greet(name, excited=False):
    if excited:
        return f"Hello, {name}"
    return f"Hi, {name}!"

if __name__ == "__main__":
    print(greet("World"))

