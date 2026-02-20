
from src.risk_agent.schemas import AccountLifecycle

def compute_risk(a: AccountLifecycle):
    reasons = []

    # BEGINNING — Sales handoff / PSP
    structural = 0
    if a.icp_score < 50:
        structural += 1
        reasons.append("Low ICP fit")
    if a.deal_complexity > 70:
        structural += 1
        reasons.append("High deal complexity")

    # MIDDLE — Onboarding / workflow integration
    adoption = 0
    if a.usage_30d < 30:
        adoption += 1
        reasons.append("Low usage (30d)")
    if not a.workflow_integrated:
        adoption += 1
        reasons.append("No workflow integration")

    # END — Executive value / renewal readiness
    renewal = 0
    if a.roi_score < 50:
        renewal += 1
        reasons.append("Low ROI / value perception")
    if not a.exec_engagement:
        renewal += 1
        reasons.append("No executive engagement")

    total = structural + adoption + renewal

    if total >= 4:
        risk_level = "HIGH"
        next_action = "Recovery: exec alignment + value proof plan (14 days)"
    elif total >= 2:
        risk_level = "MEDIUM"
        next_action = "Stabilize: integrate 1 workflow + adoption targets"
    else:
        risk_level = "LOW"
        next_action = "Expand: identify next use case + exec value review"

    return {
        "account": a.account,
        "risk_level": risk_level,
        "reasons": reasons if reasons else ["No risk signals detected"],
        "breakdown": {"structural": structural, "adoption": adoption, "renewal": renewal},
        "next_action": next_action,
    }