from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class ConfigurationGeneral:
    datetime: str
    timezone: str
    updateFrequency: int
    language: Optional[str] = None
    overnightSleepEnable: Optional[bool] = None
    overnightSleepStart: Optional[str] = None
    overnightSleepEnd: Optional[str] = None
    pollFreq: Optional[int] = None
    stayAliveTime: Optional[int] = None
    statusUpdatePeriod: int
    useDst: Optional[bool] = None

    @staticmethod
    def from_json(json_data: Any) -> 'ConfigurationGeneral':
        return ConfigurationGeneral(
            datetime=json_data['datetime'],
            timezone=json_data['timezone'],
            useDst=json_data.get('useDst'),
            updateFrequency=json_data['updateFrequency'],
            language=json_data['language'] if json_data.get('language') else None,
            overnightSleepEnable=json_data['overnightSleepEnable'] if json_data.get('overnightSleepEnable') else None,
            overnightSleepStart=json_data['overnightSleepStart'] if json_data.get('overnightSleepStart') else None,
            overnightSleepEnd=json_data['overnightSleepEnd'] if json_data.get('overnightSleepEnd') else None,
            pollFreq=json_data['pollFreq'] if json_data.get('pollFreq') else None,
            stayAliveTime=json_data['stayAliveTime'] if json_data.get('stayAliveTime') else None,
            statusUpdatePeriod=json_data['statusUpdatePeriod'],
            useDst=json_data['useDst'] if json_data.get('language') else None
        )

    def to_json(self) -> dict:
        return {
            "datetime": self.datetime,
            "timezone": self.timezone,
            "useDst": self.useDst,
            "updateFrequency": self.updateFrequency,
            "language": self.language,
            "overnightSleepEnable": self.overnightSleepEnable,
            "overnightSleepStart": self.overnightSleepStart,
            "overnightSleepEnd": self.overnightSleepEnd,
            "pollFreq": self.pollFreq,
            "stayAliveTime": self.stayAliveTime,
            "statusUpdatePeriod": self.statusUpdatePeriod,
            "useDst": self.useDst
        }
