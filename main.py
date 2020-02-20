from Automaton import Machine, State


class Turing(Machine):
    def setAcceptanceSate(self, state: str):
        self.acceptance_state = self.getState(state)

    def setRejectionState(self, state: str):
        self.rejection_state = self.getState(state)

    def check(self, word, index = 0, state: State = None) -> bool:
        if not state:
            state = self.start_state
        if state is self.acceptance_state:
            return True
        if state is self.rejection_state:
            return False
        print(state.name + ':\t' + word[0:index] + "[" + word[index] + "]" + word[index + 1:], end=' -> ')
        for t in state.transitions:
            if word[index] in t.alphabet:
                print(t.destination)
                if t.direction == 'R':
                    return self.check(word, index + 1, t.destination)
                else:
                    return self.check(word, index - 1, t.destination)
        if state.callback:
            print("??")
            state.callback(word[index], state)
            return self.check(word, index, state)
        raise InterruptedError

m = Turing()

m.setState('q0', False, callback=lambda symbol, state: state.setTransition(set(symbol), m.rejection_state))
m.setState('q1', False, callback=lambda symbol, state: state.setTransition(set(symbol), m.rejection_state))
m.setState('q2', False, callback=lambda symbol, state: state.setTransition(set(symbol), m.rejection_state))
m.setState('Acceptance', final = True)
m.setState('Rejection')

m.setStartState('q0')
m.setAcceptanceSate('Acceptance')
m.setRejectionState('Rejection')

m.setTransition('q0', {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}, 'q0')
m.setTransition('q0', {'+', '-', '*', '/'}, 'q1')
m.setTransition('q1', {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}, 'q2')
m.setTransition('q2', {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}, 'q2')
m.setTransition('q2', {'=', '>=', '<=', '>', '<', '~=', '!='}, 'Acceptance')

print(m.check('10+10='))
print(m.check('10+10b='))