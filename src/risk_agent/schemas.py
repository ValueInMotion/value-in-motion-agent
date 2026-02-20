
from pydantic import BaseModel
from typing import Literal

RiskLevel = Literal["LOW", "MEDIUM", "HIGH"]

class AccountLifecycle(BaseModel):
    account: str
    icp_score: int
    deal_complexity: int
    usage_30d: int
    workflow_integrated: bool
    roi_score: int
    exec_engagement: bool