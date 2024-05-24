from dataclasses import dataclass
from typing import Any

@dataclass
class ConfigurationConnectivity:
    wifiState: str

    @staticmethod
    def from_json(json_data: Any) -> 'ConfigurationConnectivity':
        return ConfigurationConnectivity(
            wifiState=json_data['wifiState']
        )

    def to_json(self) -> dict:
        return {
            "wifiState": self.wifiState
        }
