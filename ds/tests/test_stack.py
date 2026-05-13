#/usr/bin/env python3

import pytest
from ds.stack import Stack

## create ficxtures to avoid duplication s = Stack() in ever test function
#@pytest.fixture
#def stack():
#    """Applying fixture to avoind duplicate s = Stack(). stack is ow the instance of our class."""
#    return Stack()


# testing the constructor which is the name of the class: Stack
def test_constructor():
    """Testing the constructor."""
    s = Stack()
    assert isinstance(s, Stack)
    assert s.__class__.__name__ == "Stack"
    assert len(s) == 0

def test_push(stack):
    """Push item into stack"""
    stack.push(3)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2

def test_pop(stack):
    stack.push("hello")
    stack.push("world")
    assert stack.pop() == "world"
    assert stack.pop() == "hello"
    assert stack.pop() is None

@pytest.mark.parametrize("even_value, expected", [
    (2, True),
    (3, False),
    (4, True),
    (5, False)
])
def test_is_even(stack, even_value, expected):
    stack.push(even_value)
    assert stack.is_even(even_value) == expected