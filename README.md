# OverPy
Web scraper for Overwatch statistics
## Dependencies
requests

lxml

## Usage
Import OverPy and the overpy function
```Python
from overpy import overpy
```

Use the 'Overpy' function as follows

```Python
player_stats = overpy('en-us', 'pc', 'Player-1234')
```
The strings passed are in the order of: region, platform, BattleTag(replacing the # with a -).

You must enter the full BattleTag including the trailing numbers.

NOTE: there will be a delay while the scraper is running.

Retrieve statistics from the returned dictionary as follows:

```Python
player_stats['ALL HEROES']['Eliminations']
>>>'1,169'
stats['REAPER']['Time Spent on Fire']
>>>'05:08'
```

I will work on making the capitilization more intuitive for the dictionary.

NOTE: as of now this only retrieves competitive stats.

