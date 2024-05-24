from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class Action:
    name: str
    description: str
    value: str
    url: str
    pending: Optional[str] = None

    @staticmethod
    def from_json(json_data: Any) -> 'Action':
        return Action(
            name=json_data['actionName'],
            description=json_data['description'],
            value=json_data['actionValue'],
            pending=json_data.get('pendingValue'), 
            url=json_data['url']
        )