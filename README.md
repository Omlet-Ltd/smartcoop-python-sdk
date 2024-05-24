# Omlet Python SDK
This SDK is designed to facilitate seamless authentication with Omlet and provide interaction with
devices. With our SDK, developers can easily retrieve device information, and execute actions
tailored to their devices and groups.

## Introduction
- [Getting Started](#getting-started)
- [Authentication](#authentication)
- [Omlet](#omlet)
- [Types](#types)

## Getting Started

### Overview
To use this SDK the user will already be registered with omlet as you will use the same email and password credentials to authenticate.
We will go through the steps for including this SDK in your application and how to interact with your devices.

### Installation
To install the SmartCoop SDK, ensure you have pip installed on your system. Then, create or navigate to your project
directory and execute the following command:

```bash
pip install smartcoop-python-sdk
```

## Authentication

### Create API Key

To generate an API key you'll need to login to the developer console with the email and password that use for the App.
Once logged in navigate to "API Keys" and click "Generate Key". Take note of this key.

## Omlet

### Overview
The Omlet object offers the ability to interact with your devices, groups and user actions.

### Creating an Instance
Use the apiKey you've created to start omlet.
```python
from smartcoop.client import SmartCoopClient
from smartcoop.api.omlet import Omlet

client = SmartCoopClient(client_secret='Xwa661NcAF__secret')
omlet = Omlet(client)
```
### Retrieving Devices
```python
devices = omlet.get_devices()
```

### Device Actions
Devices have a list of actions that can be executed against them. They're represented by the [action](#action) class.

#### Using an Action

```python
open_action = next((action for action in device.actions if action.name == 'open'), None)

if open_action:
    omlet.perform_action(open_action)
```

### Updating Device Configuration
```python
config = device.configuration

configuration = device.configuration
configuration.general.language = 'US'

omlet.update_configuration(device.deviceId, configuration)
```

A full list of the available actions for omlet can be found here:

- **`get_devices()`**
    - **Description**: Retrieves a list of all devices.
    - **Returns**: `List[Device]`

- **`get_device_by_id(id: str)`**
    - **Description**: Retrieves a specific device by its ID.
    - **Parameters**:
        - `id`: The ID of the device.
    - **Returns**: `Device`

- **`perform_action(action: Action)`**
    - **Description**: Performs a specified action.
    - **Parameters**:
        - `action`: The `Action` object to be performed.

- **`update_configuration(device_id: str, configuration: Configuration)`**
    - **Description**: Updates the configuration of a specific device.
    - **Parameters**:
        - `device_id`: The ID of the device.
        - `configuration`: The new `Configuration` object.

- **`get_groups()`**
    - **Description**: Retrieves a list of all groups.
    - **Returns**: `List[Group]`

- **`get_group_by_id(id: str)`**
    - **Description**: Retrieves a specific group by its ID.
    - **Parameters**:
        - `id`: The ID of the group.
    - **Returns**: `Group`

- **`create_group(name: str)`**
    - **Description**: Creates a new group with the specified name.
    - **Parameters**:
        - `name`: The name of the new group.
    - **Returns**: `Group`

- **`get_user()`**
    - **Description**: Retrieves the current user information.
    - **Returns**: `User`

- **`accept_invite(group: GroupSubset)`**
    - **Description**: Accepts an invite to join a group.
    - **Parameters**:
        - `group`: The `GroupSubset` object representing the group invitation.

- **`reject_invite(group: GroupSubset)`**
    - **Description**: Rejects an invite to join a group.
    - **Parameters**:
        - `group`: The `GroupSubset` object representing the group invitation.

- **`update_group(group_id: str, group_name: str)`**
    - **Description**: Updates the name of a specific group.
    - **Parameters**:
        - `group_id`: The ID of the group.
        - `group_name`: The new name for the group.

- **`delete_group(group_id: str)`**
    - **Description**: Deletes a specific group.
    - **Parameters**:
        - `group_id`: The ID of the group.

- **`invite_user(group_id: str, email_address: str, access: str)`**
    - **Description**: Invites a user to a group.
    - **Parameters**:
        - `group_id`: The ID of the group.
        - `email_address`: The email address of the user to invite.
        - `access`: The access level to grant to the user.

- **`remove_user(group_id: str, email_address: str)`**
    - **Description**: Removes a user from a group.
    - **Parameters**:
        - `group_id`: The ID of the group.
        - `email_address`: The email address of the user to remove.

- **`update_user_access(group_id: str, email_address: str, access: str)`**
    - **Description**: Updates a user's access level in a group.
    - **Parameters**:
        - `group_id`: The ID of the group.
        - `email_address`: The email address of the user.
        - `access`: The new access level for the user.




### Types
#### Action
```python
@dataclass
class Action:
    name: str
    description: str
    value: str
    url: str
    pending: Optional[str] = None
```

#### Configuration Connectivity
```python
@dataclass
class ConfigurationConnectivity:
    wifiState: str
```

#### Configuration Door
```python
@dataclass
class ConfigurationDoor:
    doorType: str
    openMode: str
    openDelay: int
    openLightLevel: int
    openTime: str
    closeMode: str
    closeDelay: int
    closeLightLevel: int
    closeTime: str
    colour: str
```

#### Configuration General
```python
@dataclass
class ConfigurationGeneral:
    datetime: str
    timezone: str
    updateFrequency: int
    language: str
    overnightSleepEnable: bool
    overnightSleepStart: str
    overnightSleepEnd: str
    pollFreq: int
    stayAliveTime: int
    statusUpdatePeriod: int
    useDst: Optional[bool] = None
```

#### Configuration Light
```python
@dataclass
class ConfigurationLight:
    mode: str
    minutesBeforeClose: int
    maxOnTime: int
    equipped: int
```

#### Configuration
```python
@dataclass
class Configuration:
    general: ConfigurationGeneral
    connectivity: ConfigurationConnectivity
    door: Optional[ConfigurationDoor] = None
    light: Optional[ConfigurationLight] = None

```

#### Device
```python
@dataclass
class Device:
    deviceId: str
    name: str
    deviceType: str
    state: State
    configuration: Configuration
    actions: List[Action]
```

#### Group Subset
```python
@dataclass
class GroupSubset:
    groupId: str
    groupName: str
    access: str
```

#### Group
```python
@dataclass
class Group:
    groupId: str
    groupName: str
    devices: List[Device]
    admins: List[User]
    users: List[User]
    access: Optional[str] = None
```

#### State Connectivity
```python
@dataclass
class StateConnectivity:
    ssid: str
    wifiStrength: str
```

#### State Door
```python
@dataclass
class StateDoor:
    state: str
    lastOpenTime: str
    lastCloseTime: str
    fault: str
    lightLevel: int
```

#### State General
```python
@dataclass
class StateGeneral:
    firmwareVersionCurrent: str
    firmwareVersionPrevious: str
    firmwareLastCheck: str
    batteryLevel: int
    powerSource: str
    uptime: int
    displayLine1: str
    displayLine2: str
```

#### State Light
```python
@dataclass
class StateLight:
    state: str
```

#### State
```python
@dataclass
class State:
    general: StateGeneral
    connectivity: StateConnectivity
    door: Optional[StateDoor] = None
    light: Optional[StateLight] = None
```

#### User
```python
@dataclass
class User:
    firstName: str
    lastName: str
    userId: Optional[str] = None
    emailAddress: Optional[str] = None
    siteLink: Optional[str] = None
    invites: Optional[List[GroupSubset]] = None
```