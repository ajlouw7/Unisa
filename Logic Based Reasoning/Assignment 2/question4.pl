paint(shadows).
clay_bank(colorado).

roan(blue_lightning).
roan(X):-
not(paint(X)),
	not(clay_bank(X)). 