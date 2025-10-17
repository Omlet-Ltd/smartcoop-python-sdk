from dataclasses import dataclass
from typing import Optional, Any
from .state_connectivity import StateConnectivity
from .state_door import StateDoor
from .state_general import StateGeneral
from .state_light import StateLight
from .state_feeder import StateFeeder
from .state_fan import StateFan

@dataclass
class State:
    general: StateGeneral
    connectivity: StateConnectivity
    door: Optional[StateDoor] = None
    light: Optional[StateLight] = None
    feeder: Optional[StateFeeder] = None
    fan: Optional[StateFan] = None

    @staticmethod
    def from_json(json_data: Any) -> 'State':
        return State(
            general=StateGeneral.from_json(json_data['general']),
            connectivity=StateConnectivity.from_json(json_data['connectivity']),
            door=StateDoor.from_json(json_data['door']) if json_data.get('door') else None,
            light=StateLight.from_json(json_data['light']) if json_data.get('light') else None,
            feeder=StateFeeder.from_json(json_data['feeder']) if json_data.get('feeder') else None,
            fan=StateFan.from_json(json_data['fan']) if json_data.get('fan') else None
        )
