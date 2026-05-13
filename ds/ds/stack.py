#/usr/bin/env python3

"""
Demonstrating a Test Driven Deelopment or TDD
"""
#pylint: disable=unnecessary-pass, too-few-public-methods

class Stack:
    """A stack class."""
    def __init__(self):
        """Initialisation."""
        self._storage = []
    def __len__(self):
        """The length function."""
        return len(self._storage)
    def push(self, item):
        """Push into stack."""
        self._storage.append(item)
    def pop(self):
        """Pop method."""
        try:
            return self._storage.pop()
        except IndexError:
            return None
    def is_even(self, value):
        """Is even method."""
        if value in self._storage:
            return value % 2 == 0
        return None
