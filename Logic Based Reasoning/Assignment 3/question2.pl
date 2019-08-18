%remove one object from list. In case there are duplicates
deleteFirst(_,[],[]).
deleteFirst(O,[O|T],T).
deleteFirst(O,[H|T],[H|R]):-
    deleteFirst(O,T,R).

getPermutation([H|T],R):-
    getPermutation(T,R1),
    deleteFirst(H,R,R1).

getPermutation([],[]).

knapsack(Objects_Available,Target_weight,Objects_included):-
    getPermutation(Objects_Available,Objects_included),
    isValidSolution(Objects_included,Target_weight).

isValidSolution(Objects,Size):-
    sum_list(Objects,Sum),
    Sum == Size.







