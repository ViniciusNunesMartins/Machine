from .State import State


class Transition(object):
    def __init__(self, alphabet: set, destination: State, callback = None, direction: str = 'R', replace = None):
        self.alphabet = alphabet
        self.destination = destination
        self.callback = callback
        direction = direction.upper()
        if direction != 'R':
            direction = 'L'
        self.direction = direction
        self.replace = replace

    def __str__(self):
        return str(self.alphabet) + " -> " + self.destination.name