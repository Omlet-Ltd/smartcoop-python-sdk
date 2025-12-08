from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class StateGeneral:
    firmwareVersionCurrent: str
    firmwareVersionPrevious: str
    firmwareLastCheck: str
    powerSource: str
    uptime: int
    batteryLevel: Optional[int] = None
    displayLine1: Optional[str] = None
    displayLine2: Optional[str] = None

    @staticmethod
    def from_json(json_data: Any) -> 'StateGeneral':
        return StateGeneral(
            firmwareVersionCurrent=json_data['firmwareVersionCurrent'],
            firmwareVersionPrevious=json_data['firmwareVersionPrevious'],
            firmwareLastCheck=json_data['firmwareLastCheck'],
            powerSource=json_data['powerSource'],
            uptime=json_data['uptime'],
            batteryLevel=json_data['batteryLevel'] if json_data.get('batteryLevel') else None,
            displayLine1=json_data['displayLine1'] if json_data.get('displayLine1') else None,
            displayLine2=json_data['displayLine2'] if json_data.get('displayLine2') else None
        )
