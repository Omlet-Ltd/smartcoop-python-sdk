from dataclasses import dataclass
from typing import Any

@dataclass
class StateGeneral:
    firmwareVersionCurrent: str
    firmwareVersionPrevious: str
    firmwareLastCheck: str
    batteryLevel: int
    powerSource: str
    uptime: int
    displayLine1: str
    displayLine2: str

    @staticmethod
    def from_json(json_data: Any) -> 'StateGeneral':
        return StateGeneral(
            firmwareVersionCurrent=json_data['firmwareVersionCurrent'],
            firmwareVersionPrevious=json_data['firmwareVersionPrevious'],
            firmwareLastCheck=json_data['firmwareLastCheck'],
            batteryLevel=json_data['batteryLevel'],
            powerSource=json_data['powerSource'],
            uptime=json_data['uptime'],
            displayLine1=json_data['displayLine1'],
            displayLine2=json_data['displayLine2']
        )
