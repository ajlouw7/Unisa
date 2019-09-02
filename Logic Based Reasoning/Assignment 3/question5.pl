quicksort([],[]).
	
quicksort([X|Tail],Sorted):-
	split( X, Tail, Small, Big ),
	quicksort(Small,SortedSmall),
	quicksort(Big,SortedBig),
	conc( SortedSmall, [X|SortedBig],Sorted).
	
split( _ , [],[],[]).

split( X,[Y|Tail],Small,Big):-
	X = Y,!,
	split(X,Tail, Small, Big).
	

split(X,[Y|Tail],[Y|Small],Big):-
	X>Y,!,
	split(X,Tail, Small, Big).
	
split(X,[Y|Tail],Small,[Y|Big]):-
	split(X,Tail,Small,Big).


test(L):-
	quicksort([2,5,9,2,5,8,10],L).
	
conc( [], X, X).                                  
conc( [X | Y], Z, [X | W]) :- conc( Y, Z, W). 

sameAsNext(_,[]):-
	fail.
	
sameAsNext(S,[H|_]) :-
	S = H.

removeDuplicate([],[]).


removeDuplicate([H|T],R):-
	sameAsNext(H,T),!,
	removeDuplicate( T, R1 ),
	R = R1
	;
	removeDuplicate( T, R1 ),
	R = [H|R1].
