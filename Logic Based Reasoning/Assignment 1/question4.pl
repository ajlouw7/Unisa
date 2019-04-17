sum([],Result):-
  Result is 0.

sum([Head|Tail],Result):-
   sum(Tail,Result1),
   Result is Result1 + Head.
   
lenght([],0).

lenght([_|Tail],N):-
    lenght(Tail,N10,
    N is 1 + N1.
	
average(List,X) :-
   sum(List,Sum),
   length(List,Lenght),
   X is Sum/Lenght.
   