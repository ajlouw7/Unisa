powers_two(0,1).

powers_two(N,R):-
    N1 is N - 1,
    powers_two(N1,R1),
    R is R1 * 2.


