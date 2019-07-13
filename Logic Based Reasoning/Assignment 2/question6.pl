even(X) :- 0 is mod(X, 2).
odd(X) :- 1 is mod(X, 2).


rm(0,_,Total):- 
	Total is 0.

rm(X,Y,Total):-
	even(X),!,
	X1 is X/2,
        Y2 is Y*2,
        rm( X1, Y2, T1),
        Total is T1  
	;
        X1 is (X-1)/2,
        Y2 is Y*2,
        rm(X1, Y2, T1),
	Total is T1 + Y
	.
