powers_two(N,R):-
    powers_two(N,1,R).

powers_two(0,R,R).

powers_two(N,P,R):-
    P1 is P * 2,
    N1 is N - 1,
    powers_two(N1,P1,R).