from typing import List
from .condition import CompoundCondition
from .action import Action
from .clinician import Clinician
from typing import List, Union, Dict, Any


class PolicyFlow:
    def __init__(self, type: str, conditions: CompoundCondition, actions: List[Action]):
        self.type = type
        self.conditions = conditions
        self.actions = actions

    def __str__(self):
        action_strs = [str(action) for action in self.actions]
        return f"PolicyFlow(type={self.type}, conditions={self.conditions.__str__()}, actions={action_strs})"

    def evaluate_conditions(self, clinician: Clinician) -> bool:
        return self.conditions.evaluate(clinician)
