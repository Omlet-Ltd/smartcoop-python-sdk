from dataclasses import dataclass
from typing import Optional, Any
from .state_connectivity import StateConnectivity
from .state_door import StateDoor
from .state_general import StateGeneral
from .state_light import StateLight

@dataclass
class State:
    general: StateGeneral
    connectivity: StateConnectivity
    door: Optional[StateDoor] = None
    light: Optional[StateLight] = None

    @staticmethod
    def from_json(json_data: Any) -> 'State':
        return State(
            general=StateGeneral.from_json(json_data['general']),
            connectivity=StateConnectivity.from_json(json_data['connectivity']),
            door=StateDoor.from_json(json_data['door']) if json_data.get('door') else None,
            light=StateLight.from_json(json_data['light']) if json_data.get('light') else None
        )
