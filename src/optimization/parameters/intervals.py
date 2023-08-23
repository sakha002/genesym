from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Optional, List



@dataclass
class Interval:
    interval_end: Optional[datetime]
    interval_duration: timedelta = timedelta(minutes=60)
    index: int
    
    
    @staticmethod
    def create_intervals_from_input(time_stamps: List[datetime]) -> List["Interval"]:
        # looks like we should assume interval beginning for the time stamps
        
        interval_durations: List[timedelta] = [
            time_stamps[i+1] - time_stamps[i]
            for i in range(len(time_stamps) - 1)
        ]
        interval_durations.append(interval_durations[-1])
        # assumes the last interval has the same duration as the previous one
        
        interval_ends: List[datetime] = [
            time_stamps[i] + interval_durations[i]
            for i in range(len(time_stamps))
        ]
        
        return [
            Interval(
                interval_end=interval_ends[i],
                interval_duration=interval_durations[i],
                index=i,
            )
            for i in range(len(interval_ends))
        ]
    