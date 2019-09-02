quicksort(K,Sorted):-
	quicksortMod(K,Sorted1),
	removeDuplicate(Sorted1,Sorted).

quicksortMod([],[]).
	
quicksortMod([X|Tail],Sorted):-
	split( X, Tail, Small, Big ),
	quicksortMod(Small,SortedSmall),
	quicksortMod(Big,SortedBig),
	conc( SortedSmall, [X|SortedBig],Sorted).
	
split( X , [],[],[]).

split(X,[Y|Tail],[Y|Small],Big):-
	X>Y,!,
	split(X,Tail, Small, Big).
	
split(X,[Y|Tail],Small,[Y|Big]):-
	split(X,Tail,Small,Big).


test(L):-
	quicksortMod([2,5,9,2,5,8,10],L).
	
conc( [], X, X).                                  
conc( [X | Y], Z, [X | W]) :- conc( Y, Z, W). 

sameAsNext(_,[]):-
	fail.
	
sameAsNext(S,[H|T]) :-
	S = H.

removeDuplicate([],[]).


removeDuplicate([H|T],R):-
	sameAsNext(H,T),!,
	removeDuplicate( T, R1 ),
	R = R1
	;
	removeDuplicate( T, R1 ),
	R = [H|R1].
