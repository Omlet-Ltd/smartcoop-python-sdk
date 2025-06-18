from dataclasses import dataclass
from typing import Any

@dataclass
class StateFeeder:
    state: str
    lastOpenTime: str
    lastCloseTime: str
    fault: str
    lightLevel: int
    feedLevel: int
    mode: str

    @staticmethod
    def from_json(json_data: Any) -> 'StateFeeder':
        return StateFeeder(
            state=json_data['state'],
            lastOpenTime=json_data['lastOpenTime'],
            lastCloseTime=json_data['lastCloseTime'],
            fault=json_data['fault'],
            lightLevel=json_data['lightLevel'],
            feedLevel=json_data['feedLevel'],
            mode=json_data['mode']
        )
