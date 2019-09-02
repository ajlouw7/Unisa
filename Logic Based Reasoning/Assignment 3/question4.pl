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
	s([[1,2,3,4,5,6,7,8,9,10],[2],[]],[[2,3,4,5,6,7,8,9,10],[1,2],[]]).

t1to3():-
	s([[2,4,5,6,7,8,9,10],[1],[3]],[[4,5,6,7,8,9,10],[1],[2,3]]).

t2to1():-
	s([[4,5,6,7,8,9,10],[1,2],[3]],[[4,5,6,7,8,9,10],[2],[1,3]]).
	
t2to3():-
	s([[4,5,6,7,8,9,10],[1,3],[2]],[[4,5,6,7,8,9,10],[3],[1,2]]).

t3to1():-
		s([[4,5,6,7,8,9,10],[],[1,2,3]],[[1,4,5,6,7,8,9,10],[],[2,3]]).

t3to2():-
		s([[4,5,6,7,8,9,10],[2],[1,3]],[[4,5,6,7,8,9,10],[1,2],[3]]).
	
%stack 1 to 2
s(Stacks,[TailStack1,[HeadStack1|Stack2]|Stack3]):-
    write("1-2"),
	write(Stacks),
    del([HeadStack1|TailStack1],Stacks,Last2Stacks),
    del(Stack2,Last2Stacks,Stack3),
    canAdd(HeadStack1,Stack2).

%stack 1 to 3
s(Stacks,[TailStack1,Stack2,[HeadStack1|OldStack3]]):-
    write("1-3"),
		write(Stacks),
    del([HeadStack1|TailStack1],Stacks,Last2Stacks),
    del(Stack2,Last2Stacks,[OldStack3]),
    canAdd(HeadStack1,OldStack3).

%stack 2 to 1
s(Stacks,[[HeadStack2|Stack1],TailStack2,Stack3]):-
    write("2-1"),
		write(Stacks),
	del(Stack1,Stacks,Last2Stacks),
	del([HeadStack2|TailStack2],Last2Stacks,Stack3),
	canAdd(HeadStack2,Stack1).
	
%stack 2 to 3
s(Stacks,[Stack1,TailStack2,[HeadStack2|OldStack3]]):-
	write("2-3"),
		write(Stacks),
	del(Stack1,Stacks,Last2Stacks),
	del([HeadStack2|TailStack2],Last2Stacks,[OldStack3]),
	canAdd(HeadStack2,OldStack3).

%stack 3 to 1
s(Stacks,[[HeadStack3|Stack1],Stack2|[TailStack3]]):-
	write("3-1"),
		write(Stacks),
	del(Stack1,Stacks,Last2Stacks),
	del(Stack2,Last2Stacks,[[HeadStack3|TailStack3]]),
	canAdd(HeadStack3,Stack1).

%stack 3 to 2
s(Stacks,[Stack1,[HeadStack3|Stack2]|[TailStack3]]):-
	write("3-2"),
		write(Stacks),
	del(Stack1,Stacks,Last2Stacks),
	del(Stack2,Last2Stacks,[[HeadStack3|TailStack3]]),
	canAdd(HeadStack3,Stack2).



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
