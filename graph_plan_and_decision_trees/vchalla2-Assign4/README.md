The GraphPlan.java contains code to generate a graph plan for a given PDDL and extract a plan from it.

Use command prompt to compile the given java file and execute as below.

## Syntax

```
javac GraphPlan.java
java GraphPlan file_location
```

## Sample execution

```
javac GraphPlan.java
java GraphPlan Problem.txt
```

This will execute the given program and will log the output on the screen.

## Output

```
Creating Layer = A1
Adding Actions:
[persist(-Dinner), persist(CleanPan), persist(-FriedEggs), Fry, persist(-BoiledVegetables), Boil]

Next States:
[-FriedEggs, -Dinner, CleanPan, -BoiledVegetables, -CleanPan, BoiledVegetables, FriedEggs]

Mutex Type IE Found:[(persist(CleanPan),Boil), (persist(-FriedEggs),Fry), (persist(-BoiledVegetables),Boil), (persist(CleanPan),Fry)]

Mutex Type I Found:[(Fry,Boil), (persist(CleanPan),Boil), (persist(-FriedEggs),Fry), (persist(-BoiledVegetables),Boil), (persist(CleanPan),Fry)]

Mutex Type NL Found:[(-FriedEggs,FriedEggs), (-BoiledVegetables,BoiledVegetables), (CleanPan,-CleanPan)]

Mutex Type IS Found:[(CleanPan,FriedEggs), (BoiledVegetables,FriedEggs), (CleanPan,BoiledVegetables)]

Creating Layer = A2
Adding Actions:
[persist(-Dinner), persist(CleanPan), persist(-FriedEggs), persist(BoiledVegetables), Wash, persist(-CleanPan), Fry, persist(-BoiledVegetables), Boil, persist(FriedEggs)]

Next States:
[-FriedEggs, -Dinner, CleanPan, -BoiledVegetables, -CleanPan, BoiledVegetables, FriedEggs]

Mutex Type CN Found:[(persist(CleanPan),Wash), (persist(BoiledVegetables),persist(FriedEggs)), (persist(-CleanPan),Boil), (persist(CleanPan),persist(FriedEggs)), (persist(-CleanPan),Fry), (Wash,Fry), (persist(BoiledVegetables),Boil), (persist(-FriedEggs),persist(FriedEggs)), (Boil,persist(FriedEggs)), (persist(CleanPan),persist(-CleanPan)), (Fry,persist(FriedEggs)), (persist(BoiledVegetables),Fry), (Wash,Boil), (persist(BoiledVegetables),persist(-BoiledVegetables)), (persist(CleanPan),persist(BoiledVegetables))]

Mutex Type IE Found:[(persist(-FriedEggs),persist(FriedEggs)), (persist(CleanPan),persist(-CleanPan)), (persist(CleanPan),Boil), (persist(-FriedEggs),Fry), (persist(-BoiledVegetables),Boil), (Wash,persist(-CleanPan)), (Wash,Boil), (persist(BoiledVegetables),persist(-BoiledVegetables)), (persist(CleanPan),Fry), (Wash,Fry)]

Mutex Type I Found:[(persist(CleanPan),Wash), (persist(CleanPan),Boil), (persist(-BoiledVegetables),Boil), (persist(-CleanPan),Boil), (persist(-CleanPan),Fry), (persist(CleanPan),Fry), (persist(BoiledVegetables),Boil), (Fry,Boil), (persist(-FriedEggs),persist(FriedEggs)), (persist(CleanPan),persist(-CleanPan)), (Fry,persist(FriedEggs)), (persist(-FriedEggs),Fry), (Wash,persist(-CleanPan)), (persist(BoiledVegetables),persist(-BoiledVegetables))]

Mutex Type NL Found:[(-FriedEggs,FriedEggs), (-BoiledVegetables,BoiledVegetables), (CleanPan,-CleanPan)]

Mutex Type IS Found:[(BoiledVegetables,FriedEggs)]

Creating Layer = A3
Adding Actions:
[persist(-Dinner), persist(CleanPan), persist(-FriedEggs), persist(BoiledVegetables), Wash, persist(-CleanPan), Fry, persist(-BoiledVegetables), Boil, persist(FriedEggs)]

Next States:
[-FriedEggs, -Dinner, CleanPan, -BoiledVegetables, -CleanPan, BoiledVegetables, FriedEggs]

Mutex Type CN Found:[(persist(BoiledVegetables),Boil), (persist(CleanPan),Wash), (persist(-FriedEggs),persist(FriedEggs)), (persist(CleanPan),persist(-CleanPan)), (Fry,persist(FriedEggs)), (persist(BoiledVegetables),persist(FriedEggs)), (Wash,Boil), (persist(-CleanPan),Boil), (persist(BoiledVegetables),persist(-BoiledVegetables)), (persist(-CleanPan),Fry), (Wash,Fry)]

Mutex Type IE Found:[(persist(-FriedEggs),persist(FriedEggs)), (persist(CleanPan),persist(-CleanPan)), (persist(CleanPan),Boil), (persist(-FriedEggs),Fry), (persist(-BoiledVegetables),Boil), (Wash,persist(-CleanPan)), (Wash,Boil), (persist(BoiledVegetables),persist(-BoiledVegetables)), (persist(CleanPan),Fry), (Wash,Fry)]

Mutex Type I Found:[(persist(CleanPan),Wash), (persist(CleanPan),Boil), (persist(-BoiledVegetables),Boil), (persist(-CleanPan),Boil), (persist(-CleanPan),Fry), (persist(CleanPan),Fry), (persist(BoiledVegetables),Boil), (Fry,Boil), (persist(-FriedEggs),persist(FriedEggs)), (persist(CleanPan),persist(-CleanPan)), (Fry,persist(FriedEggs)), (persist(-FriedEggs),Fry), (Wash,persist(-CleanPan)), (persist(BoiledVegetables),persist(-BoiledVegetables))]

Mutex Type NL Found:[(-FriedEggs,FriedEggs), (-BoiledVegetables,BoiledVegetables), (CleanPan,-CleanPan)]

Creating Layer = A4
Adding Actions:
[persist(-Dinner), persist(CleanPan), persist(-FriedEggs), persist(BoiledVegetables), Wash, persist(-CleanPan), Fry, persist(-BoiledVegetables), Mix, Boil, persist(FriedEggs)]

Next States:
[-FriedEggs, -Dinner, Dinner, CleanPan, -BoiledVegetables, -CleanPan, BoiledVegetables, FriedEggs]

Mutex Type CN Found:[(persist(CleanPan),Wash), (persist(-FriedEggs),Mix), (Fry,Mix), (persist(-BoiledVegetables),Mix), (persist(-CleanPan),Boil), (persist(-CleanPan),Fry), (Wash,Fry), (persist(BoiledVegetables),Boil), (persist(-FriedEggs),persist(FriedEggs)), (persist(CleanPan),persist(-CleanPan)), (Fry,persist(FriedEggs)), (Wash,Boil), (Mix,Boil), (persist(BoiledVegetables),persist(-BoiledVegetables))]

Mutex Type IE Found:[(persist(-Dinner),Mix), (persist(-FriedEggs),persist(FriedEggs)), (persist(CleanPan),persist(-CleanPan)), (persist(CleanPan),Boil), (persist(-FriedEggs),Fry), (persist(-BoiledVegetables),Boil), (Wash,persist(-CleanPan)), (Wash,Boil), (persist(BoiledVegetables),persist(-BoiledVegetables)), (persist(CleanPan),Fry), (Wash,Fry)]

Mutex Type I Found:[(persist(CleanPan),Wash), (persist(CleanPan),Boil), (persist(-FriedEggs),Mix), (persist(-BoiledVegetables),Mix), (persist(-BoiledVegetables),Boil), (persist(-CleanPan),Boil), (persist(-CleanPan),Fry), (persist(CleanPan),Fry), (persist(-Dinner),Mix), (persist(BoiledVegetables),Boil), (Fry,Boil), (persist(-FriedEggs),persist(FriedEggs)), (persist(CleanPan),persist(-CleanPan)), (Fry,persist(FriedEggs)), (persist(-FriedEggs),Fry), (Wash,persist(-CleanPan)), (persist(BoiledVegetables),persist(-BoiledVegetables))]

Mutex Type NL Found:[(-FriedEggs,FriedEggs), (-BoiledVegetables,BoiledVegetables), (-Dinner,Dinner), (CleanPan,-CleanPan)]

Mutex Type IS Found:[(Dinner,-BoiledVegetables), (-FriedEggs,Dinner)]


Plan Extract:
[(persist(-BoiledVegetables), Fry), (Wash, persist(-BoiledVegetables), persist(FriedEggs)), (Boil, persist(FriedEggs)), (persist(BoiledVegetables), persist(-CleanPan), Mix, persist(FriedEggs))]
```
