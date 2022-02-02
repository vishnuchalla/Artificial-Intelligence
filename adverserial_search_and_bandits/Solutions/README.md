The zip file contains implementation of all the 3 bandit algorithms STAT, ROLL and REC.

Here is the demonstration on how to trigger the code for each algorithm.

# STAT:

## Syntax

```
bandit.py [-h] -a {STAT,ROLL,REC} -e EXP -u DIST -d DECAY [-r RWT] -w W0 -i INFILE
```

Output will be printed on the console. It can also be piped to a file.

## Sample execution

```
python3 bandit.py -a STAT -e 0.5 -u 0.5 -d 0.5 -r 0.5 -w 1 -i Data1.csv

STDOUT
Current Step: 1
Decision Made: Arm5
Current Reward: 0.0
Cummulative Reward: 0.0

Current Step: 2
Decision Made: Arm2
Current Reward: 0.0
Cummulative Reward: 0.0
.
.
.
.
.
.
Current Step: 5000
Decision Made: Arm6
Current Reward: 0.0
Cummulative Reward: 2426.0
```

# ROLL:

## Syntax

```
bandit.py [-h] -a {STAT,ROLL,REC} -e EXP -u DIST -d DECAY [-r RWT] -w W0 -i INFILE
```

Output will be printed on the console. It can also be piped to a file.

## Sample execution

```
python3 bandit.py --a ROLL -e 0.50 -u 0.5 -d 0.5 -w 1 -i Data2.csv

STDOUT
Current Step: 1
Decision Made: Arm4
Current Reward: 0.0
Cummulative Reward: 0.0

Current Step: 2
Decision Made: Arm2
Current Reward: 0.0
Cummulative Reward: 0.0
.
.
.
.
.
.
Current Step: 5000
Decision Made: Arm3
Current Reward: 26.0
Cummulative Reward: 143618.0
```

# REC:

## Syntax

```
bandit.py [-h] -a {STAT,ROLL,REC} -e EXP -u DIST -d DECAY [-r RWT] -w W0 -i INFILE
```

Output will be printed on the console. It can also be piped to a file.

## Sample execution

```
python3 bandit.py --a REC -e 0.50 -u 0.5 -d 0.5 -w 1 -i Data2.csv

STDOUT
Current Step: 1
Decision Made: Arm2
Current Reward: 0.0
Cummulative Reward: 0.0

Current Step: 2
Decision Made: Arm2
Current Reward: 0.0
Cummulative Reward: 0.0
.
.
.
.
.
.
Current Step: 5000
Decision Made: Arm3
Current Reward: 26.0
Cummulative Reward: 132011.0
```
