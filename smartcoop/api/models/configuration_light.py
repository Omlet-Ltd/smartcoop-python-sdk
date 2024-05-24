from dataclasses import dataclass
from typing import Any

@dataclass
class ConfigurationLight:
    mode: str
    minutesBeforeClose: int
    maxOnTime: int
    equipped: int

    @staticmethod
    def from_json(json_data: Any) -> 'ConfigurationLight':
        return ConfigurationLight(
            mode=json_data['mode'],
            minutesBeforeClose=json_data['minutesBeforeClose'],
            maxOnTime=json_data['maxOnTime'],
            equipped=json_data['equipped']
        )

    def to_json(self) -> dict:
        return {
            "mode": self.mode,
            "minutesBeforeClose": self.minutesBeforeClose,
            "maxOnTime": self.maxOnTime,
            "equipped": self.equipped
        }
