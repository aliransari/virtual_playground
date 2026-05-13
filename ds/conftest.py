#!/usr/bin/env python3

import pytest
from ds.stack import Stack

# create ficxtures to avoid duplication s = Stack() in ever test function
@pytest.fixture
def stack():
    """Applying fixture to avoind duplicate s = Stack(). stack is ow the instance of our class."""
    return Stack()
