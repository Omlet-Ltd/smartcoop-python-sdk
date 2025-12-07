import unittest
import json
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from smartcoop.api.models import Device

class TestDeviceParsing(unittest.TestCase):
    def setUp(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.project_root = os.path.dirname(self.base_path)

    def test_parse_sample_with_fan(self):
        file_path = os.path.join(self.project_root, 'sampleWithFan.json')
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # The sample files contain a single device object
        device = Device.from_json(data)
        self.assertIsInstance(device, Device)
        self.assertIsNotNone(device.deviceId)
        self.assertIsNotNone(device.name)
        self.assertIsNotNone(device.deviceType)
        self.assertIsNotNone(device.state)
        self.assertIsNotNone(device.configuration)
        self.assertIsNotNone(device.actions)

    def test_parse_sample_with_light(self):
        file_path = os.path.join(self.project_root, 'sampleWithLight.json')
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        # The sample files contain a single device object
        device = Device.from_json(data)
        self.assertIsInstance(device, Device)
        self.assertIsNotNone(device.deviceId)
        self.assertIsNotNone(device.name)
        self.assertIsNotNone(device.deviceType)
        self.assertIsNotNone(device.state)
        self.assertIsNotNone(device.configuration)
        self.assertIsNotNone(device.actions)

if __name__ == '__main__':
    unittest.main()
