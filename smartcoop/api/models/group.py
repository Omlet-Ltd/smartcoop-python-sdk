from dataclasses import dataclass
from typing import Optional, List, Any
from .device import Device 
from .user import User

@dataclass
class Group:
    groupId: str
    groupName: str
    devices: List[Device]
    admins: List[User]
    users: List[User]
    access: Optional[str] = None

    @staticmethod
    def from_json(json_data: Any) -> 'Group':
        return Group(
            groupId=json_data['groupId'],
            groupName=json_data['groupName'],
            access=json_data.get('access'),
            devices=[Device.from_json(device) for device in json_data['devices']],
            admins=[User.from_json(admin) for admin in json_data['admins']],
            users=[User.from_json(user) for user in json_data['users']]
        )

    def to_json(self) -> dict:
        return {
            "groupId": self.groupId,
            "groupName": self.groupName,
            "access": self.access,
            "devices": [device.to_json() for device in self.devices],
            "admins": [admin.to_json() for admin in self.admins],
            "users": [user.to_json() for user in self.users]
        }
