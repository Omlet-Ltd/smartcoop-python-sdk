from typing import List
from smartcoop.client import SmartCoopClient
from smartcoop.api.models import Device, Action, Configuration, Group, User, GroupSubset

class Omlet:
    def __init__(self, client: SmartCoopClient):
        self.client = client

    def get_devices(self) -> List[Device]:
        endpoint = 'device'
        response = self.client.get(endpoint)
        devices = [Device.from_json(device_json) for device_json in response]
        return devices

    def get_device_by_id(self, id) -> Device:
        endpoint = f'device/{id}'
        response = self.client.get(endpoint)
        device = Device.from_json(response)
        return device

    def perform_action(self, action: Action) -> None:
        endpoint = action.url.lstrip('/')
        self.client.post(endpoint)

    def update_configuration(self, device_id: str, configuration: Configuration) -> None:
        endpoint = f'device/{device_id}/configuration'
        self.client.patch(endpoint, json=configuration.to_json())

    def get_groups(self) -> List[Group]:
        endpoint = 'group'
        response = self.client.get(endpoint)
        groups = [Group.from_json(group_json) for group_json in response]
        return groups

    def get_group_by_id(self, id) -> Group:
        endpoint = f'group/{id}'
        response = self.client.get(endpoint)
        group = Group.from_json(response)
        return group

    def create_group(self, name) -> Group:
        endpoint = f'group/{id}'
        payload = {'groupName': name}
        response = self.client.post(endpoint, payload)
        group = Group.from_json(response)
        return group

    def get_user(self) -> User:
        endpoint = 'whoami'
        response = self.client.get(endpoint)
        user = User.from_json(response)
        return user

    def accept_invite(self, group: GroupSubset) -> None:
        endpoint = f'invite/{group.groupId}'
        self.client.post(endpoint)

    def reject_invite(self, group: GroupSubset) -> None:
        endpoint = f'invite/{group.groupId}'
        self.client.delete(endpoint)

    def update_group_name(self, group_id: str, group_name: str) -> None:
        endpoint = f'group/{group_id}'
        payload = {'groupName': group_name}
        self.client.patch(endpoint, json=payload)

    def delete_group(self, group_id: str) -> None:
        endpoint = f'group/{group_id}'
        self.client.delete(endpoint)

    def invite_user(self, group_id: str, email_address: str, access: str) -> None:
        endpoint = f'group/{group_id}/user'
        payload = {'emailAddress': email_address, 'access': access}
        self.client.post(endpoint, json=payload)

    def remove_user(self, group_id: str, email_address: str) -> None:
        endpoint = f'group/{group_id}/user'
        payload = {'emailAddress': email_address}
        self.client.delete(endpoint, json=payload)

    def update_user_access(self, group_id: str, email_address: str, access: str) -> None:
        endpoint = f'group/{group_id}/user'
        payload = {'emailAddress': email_address, 'access': access}
        self.client.patch(endpoint, json=payload)
