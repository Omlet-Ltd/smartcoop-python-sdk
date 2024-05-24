from dataclasses import dataclass
from typing import List, Any
from .action import Action
from .configuration import Configuration
from .state import State

@dataclass
class Device:
    deviceId: str
    name: str
    deviceType: str
    state: State
    configuration: Configuration
    actions: List[Action]

    @staticmethod
    def from_json(json_data: Any) -> 'Device':
        return Device(
            deviceId=json_data['deviceId'],
            name=json_data['name'],
            deviceType=json_data['deviceType'],
            state=State.from_json(json_data['state']),
            configuration=Configuration.from_json(json_data['configuration']),
            actions=[Action.from_json(action) for action in json_data['actions']]
        )
