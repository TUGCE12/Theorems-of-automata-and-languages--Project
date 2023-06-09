class TuringMachine:
    def __init__(self,
                 tape = "",
                 blank_symbol = " ",
                 initial_state = 0,
                 final_states = 0,
                 transition_table = None):
        self.tape = list(tape)
        self.head_position = 0
        self.blank_symbol = blank_symbol
        self.current_state = initial_state
        if transition_table == None:
            self.transition_table = {}
        else:
            self.transition_table = transition_table
        if final_states == 0:
            self.final_states = set()
        else:
            self.final_states = set(final_states)

    def get_current_symbol(self):
        return self.tape[self.head_position]

    def write_symbol(self, symbol):
        self.tape[self.head_position] = symbol

    def move_head(self, direction):
        if direction == "R":
            self.head_position += 1
            if self.head_position >= len(self.tape):
                self.tape.append(self.blank_symbol)
        elif direction == "L":
            self.head_position -= 1

    def step(self):
        state_symbol_pair = (self.current_state, self.get_current_symbol())
        if state_symbol_pair in self.transition_table:
            new_state, new_symbol, direction = self.transition_table[state_symbol_pair]
            self.current_state = new_state
            self.write_symbol(new_symbol)
            self.move_head(direction)

    def final(self):
        if self.current_state in self.final_states:
            return True
        else:
            return False


# Define the initial state, final states, and transition table for the Turing machine
initial_state = 1
final_states = {5}
# transition_table: there is really tons of step so slow
# transition_table = {
#     (1, "a"): (2, "X", "R"),
#     (2, "a"): (2, "a", "R"),
#     (2, "b"): (3, "Y", "L"),
#     (3, "a"): (3, "a", "L"),
#     (3, "X"): (1, "X", "R"),
#     (1, "Y"): (4, "Y", "R"),
#     (4, "Y"): (4, "Y", "R"),
#     (4, " "): (5, " ", "R"),
# }

transition_table = {
    (1, "a"): (2, "X", "R"),
    (2, "a"): (2, "a", "R"),
    (2, "b"): (3, "Y", "L"),
    (3, "a"): (3, "a", "L"),
    (3, "X"): (1, "X", "R"),
    (1, "Y"): (5, "Y", "R"),
    (5, "Y"): (5, "Y", "R"),
    (5, " "): (5, " ", "R"),
}
# Create an instance of the TuringMachine class
t = TuringMachine(
    tape = "ab ",
    initial_state = initial_state,
    final_states = final_states,
    transition_table = transition_table
)

# Print the initial tape
print("Entree de bande d'essai:" + ''.join(t.tape))

# Run the Turing machine until it reaches a final state
while not t.final():
    t.step()

# Print the final tape
print("Tape Finale:\n" + ''.join(t.tape))

# Check if the Turing machine accepted the input
if t.final():
    print("La chaîne d'entrée a été acceptée.")
else:
    print("La chaîne d'entrée n'a pas été acceptée.")

while True:
    test = input("\n\nAppuyez sur la touche q pour quitter le programme. \nOu Saisissez une chaîne de a et de b\ninput:")
    if test == 'q' or test == 'Q':
        print("\nA bientot!")
        break
    t = TuringMachine(
        tape=test,
        initial_state=initial_state,
        final_states=final_states,
        transition_table=transition_table
    )
    # Print the initial tape
    print("\nEntree de bande d'essai:" + ''.join(t.tape))

    # Run the Turing machine until it reaches a final state
    while not t.final():
        t.step()

    # Print the final tape
    print("Tape Finale:" + ''.join(t.tape))

    # Check if the Turing machine accepted the input
    if t.final():
        print("\nLa chaîne d'entrée a été acceptée.\n------------------\n")
    else:
        print("\nLa chaîne d'entrée n'a pas été acceptée.\n------------------\n")
