from typing import List
from .policy_flow import PolicyFlow
from .clinician import Clinician
from .action import Action
from utils.action_executor import ActionExecutor


class PolicyEngine:
    def __init__(self, policy_flows: List[PolicyFlow], clinicians: List[Clinician]):
        self.policy_flows = policy_flows
        self.clinicians = clinicians

    def __str__(self):
        return f"PolicyEngine(policy_flows={self.policy_flows}, clinicians={self.clinicians})"

    def evaluate_and_execute(self):
        for policy_flow in self.policy_flows:
            for clinician in self.clinicians:
                if policy_flow.evaluate_conditions(clinician):
                    for action in policy_flow.actions:
                        ActionExecutor.execute(action, clinician)
                        print()
