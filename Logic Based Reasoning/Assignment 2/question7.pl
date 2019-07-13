m(a).
m(b).
n(a,1).
n(a,2).
n(b,3).
n(b,4).
q(1,1).
q(1,2).
q(2,3).
q(2,4).
q(3,5).
q(3,6).
q(4,7).
q(4,8).

q1(X,Y,Z):-
	m(X),n(X,Y),!,q(Y,Z).

q2(X,Y,Z):-
	m(X),once(n(X,Y)),q(Y,Z).

q3(X,Y):- 
	m(X),!,n(X,Y).

q4(X,Y,L):-
	bagof(X,(m(X),X=a,n(X,Y)),L).

q5(X,Y,L):-
	setof(X,Y^q(X,Y),L).