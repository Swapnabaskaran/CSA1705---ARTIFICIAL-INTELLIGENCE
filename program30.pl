bird(parrot).
has_wings(parrot).

flies(X) :-
    bird(X),
    has_wings(X).