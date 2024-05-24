from dataclasses import dataclass
from typing import Any

@dataclass
class StateLight:
    state: str

    @staticmethod
    def from_json(json_data: Any) -> 'StateLight':
        return StateLight(
            state=json_data['state']
        )
