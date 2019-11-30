from .Transition import Transition


class State(object):
    def __init__(self, name, final = False, callback = None):
        self.name = name
        self.final = final
        self.callback = callable
        self.transitions = list()

    def setTransition(self, alphabet, destination, callback = None, direction = 'R', replace = None):
        self.transitions.append(Transition(alphabet, destination, callback, direction, replace))