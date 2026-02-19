from state import AccountState
from lifecycle import advance_phase


def run():
    state = AccountState()
    print("Initial:", state)

    state = advance_phase(state)
    print("After transition:", state)


if __name__ == "__main__":
    run()
