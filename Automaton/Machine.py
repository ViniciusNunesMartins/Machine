from .State import State


class Machine (object):
    def __init__(self):
        self.states = list()
        self.start_state = None

    def setState(self, name, final = False, callback = None):
        if not self.getState(name):
            self.states.append(State(name, final, callback))

    def getState(self, name):
        for s in self.states:
            if s.name == name:
                return s
        return None
    
    def setStartState(self, state):
        if type(state) == type(""):
            state = self.getState(state)
        if state:
            self.start_state = state
        exit
    def setFinalState(self, state):
        if type(state) == type(""):
            state = self.getState(state)
        if state is None:
            exit()
        state.final = True

    def setTransition(self, source,  alphabet, destination, callback = None, direction = 'R', replace = None):
        if type(source) == type(""):
            source = self.getState(source)
        if type(destination) == type(""):
            destination = self.getState(destination)
        if source and destination:
            source.setTransition(alphabet, destination, callback, direction, replace)

    def check(self, word, state = None) -> bool:
        if not state:
            state = self.start_state
        raise NotImplementedError