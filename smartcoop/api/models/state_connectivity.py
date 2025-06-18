from dataclasses import dataclass
from typing import Any

@dataclass
class StateConnectivity:
    ssid: str
    wifiStrength: str
    connected: bool

    @staticmethod
    def from_json(json_data: Any) -> 'StateConnectivity':
        return StateConnectivity(
            ssid=json_data['ssid'],
            wifiStrength=json_data['wifiStrength'],
            connected=json_data['connected']
        )
