from dataclasses import dataclass
from typing import Any

@dataclass
class ConfigurationFeeder:
    mode: str
    openLightLevel: int
    closeLightLevel: int
    openTime1: str
    openTime2: str
    openTime3: str
    openTime4: str
    closeTime1: str
    closeTime2: str
    closeTime3: str
    closeTime4: str

    @staticmethod
    def from_json(json_data: Any) -> 'ConfigurationFeeder':
        return ConfigurationFeeder(
            mode=json_data['mode'],
            openLightLevel=json_data['openLightLevel'],
            closeLightLevel=json_data['closeLightLevel'],
            openTime1=json_data['openTime1'],
            openTime2=json_data['openTime2'],
            openTime3=json_data['openTime3'],
            openTime4=json_data['openTime4'],
            closeTime1=json_data['closeTime1'],
            closeTime2=json_data['closeTime2'],
            closeTime3=json_data['closeTime3'],
            closeTime4=json_data['closeTime4']
        )

    def to_json(self) -> dict:
        return {
            "mode": self.mode,
            "openLightLevel": self.openLightLevel,
            "closeLightLevel": self.closeLightLevel,
            "openTime1": self.openTime1,
            "openTime2": self.openTime2,
            "openTime3": self.openTime3,
            "openTime4": self.openTime4,
            "closeTime1": self.closeTime1,
            "closeTime2": self.closeTime2,
            "closeTime3": self.closeTime3,
            "closeTime4": self.closeTime4
        }
