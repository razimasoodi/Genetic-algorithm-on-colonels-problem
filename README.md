# Genetic-algorithm-on-colonels-problem
This project is an abstract war game that generalizes to many situations involving competing strategies of resource distribution. In the military context, it goes as follows:
Each colonel has a limited number of soldiers, S, and a fixed number of battles, B, to be fought during a war (against one opposing colonel). In each battle, the commander who shows up with the most troops wins, and the commander who wins the majority of the B battles wins the war. The colonel’s job is to decided, prior to the first battle, the distribution of troops for all the battles.
Your task here is to implement the genetic algorithm (GA) to evolve the colonels’ strategies.
A representation for each strategy is simply a list of B non-negative integers (that sum to S).
Each strategy will compete (i.e., have a war) with every other strategy in the population. Each war win is worth 2 points, and each tie is worth 1; losses are worth 0. Fitness should be directly based on the total number of war points. The degree of battle victory does not count, only the binary act of winning or losing.
Use the following parameters in the default implementation:
 Random initialization
 Population size: 50
 Tournament selection
 10 % elitism.
Colonel
Battle 1
Battle 2
Battle 3
Battle 4
A
8
1
6
5
B
9
1
0
10
C
6
6
4
4
