The a3q3.pl contains code to perform min-max and alpha beta pruning for a valid n-ary tree.

Use command prompt to load prolog file by typing the following command.

## Syntax

```
swipl -s file_location
```

## Sample execution

```
swipl -s /Users/vishnuchalla/AI/Assignment3/a3q3.pl'
```

This will log you into the swipl command prompt

To perform alpha beta pruning a tree needs to created as shown in the code.

## Syntax

```
?- tree(Tree that needs to be created), alphabeta(Tree created as input, Result variable)
```

Output will be printed on the console. You can make use of sample tree mentioned in the testing section of a3q3.pl.
A additional tree also can be tested in the same process as mentioned in the testing section of a3q3.pl.

## Sample execution

```
?- tree1(T), alphabeta(T,V).
Leaf Value: 2
Leaf Value: 12
Min node Value: 2
Leaf Value: 6
Leaf Value: 10
Min node Value: 6
Max node Value: 6
Leaf Value: 8
Leaf Value: 19
Min node Value: 8
Max Node Value: 8
Beta Prune: [minimum([l(17),l(21)])]
Min node Value: 6
Leaf Value: 5
Min Node Value: 5
Alpha Prune: [l(4)]
Leaf Value: 15
Leaf Value: 9
Min node Value: 9
Max node Value: 9
Leaf Value: 12
Leaf Value: 16
Min node Value: 12
Max Node Value: 12
Beta Prune: [minimum([l(2),l(12)])]
Min node Value: 9
Max node Value: 9
T = maximum([minimum([maximum([minimum([l(2), l(...)]), minimum([l(...)|...])]), maximum([minimum([l(...)|...]), minimum([...|...])])]), minimum([maximum([minimum([l(...)|...]), minimum([...|...])]), maximum([minimum([...|...]), minimum(...)])])]),
V = 9 .
```
