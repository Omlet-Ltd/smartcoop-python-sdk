from dataclasses import dataclass
from typing import Optional, Any
from .configuration_general import ConfigurationGeneral
from .configuration_connectivity import ConfigurationConnectivity
from .configuration_door import ConfigurationDoor
from .configuration_light import ConfigurationLight
from .configuration_feeder import ConfigurationFeeder
from .configuration_fan import ConfigurationFan

@dataclass
class Configuration:
    general: ConfigurationGeneral
    connectivity: ConfigurationConnectivity
    door: Optional[ConfigurationDoor] = None
    light: Optional[ConfigurationLight] = None
    feeder: Optional[ConfigurationFeeder] = None
    fan: Optional[ConfigurationFan] = None

    @staticmethod
    def from_json(json_data: Any) -> 'Configuration':
        return Configuration(
            general=ConfigurationGeneral.from_json(json_data['general']),
            connectivity=ConfigurationConnectivity.from_json(json_data['connectivity']),
            door=ConfigurationDoor.from_json(json_data['door']) if json_data.get('door') else None,
            light=ConfigurationLight.from_json(json_data['light']) if json_data.get('light') else None,
            feeder=ConfigurationFeeder.from_json(json_data['feeder']) if json_data.get('feeder') else None,
            fan=ConfigurationFan.from_json(json_data['fan']) if json_data.get('fan') else None
        )

    def to_json(self) -> dict:
        return {
            "general": self.general.to_json(),
            "connectivity": self.connectivity.to_json(),
            "door": self.door.to_json() if self.door else None,
            "light": self.light.to_json() if self.light else None,
            "feeder": self.feeder.to_json() if self.feeder else None,
            "fan": self.fan.to_json if self.fan else None
        }
