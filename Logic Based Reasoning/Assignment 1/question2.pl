exp(B,0,1).
exp(0,E,0).
exp(B,E,R):-
  E1 is E - 1,
  exp(B,E1,R1),
  R is R1 * B.