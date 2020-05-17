# carcassonne
Carcassonne implementation in python

![Example game](https://github.com/wingedsheep/carcassonne/blob/master/example_game.gif)

## API (work in progress)

The following is how it is supposed to work once the code is finished. 

Code example for a game with two players

    carcassonne_game = CarcassonneGame(
	    players=2, 
	    tile_sets=[TileSets.BASE, TileSets.THE_RIVER, TileSets.INNS_AND_CATHEDRALS]
	)
	
	while not game.finished():
		player: int = carcassonne_game.state.current_player
		valid_actions: [Action] = carcassonne_game.get_possible_actions()
		action: Optional[Action] = # Choose an action
		if action is not None:
			carcassonne_game.play(player, action)
