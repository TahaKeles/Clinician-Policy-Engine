from typing import List, Union, Dict, Any
from .clinician import Clinician


class Condition:
    def __init__(self, attribute: str, operator: str, value: Union[str, int, bool]):
        self.attribute = attribute
        self.operator = operator
        self.value = value

    def __str__(self):
        return f"Condition(attribute={self.attribute}, operator={self.operator}, value={self.value})"

    def evaluate(self, clinician: Clinician) -> bool:
        if hasattr(clinician, self.attribute):
            clinician_value = getattr(clinician, self.attribute)
            if self.operator == "==":
                return clinician_value == self.value
            elif self.operator == ">=":
                return clinician_value >= self.value
            elif self.operator == "<=":
                return clinician_value <= self.value
            elif self.operator == ">":
                return clinician_value > self.value
            elif self.operator == "<":
                return clinician_value < self.value
        return False


class CompoundCondition:
    def __init__(
        self, logic: str, conditions: List[Union[Condition, "CompoundCondition"]]
    ):
        self.logic = logic
        self.conditions = conditions

    def __str__(self):
        condition_strs = [str(condition) for condition in self.conditions]
        return f"CompoundCondition(logic={self.logic}, conditions={condition_strs})"

    def evaluate(self, clinician: Clinician) -> bool:
        if self.logic == "AND":
            return all(condition.evaluate(clinician) for condition in self.conditions)
        elif self.logic == "OR":
            return any(condition.evaluate(clinician) for condition in self.conditions)
        else:
            return False

    @classmethod
    def from_dict(cls, data: Dict) -> "CompoundCondition":
        logic = data["logic"]
        conditions = []
        for cond in data["conditions"]:
            if "logic" in cond:
                conditions.append(CompoundCondition.from_dict(cond))
            else:
                conditions.append(
                    Condition(cond["attribute"], cond["operator"], cond["value"])
                )
        return cls(logic, conditions)
