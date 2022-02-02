The NeuralModel.py and NeuralModel_v2.py contains code to create and test a neural model on training and testing data

Use command prompt to compile the given python files and execute as below.

# NeuralModel.py

## Syntax

```
python3 NeuralModel.py <ALPHA> <TRAIN> <TEST>
```

## Sample execution

```
python3 NeuralModel.py 0.98 TrainFile.txt TestFile.txt
```

This will execute the given program and will log the output on the screen.

## Output

```
Train: Predicted Value=1.8134934084949248 Actual Value=0.41341848475658705
Train: Predicted Value=92.64200076398367 Actual Value=0.8465847262607703
.
.
.
Final Performance Of Trained Data:- 7234.213213
Test: Predicted Value=4.051583855055719 Actual Value=0.8559680325383092
Test: Predicted Value=3.2387536780860646 Actual Value=0.4330235296216351
.
.
.
Final Performance Of Tested Data:- 2073501.7449564135
```

# NeuralModel_v2.py

## Syntax

```
python3 NeuralModel_v2.py <ALPHA> <TRAIN> <TEST>
```

## Sample execution

```
python3 NeuralModel_v2.py 0.98 TrainFile.txt TestFile.txt
```

This will execute the given program and will log the output on the screen.

## Output

```
Train: Predicted Value=1.8134934084949248 Actual Value=0.41341848475658705
Train: Predicted Value=-92.64200076398367 Actual Value=0.8465847262607703
.
.
.
Final Performance Of Trained Data:- 12331.213213
Test: Predicted Value=-4.051583855055719 Actual Value=0.8559680325383092
Test: Predicted Value=-3.2387536780860646 Actual Value=0.4330235296216351
.
.
.
Final Performance Of Tested Data:- 12131241.7449564135
```
