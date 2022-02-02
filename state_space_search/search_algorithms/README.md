The zip file contains implementation of all the 3 algorithms DFS, BFS and Astar.

Here is the demonstration on how to trigger the code for each algorithm.

# DFS:

## Syntax

```
python3 mazes_dfs.py <inputFile>
```

Output file will be generated with and extension of "-solution-dfs-vchalla2.txt" to the input file name

## Sample execution

```
python3 mazes_dfs.py 4x4Maze-maze.txt

STDOUT
Intermediate states expanded: [(0, 0), (2, 0), (1, 0), (1, 2), (3, 2), (3, 0), (3, 3), (2, 3), (2, 1), (1, 1), (0, 1), (3, 1)]
Total number of intermediate states expanded: 12
```

Output file will be generated as "4x4Maze-maze-solution-dfs-vchalla2.txt"

```
cat 4x4Maze-maze-solution-dfs-vchalla2.txt for verifying the output.
```

# DFS Brute Force (Specific to 6x6 mazes):

## Syntax

```
python3 mazes_dfs_bruteforce.py <inputFile>
```

Output file will be generated with and extension of "-solution-dfs-brute-force-vchalla2.txt" to the input file name

## Sample execution

```
python3 mazes_dfs_bruteforce.py 6x6Maze.txt

STDOUT
Total unique paths:
[[(0, 0), (5, 0), (3, 0), (3, 3), (0, 3), (2, 3), (2, 5), (4, 5), (4, 1), (1, 1), (1, 4), (3, 4), (5, 4), (2, 4), (2, 0), (1, 0), (1, 3), (5, 3), (5, 5)], [(0, 0), (5, 0), (5, 2), (0, 2), (3, 2), (3, 3), (0, 3), (2, 3), (2, 5), (4, 5), (4, 1), (1, 1), (1, 4), (3, 4), (5, 4), (2, 4), (2, 0), (1, 0), (1, 3), (5, 3), (5, 5)], [(0, 0), (0, 5), (4, 5), (4, 1), (1, 1), (1, 4), (3, 4), (5, 4), (2, 4), (2, 0), (1, 0), (1, 3), (5, 3), (5, 5)], [(0, 0), (5, 0), (3, 0), (3, 3), (0, 3), (0, 1), (3, 1), (3, 5), (3, 2), (2, 2), (2, 1), (2, 5), (4, 5), (4, 1), (1, 1), (1, 4), (3, 4), (5, 4), (2, 4), (2, 0), (1, 0), (1, 3), (5, 3), (5, 5)]]
And their corresponding states with expansion count:
['[(0, 0), (5, 0), (3, 0), (3, 3), (0, 3), (2, 3), (4, 3), (2, 5), (4, 5), (4, 1), (1, 1), (1, 4), (3, 4), (5, 4), (2, 4), (2, 0), (1, 0), (4, 0), (1, 3), (5, 3), (5, 5)]:21', '[(0, 0), (5, 0), (5, 2), (0, 2), (3, 2), (4, 2), (4, 4), (0, 4), (4, 0), (3, 3), (0, 3), (2, 3), (4, 3), (2, 5), (4, 5), (4, 1), (1, 1), (1, 4), (3, 4), (5, 4), (2, 4), (2, 0), (1, 0), (1, 3), (5, 3), (5, 5)]:26', '[(0, 0), (0, 5), (4, 5), (4, 1), (4, 4), (0, 4), (4, 0), (1, 1), (1, 4), (3, 4), (5, 4), (2, 4), (2, 0), (2, 1), (2, 5), (2, 3), (4, 3), (0, 3), (3, 0), (3, 3), (1, 0), (1, 3), (5, 3), (5, 5)]:24', '[(0, 0), (5, 0), (3, 0), (3, 3), (0, 3), (0, 1), (3, 1), (3, 5), (3, 2), (4, 2), (4, 0), (4, 4), (2, 2), (2, 1), (2, 5), (4, 5), (4, 1), (1, 1), (1, 4), (3, 4), (5, 4), (5, 1), (2, 4), (2, 0), (1, 0), (1, 3), (5, 3), (5, 5)]:28']
Total number of unique paths: 4
Total number of intermediate states expanded: 99
```

Total unique paths is the total number of unique paths in the given 6x6 maze.
And their corresponding states with expansion count indicates the total number states expanded for each unique path one-one mapped and the expanded nodes count.

Output file will be generated as "6x6Maze-solution-dfs-brute-force-vchalla2.txt". The output file contains the path with minimum cost among all the possibilities.

```
cat 6x6Maze-solution-dfs-brute-force-vchalla2.txt for verifying the output.
```

# BFS:

## Syntax

```
python3 mazes_bfs.py <inputFile>
```

Output file will be generated with and extension of "-solution-bfs-vchalla2.txt" to the input file name

## Sample execution

```
python3 mazes_bfs.py 4x4Maze-maze.txt

STDOUT
Intermediate states expanded: [(0, 0), (2, 0), (2, 1), (3, 1)]
Total number of intermediate states expanded: 4
```

Output file will be generated as "4x4Maze-maze-solution-bfs-vchalla2.txt"

```
cat 4x4Maze-maze-solution-bfs-vchalla2.txt for verifying the output.
```

# AStar:

## Syntax

```
python3 mazes_aStar.py <inputFile>
```

Output file will be generated with and extension of "-solution-aStar-vchalla2.txt" to the input file name

## Sample execution

```
python3 mazes_aStar.py 4x4Maze-maze.txt

STDOUT
Intermediate states expanded: [(0, 0), (2, 0), (2, 1), (3, 0), (3, 1)]
Total number of intermediate states expanded: 5
```

Output file will be generated as "4x4Maze-maze-solution-aStar-vchalla2.txt"

```
cat 4x4Maze-maze-solution-aStar-vchalla2.txt for verifying the output.
```
