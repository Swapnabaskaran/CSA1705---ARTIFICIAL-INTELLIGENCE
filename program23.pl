parent(ram, ravi).
parent(ram, priya).
parent(sita, ravi).
parent(sita, priya).

male(ram).
male(ravi).

female(sita).
female(priya).

father(X,Y) :- parent(X,Y), male(X).
mother(X,Y) :- parent(X,Y), female(X).