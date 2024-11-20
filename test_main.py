#test_main.py
from main import greet

#def test_greet():
#    assert greet("Alice") == "Hello, Alice!"
#    assert greet("Bob") == "Hello, Bob!"

def test_greet_fails():
    assert greet("Alice") == "Hello, Alice!"
