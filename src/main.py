from state import AccountState
from lifecycle import advance_phase

def run():
    state = AccountState()
    print("Initial:", state)

    for _ in range(3):
        state = advance_phase(state)
        print("Next:", state)

if __name__ == "__main__":
    run()
