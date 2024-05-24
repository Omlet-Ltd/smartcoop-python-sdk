from dataclasses import dataclass
from typing import Any

@dataclass
class StateDoor:
    state: str
    lastOpenTime: str
    lastCloseTime: str
    fault: str
    lightLevel: int

    @staticmethod
    def from_json(json_data: Any) -> 'StateDoor':
        return StateDoor(
            state=json_data['state'],
            lastOpenTime=json_data['lastOpenTime'],
            lastCloseTime=json_data['lastCloseTime'],
            fault=json_data['fault'],
            lightLevel=json_data['lightLevel']
        )
