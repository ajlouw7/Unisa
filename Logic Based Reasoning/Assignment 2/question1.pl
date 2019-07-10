split([],_,L1,L2):-
L1 = [], L2 =[].

split([H|L],N,L1,L2):-
H>= N,!,
split(L,N,L1temp,L2temp),
L1 = [H|L1temp],
L2 = L2temp          
;
split(L,N,L1temp,L2temp),
L1 = L1temp,
L2 = [H|L2temp].



