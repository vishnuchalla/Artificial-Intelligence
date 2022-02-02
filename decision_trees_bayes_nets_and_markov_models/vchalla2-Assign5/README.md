The Decision-Theory.py contains code to generate a decision tree and extract the outcome of it.

Use command prompt to compile the given python file and execute as below.

## Syntax

```
python3 Decision-Theory.py file_location
```

## Sample execution

```
python3 Decision-Theory.py Problem.txt
```

This will execute the given program and will log the output on the screen.

## Output

```
Nodes while building the decision tree:

Adding Node 1 choice Start None
Adding Node 2 outcome Out1 Start
Adding Node 3 outcome Out0 Start
Adding Node 4 lottery TestLottery Start
Adding Node 5 choice Purchase TestLottery
Adding Node 6 outcome Out2 Purchase
Adding Node 7 lottery CarLottery Purchase
Adding Node 8 outcome Out4 CarLottery
Adding Node 9 outcome Out3 CarLottery
Adding Node 10 choice Purchase TestLottery
Adding Node 11 outcome Out2 Purchase
Adding Node 12 lottery CarLottery Purchase
Adding Node 13 outcome Out4 CarLottery
Adding Node 14 outcome Out3 CarLottery

Nodes while updating the decision tree:

Expected Value Node:12, CarLottery 35.0
Decision Node:10, Purchase Buy 35.0
Expected Value Node:7, CarLottery 35.0
Decision Node:5, Purchase Buy 35.0
Expected Value Node:4, TestLottery 35.0
Decision Node:1, Start Test 35.0
```
