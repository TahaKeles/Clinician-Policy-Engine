import json
import os
from models.policy_flow import PolicyFlow
from models.condition import CompoundCondition
from models.action import Action
from models.clinician import Clinician
from models.policy_engine import PolicyEngine


def main():
    # Read policy flow data from file
    with open(
        os.path.join(os.path.dirname(__file__), "data", "policyFlowExample.json")
    ) as f:
        policy_flow_data = json.load(f)

    # Read clinician data from file
    with open(
        os.path.join(os.path.dirname(__file__), "data", "clinicianExample.json")
    ) as f:
        clinician_data = json.load(f)

    policy_flows = policy_flow_data["policyFlows"]
    clinicians = clinician_data["clinicians"]

    policy_flow_objects = [
        PolicyFlow(
            rf["type"],
            CompoundCondition.from_dict(rf["conditions"]),
            [
                Action(a["type"], a.get("value"), a.get("message"))
                for a in rf["actions"]
            ],
        )
        for rf in policy_flows
    ]
    clinician_objects = [
        Clinician(
            cg["id"],
            cg["name"],
            cg["shift_count"],
            cg["timeliness"],
            cg["open_shifts_picked"],
            cg["streak"],
            cg["email"],
        )
        for cg in clinicians
    ]

    policy_engine = PolicyEngine(policy_flow_objects, clinician_objects)
    policy_engine.evaluate_and_execute()


if __name__ == "__main__":
    main()
