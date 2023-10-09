## Project Structure

python
│
├── models
│ ├── init.py
│ ├── condition.py
│ ├── action.py
│ ├── policy_flow.py
│ ├── clinician.py
│ └── policy_engine.py
│
├── utils
│ ├── init.py
│ └── action_executor.py
│
├── main.py
└── README.md

### Models

- `condition.py`: Contains `Condition` and `CompoundCondition` classes to represent individual and compound conditions.
- `action.py`: Contains the `Action` class representing the actions to be executed.
- `policy_flow.py`: Contains the `PolicyFlow` class representing a flow consisting of conditions and corresponding actions.
- `clinician.py`: Contains the `Clinician` class representing a healthcare clinician.
- `policy_engine.py`: Contains the `PolicyEngine` class responsible for evaluating conditions and executing actions based on policy flows.

### Utils

- `action_executor.py`: Contains the `ActionExecutor` class, which is responsible for executing actions.

### Main

- `main.py`: The entry point of your application.

## Task

1. Parse the provided JSON representing Policy Flows and Clinician data.
2. Evaluate the conditions for each clinician based on the given policy flows.
3. Execute the corresponding actions if the conditions are met.
4. Output the results.

## Example Input and Output

### PolicyFlow JSON

```json
{
  "policyFlows": [
    {
      "type": "shift_completed",
      "conditions": {
        "logic": "OR",
        "conditions": [
          // ... conditions
        ]
      },
      "actions": [
        // ... actions
      ]
    }
  ]
}

{
  "clinicians": [
    {
      "id": "c1",
      "name": "John Doe",
      // ... other clinician attributes
    }
  ]
}
```

### Desired Output

Clinician John Doe has met the conditions for the shift_completed policy flow.
Executing actions: allocate_points, send_email
Allocating 200 points to John Doe.
Sending email to johndoe@example.com: "Fantastic Work! You have earned 200 points for your dedication and timeliness."
