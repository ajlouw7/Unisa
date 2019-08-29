% start - [[1,2,3,4,5,6,7,8,9,10],[],[]]
% goal - [[],[],[1,2,3,4,5,6,7,8,9,10]]

t(R):-
    solve([[1,2,3,4,5,6,7,8,9,10],[],[]],R).

% can always add to empty stack
canAdd(_,[]).

% can add to stack if item is smaller than head of stack
canAdd(A,[H|_]):-
  A < H.

t1to2():-
	s([[1,2,3,4,5,6,7,8,9,10],[],[]],[[2,3,4,5,6,7,8,9,10],[1],[]]).

t1to3():-
	s([[1,2,3,4,5,6,7,8,9,10],[],[]],[[2,3,4,5,6,7,8,9,10],[],[1]]).




%stack 1 to 2
s(Stacks,[TailStack1,[HeadStack1|Stack2]|Stack3]):-
    del([HeadStack1|TailStack1],Stacks,Last2Stacks),
    del(Stack2,Last2Stacks,Stack3),
    canAdd(HeadStack1,Stack2).

%stack 1 to 3
s(Stacks,[TailStack1,Stack2,[HeadStack1|OldStack3]]):-
    del([HeadStack1|TailStack1],Stacks,Last2Stacks),
    del(Stack2,Last2Stacks,[OldStack3]),
    canAdd(HeadStack1,OldStack3).

%stack 2 to 3
s(Stacks,[Stack1,TailStack2,[HeadStack2|OldStack3]]):-
	del






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
