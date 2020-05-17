# carcassonne
Carcassonne implementation in python

![Example game](https://github.com/wingedsheep/carcassonne/blob/master/example_game.gif)

## API (work in progress)

Code example for a game with two players

    import random  
    from typing import Optional  
      
    from main.carcassonne_game import CarcassonneGame  
    from main.objects.actions.action import Action  
    from main.tile_sets.tile_sets import TileSet  
      
    game = CarcassonneGame(  
        players=2,  
        tile_sets=[TileSet.BASE, TileSet.THE_RIVER, TileSet.INNS_AND_CATHEDRALS]  
    )  
      
    while not game.is_finished():  
        player: int = game.state.current_player  
        valid_actions: [Action] = game.get_possible_actions()  
        action: Optional[Action] = random.choice(valid_actions)  
        if action is not None:  
            game.step(player, action)  
        game.render()
