hanoi(1,Source,Temp,Dest):-
    write('Move disk 1 from '),
    write(Source),
    write(' to '),
    write(Dest), nl.

hanoi(N,Source,Temp,Dest):-
    N>1,
    M is N-1,
    hanoi(M,Source,Dest,Temp),
    write('Move disk '),
    write(N),
    write(' from '),
    write(Source),
    write(' to '),
    write(Dest), nl,
    hanoi(M,Temp,Source,Dest).