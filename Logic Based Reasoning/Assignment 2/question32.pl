dog('Sasha','Beagle','Nadia').
dog('Zappa','Labrador','Sjanie').
dog('Domino','Dalmation','Peter').
dog('Daisy','Boxer','John').
dog('Ben','Ridgeback','Ben').
breed('Beagles','Medium','Hunting').
breed('Basset','','Hunting').
breed('Labrador','Large','GuideDog').
breed('GermanShephard','','GaurdDog').

breeds(L):-
	setof(B,Size^Job^breed(B,Size,Job),L).


count_hunt(L,N):-
	findall(B,breed(B,_,'Hunting'),L),
        length(L,N).

sizes(N):-
	setof(Size,B^J^breed(B,Size,J),L),
        length(L,N).


calcIntersection([],_,L):-
L =[].

calcIntersection([H1|A],B,L):-
	findall(H1,member(H1,B),Temp),
        length(Temp ,N),
        N\=0,!,
        symmetric_difference(A,B,L1),
	append(Temp,L1,L)
        ;
        symmetric_difference(A,B,L1), 
        L= L1
        .

mergeIfNotInIntersection(A,I,L).
	


symmetric_difference(A,B,L):-
      calcIntersection(A,B,Intersection),
      mergeIfNotInIntersection(A,Intersection,L).

