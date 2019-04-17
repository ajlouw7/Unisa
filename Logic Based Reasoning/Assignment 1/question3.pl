student('Quinton','Duminy',male,12,[soccer,hockey,cricket]).
student('Vusi','Dlamini',male,10,[rugby,cricket]).
student('Fiona','Dolman',female,10,[hockey]).
student('John','Barnaby',male,8,[hockey,soccer]).
student('Precious','Zulu',12,female,[soccer,cricket]).

gender(Name,Surname,Gender):- 
  student(Name,Surname,Gender,_,_).
  
grade(Name,Surname,Grade):- 
  student(Name,Surname,_,Grade,_).

sports(Name,Surname,Sports):- 
  student(Name,Surname,_,_,Sports).

playingSport(Name,Surname,Sport):-
  student(Name,Surname,_,_,SportList),
  member(Sport,SportList).
   
