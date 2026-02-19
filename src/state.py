class AccountState:
    def __init__(self, phase="handoff", risk_score=0):
        self.phase = phase
        self.risk_score = risk_score

    def __repr__(self):
        return f"AccountState(phase={self.phase}, risk_score={self.risk_score})"
