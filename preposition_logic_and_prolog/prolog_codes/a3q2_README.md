The a3q2.pl contains all the rules and functions to perform queries on the prolog knowledge base.

Use command prompt to load prolog file by typing the following command.

## Syntax

```
swipl -s file_location
```

## Sample execution

```
swipl -s /Users/vishnuchalla/AI/Assignment3/a3q2.pl'
```

This will log you into the swipl command prompt

To perform queries on properties and the type of vehicles.

# Property:

## Syntax

```
?- property(property of the vehicle, vehicle, X).
```

Output will be printed on the console.

## Sample execution

```
?- property(fuel, car, X).
X = gasoline ;
X = gasoline ;
false.

?- property(wheels, car, X).
X = 4 ;
false.
```

# Type:

## Syntax

```
?- type(vehicle name, X).
```

Output will be printed on the console.

## Sample execution

```
?- type(flx_drive, X).
X = train ;
X = land_vehicles ;
X = vehicle ;
false.

?- type(peral, X).
X = aquatic_vehicles ;
X = vehicle ;
false.
```
