from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class ConfigurationGeneral:
    datetime: str
    timezone: str
    updateFrequency: int
    statusUpdatePeriod: int
    language: Optional[str] = None
    overnightSleepEnable: Optional[bool] = None
    overnightSleepStart: Optional[str] = None
    overnightSleepEnd: Optional[str] = None
    pollFreq: Optional[int] = None
    stayAliveTime: Optional[int] = None
    useDst: Optional[bool] = None

    @staticmethod
    def from_json(json_data: Any) -> 'ConfigurationGeneral':
        return ConfigurationGeneral(
            datetime=json_data['datetime'],
            timezone=json_data['timezone'],
            updateFrequency=json_data['updateFrequency'],
            statusUpdatePeriod=json_data['statusUpdatePeriod'],
            language=json_data['language'] if json_data.get('language') else None,
            overnightSleepEnable=json_data['overnightSleepEnable'] if json_data.get('overnightSleepEnable') else None,
            overnightSleepStart=json_data['overnightSleepStart'] if json_data.get('overnightSleepStart') else None,
            overnightSleepEnd=json_data['overnightSleepEnd'] if json_data.get('overnightSleepEnd') else None,
            pollFreq=json_data['pollFreq'] if json_data.get('pollFreq') else None,
            stayAliveTime=json_data['stayAliveTime'] if json_data.get('stayAliveTime') else None,
            useDst=json_data['useDst'] if json_data.get('useDst') else None
        )

    def to_json(self) -> dict:
        data = {
            "datetime": self.datetime,
            "timezone": self.timezone,
            "updateFrequency": self.updateFrequency,
            "statusUpdatePeriod": self.statusUpdatePeriod,
        }

        # Only include optional fields if they are explicitly set, to
        # avoid sending JSON nulls that some backend versions reject.
        if self.language is not None:
            data["language"] = self.language
        if self.overnightSleepEnable is not None:
            data["overnightSleepEnable"] = self.overnightSleepEnable
        if self.overnightSleepStart is not None:
            data["overnightSleepStart"] = self.overnightSleepStart
        if self.overnightSleepEnd is not None:
            data["overnightSleepEnd"] = self.overnightSleepEnd
        if self.pollFreq is not None:
            data["pollFreq"] = self.pollFreq
        if self.stayAliveTime is not None:
            data["stayAliveTime"] = self.stayAliveTime
        if self.useDst is not None:
            data["useDst"] = self.useDst

        return data
