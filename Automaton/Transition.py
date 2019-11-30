class Transition(object):
    def __init__(self, alphabet, destination, callback = None, direction = 'R', replace = None):
        self.alphabet = alphabet
        self.destination = destination
        self.callback = callback
        direction = direction.upper()
        if direction != 'R':
            direction = 'L'
        self.direction = direction
        self.replace = replace