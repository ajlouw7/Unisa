test(L):-
app3_dl([1,2,3]-[3,4],[5,6,7]-[7,8,9], [10,11,12]-[11,12],L).

app3_dl(A1-A2,B1-B2,C1-C2,L).

remover(L1,L2,Result):-
   matchedPattern(L1,L2),!,
   true
   ;
   decide(L1,L2,Result)
   . 
 
decide([H1|L1],L2,Result):-
   [H1|L1] == [],!,
   Result = []
   ; 
   remover(L1,L2,Result),
   Result is [H1|Result].


matchedPattern([],[]).

matchedPattern(_,[]) :-
   fail.

matchedPattern([H1|L1],[H2|L2]):-
     H1 == H2,!,
     matchedPattern(L1,L2)
     ;
     fail. 
  
test2(L) :-
  remover([1,2,3],[3,5],L).








