inner_prod([],[],Result):-
Result is 0.

inner_prod([H1|T1],[H2|T2],Result):-
   inner_prod(T1,T2,Result1),
   Result is (H1*H2) + Result1.


 