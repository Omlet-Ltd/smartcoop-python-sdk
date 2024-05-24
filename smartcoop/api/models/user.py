from dataclasses import dataclass
from typing import Optional, List, Any
from .group_subset import GroupSubset

@dataclass
class User:
    firstName: str
    lastName: str
    userId: Optional[str] = None
    emailAddress: Optional[str] = None
    siteLink: Optional[str] = None
    invites: Optional[List[GroupSubset]] = None

    @staticmethod
    def from_json(json_data: Any) -> 'User':
        return User(
            userId=json_data.get('userId'),
            firstName=json_data['firstName'],
            lastName=json_data['lastName'],
            emailAddress=json_data.get('emailAddress'),
            siteLink=json_data.get('siteLink'),
            invites=[GroupSubset.from_json(invite) for invite in json_data['invites']] if json_data.get('invites') else None
        )

    def to_json(self) -> dict:
        return {
            "userId": self.userId,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "emailAddress": self.emailAddress,
            "siteLink": self.siteLink,
            "invites": [invite.to_json() for invite in self.invites] if self.invites else None
        }
