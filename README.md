Overview
========
The purpose of this repo is to illustrate how to combine csv data and json
data, aggregated it, and report results using libraries exclusively built
into python. In this case, we join based on user id, look for measurements
where the temperature reading is greater than 99.5 degrees, indicating a
fever. We then present results, counting up both unique and total 
occurrences, per zip code, per date.

How to run this
===============
To execute results, ensure you are in the repo's directory. The code should
be able to run successfully with the latest versions of both python 2 and 3.

```
python2 fever_population.py
python3 fever_population.py
```


Results
=======
With either version you should see the same results below, though your tab
settings could make the output inconsistent:

```
User file (user_data.csv) records: 398
Reading file (readings.json) records: 400
Joined count matches reading data
Fever entry count: 47
Fever Detection Results
```
 
	|Date		|Zip	|Unique Count	|Total Count	|Duplicate Detected	|
	=================================================================================
	|2018-03-15	|12198	|3		|4		|	X		|
	|2018-03-15	|13464	|2		|2		|			|
	|2018-03-15	|30585	|6		|7		|	X		|
	|2018-03-15	|34709	|3		|4		|	X		|
	|2018-03-15	|36493	|2		|2		|			|
	|2018-03-15	|39234	|3		|4		|	X		|
	|2018-03-15	|43795	|5		|5		|			|
	|2018-03-15	|44842	|3		|3		|			|
	|2018-03-15	|45055	|1		|1		|			|
	|2018-03-15	|46197	|1		|1		|			|
	|2018-03-15	|46279	|2		|2		|			|
	|2018-03-15	|48795	|3		|3		|			|
	|2018-03-15	|70272	|2		|2		|			|
	|2018-03-15	|74471	|1		|1		|			|
	|2018-03-15	|77189	|1		|1		|			|
	|2018-03-15	|92167	|2		|2		|			|
	|2018-03-15	|95483	|1		|1		|			|
	|2018-03-15	|99178	|2		|2		|			|

