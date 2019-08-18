% start - [[1,2,3,4,5,6,7,8,9,10],[],[]]
% goal - [[],[],[1,2,3,4,5,6,7,8,9,10]]

t(R):-
    solve([[1,2,3,4,5,6,7,8,9,10],[],[]],R).

%stack 1 to 2
s(Stacks,[Stack1,[Top1|Stack2]|Otherstacks]):-
    del([Top1|Stack1],Stacks,Stacks1),
    del(Stack2,Stacks1,Otherstacks).

%stack 1 to 3
s(Stacks,[Stack1,[NewTopOfStack2|Stack2]|Otherstacks]):-
    del([Top1|Stack1],Stacks,Stacks1),
    del([Top2|Stack2],Stacks1,Otherstacks),
    NewTopOfStack2 = [Top1|Top2],
    Top1 < Top2.

s([[Hcol1|Tcol1],[Hcol2|Tcol2]])







goal(Situation):-
    Situation = [[],[],[1,2,3,4,5,6,7,8,9,10]].


solve(Start,Solution):-
    Solution1=[],
    solver(Start,Solution1),
    Solution = Solution1.

% base case
% found goal. return start of Solution list
solver(Situation,Situation):-
    goal(Situation).


solver(Situation1,Solution):-
    s(Situation1,Situation2),
    solver(Situation2,Solution1),
    Solution = Solution1.

del(X,[X|L],L).

del(X, [Y,L], [Y|L1]):-
    del(X,L,L1).
