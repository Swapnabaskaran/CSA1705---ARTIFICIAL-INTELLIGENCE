fact(bird).
fact(has_wings).

rule(flies) :-
    fact(bird),
    fact(has_wings).

forward :-
    rule(X),
    write('Derived Fact: '),
    write(X).