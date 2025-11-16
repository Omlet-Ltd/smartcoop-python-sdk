from dataclasses import dataclass
from typing import Any

@dataclass
class ConfigurationFan:
    mode: str
    manualSpeed: int
    timeOn1: str
    timeOn2: str
    timeOn3: str
    timeOn4: str
    timeOff1: str
    timeOff2: str
    timeOff3: str
    timeOff4: str
    timeSpeed1: int
    timeSpeed2: int
    timeSpeed3: int
    timeSpeed4: int
    tempOn: int
    tempOff: int
    tempSpeed: int

    @staticmethod
    def from_json(json_data: Any) -> 'ConfigurationFan':
        return ConfigurationFan(
            mode = json_data['mode'],
            manualSpeed = json_data['manualSpeed'],
            timeOn1 = json_data['timeOn1'],
            timeOn2 = json_data['timeOn2'],
            timeOn3 = json_data['timeOn3'],
            timeOn4 = json_data['timeOn4'],
            timeOff1 = json_data['timeOff1'],
            timeOff2 = json_data['timeOff2'],
            timeOff3 = json_data['timeOff3'],
            timeOff4 = json_data['timeOff4'],
            timeSpeed1 = json_data['timeSpeed1'],
            timeSpeed2 = json_data['timeSpeed2'],
            timeSpeed3 = json_data['timeSpeed3'],
            timeSpeed4 = json_data['timeSpeed4'],
            tempOn = json_data['tempOn'],
            tempOff = json_data['tempOff'],
            tempSpeed = json_data['tempSpeed']
        )

    def to_json(self) -> dict:
        return {
            "mode": self.mode,
            "manualSpeed": self.manualSpeed,
            "timeOn1": self.timeOn1,
            "timeOn2": self.timeOn2,
            "timeOn3": self.timeOn3,
            "timeOn4": self.timeOn4,
            "timeOff1": self.timeOff1,
            "timeOff2": self.timeOff2,
            "timeOff3": self.timeOff3,
            "timeOff4": self.timeOff4,
            "timeSpeed1": self.timeSpeed1,
            "timeSpeed2": self.timeSpeed2,
            "timeSpeed3": self.timeSpeed3,
            "timeSpeed4": self.timeSpeed4,
            "tempOn": self.tempOn,
            "tempOff": self.tempOff,
            "tempSpeed": self.tempSpeed
        }
