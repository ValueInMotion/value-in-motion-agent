def advance_phase(state):
    phases = [
        "handoff",
        "diagnostic",
        "success_plan",
        "velocity",
        "renewal"
    ]

    current_index = phases.index(state.phase)

    if current_index < len(phases) - 1:
        state.phase = phases[current_index + 1]

    return state
