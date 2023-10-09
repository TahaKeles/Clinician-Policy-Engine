from models.action import Action
from models.clinician import Clinician


class ActionExecutor:
    @staticmethod
    def execute(action: Action, clinician: Clinician):
        if action.type == "allocate_points":
            print(
                f"Clinician ID: {clinician.id}\nAction: {action.type}\nValue: {action.value}"
            )
        elif action.type == "send_email":
            print(
                f"Clinician ID: {clinician.id}\nAction: {action.type}\nMessage: {action.message}"
            )
        else:
            print(f"Unknown action type: {action.type}")
