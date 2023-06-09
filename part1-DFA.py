class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state

    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function):
            self.current_state = None
        else:
            self.current_state = self.transition_function[(self.current_state, input_value)]

    def in_accept_state(self):
        return self.current_state in self.accept_states

    def go_to_initial_state(self):
        self.current_state = self.start_state

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            if self.current_state is None:
                return False
        return self.in_accept_state()

states = {0, 1, 2}
alphabet = {'a', 'b'}

tf = dict()
tf[(0, 'a')] = 0
tf[(0, 'b')] = 1
tf[(1, 'a')] = 2
tf[(1, 'b')] = 0
tf[(2, 'a')] = 1
tf[(2, 'b')] = 2

start_state = 0
accept_states = {0}

d = DFA(states, alphabet, tf, start_state, accept_states)

while True:
    test_input = input("Appuyez sur la touche q pour quitter le programme. \nOu Saisissez une chaîne de a et de b\ninput:")
    input_list = list(test_input)
    if input_list[0] == 'q' or input_list[0]=='Q':
        print("\nA bientot!")
        break
    if d.run_with_input_list(input_list):
        print("\nLa chaine que vous avez entree a ete acceptee.\n\n")
    else:
        print("\nLa chaine que vous avez entree n'a pas ete acceptee.\n\n")