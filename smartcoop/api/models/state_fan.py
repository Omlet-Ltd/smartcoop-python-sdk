from dataclasses import dataclass
from typing import Any

@dataclass
class StateFan:
    state: str
    temperature: int
    humidity: int

    @staticmethod
    def from_json(json_data: Any) -> 'StateFan':
        return StateFan(
            state = json_data['state'],
            temperature = json_data['temperature'],
            humidity = json_data['humidity']
        )
