from dataclasses import dataclass
from typing import Any

@dataclass
class GroupSubset:
    groupId: str
    groupName: str
    access: str

    @staticmethod
    def from_json(json_data: Any) -> 'GroupSubset':
        return GroupSubset(
            groupId=json_data['groupId'],
            groupName=json_data['groupName'],
            access=json_data['access']
        )

    def to_json(self) -> dict:
        return {
            "groupId": self.groupId,
            "groupName": self.groupName,
            "access": self.access
        }
