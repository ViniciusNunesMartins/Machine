import abc
from .State import State


class Machine (object):
    def __init__(self):
        self.states = list()
        self.start_state = None

    def setState(self, name: str, final: bool = False, callback = None):
        self.states.append(State(name, final, callback))
        if self.start_state is None:
            self.setStartState(name)
    
    def getState(self, name: str) -> State:
        for s in self.states:
            if s.name == name:
                return s
        raise NameError
    

    def setStartState(self, state: str):
        if type(state) == type(""):
            state = self.getState(state)
        if state:
            self.start_state = state
        exit
    def setFinalState(self, state: str):
        if type(state) == type(""):
            state = self.getState(state)
        if state is None:
            exit()
        state.final = True

    def setTransition(self, source: str,  alphabet: set, destination: str, callback = None, direction: str = 'R', replace = None):
        if type(source) == type(""):
            source = self.getState(source)
        if type(destination) == type(""):
            destination = self.getState(destination)
        if source and destination:
            source.setTransition(alphabet, destination, callback, direction, replace)

    @abc.abstractclassmethod
    def check(self, word, state: State = None) -> bool:
        """Implement the method for checking words"""
        if not state:
            state = self.start_state
        raise NotImplementedError