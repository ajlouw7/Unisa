interleave([],[],[]).

interleave([H1|T1],[H2|T2],Result):-
   interleave(T1,T2,Result1),
   Result = [[H1|H2]|Result1].


 