## OverPy
Web scraper for Overwatch statistics
### Dependencies
requests

lxml

### How to use
Import OverPy and the Overpy class
```Python
from overpy import Overpy
```

You will need to create an instance of the 'Overpy' class as follows

```Python
joe = Overpy('en-us', 'pc', 'joe-1234')
```
The strings passed are in the order of: region, platform, BattleTag(replacing the # with a -).

You must enter the full BattleTag including the trailing numbers.

Use the get_stats method to gather player statistics. This method returns a dictionary.

```Python
stats = joe.get_stats()
```

Note there will be a delay while the scraper is running.

Retrieve statistics from the nested dictionary as follows:

```Python
stats['ALL HEROES']['Eliminations']
>>>'1,169'
stats['REAPER']['Time Spent on Fire']
>>>'05:08'
```

I will work on making the capitilization more intuitive for the dictionary.

NOTE: as of now this only retrieves competitive stats.

