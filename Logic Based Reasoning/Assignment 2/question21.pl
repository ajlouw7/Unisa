fun(X,Y):-
	number(X),
	Y is X^3.

filter([],_,R):-
R = [].


filter([H|L],PredName,R):-
filter(L,PredName,R1),
F =.. [PredName,H,Result],
call(F),
R = [Result|R1].


apply([],_,R):-
R = [].

apply([H|L],PredName,R):-
apply(L,PredName,R1),
F =.. [PredName,H,Result],
call(F),
R = [Result|R1].


