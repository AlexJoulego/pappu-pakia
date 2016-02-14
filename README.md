# pappu-pakia


An attempt to implement the Pappu-Pakia game in Python/Pygame.

## Python Implementation
This game (Pappu Pakia) has been made for [Github Game Off 2012](https://github.com/blog/1303-github-game-off) using all that modern stuff with HTML5 (esp. Canvas methods) and JavaScript. I tried to implement it
in Python using a bit of Pygame framework (but not all the power of that framework, e.g. I did not use
collide methods from there, rather implemented it similar to the authors' way) just for an exercise. 
I'm a linguist, a former school teacher, who wants to become a software developer and does everything possible to achieve his goals. Sure, the OO design is awful here, but I'm just beginning!

## About
You are pappu in the game, that small character. You need to click the mouse or press the Up key
to levitate, otherwise the pappu will descend. If he hits the top or bottom boundaries,
that'll end the game.

There will be some obstacles along the way like forks, branches and some enemies, aka "pakias".
Hitting them will end the game. There are 3 types of pakias: sad (pull you),
happy (push you), angry (kill you) /not implemented yet/.
Keep safe distance from them!

There are some collectibles, too! Coins for points (50, 100, 500, and 1000).
Apples for invincibility for a short period.
Berries spawning clones that'll destroy anything that comes in their way!

If the collectibles are found to be over forks or branches
then that's not a bug. The authors did that deliberately to help you
test your greed level.

Collisions are not super strict to make the gameplay a bit easier.

## Credits
Handsomely coded in JavaScript by [Rishabh](http://twitter.com/_rishabhp).
Beautiful graphics by [Kushagra](http://twitter.com/solitarydesigns).
Music by [Rezoner](http://rezoner.net). All other sounds produced by the authors' personal things
like mouths, hands and books.

Implemented in Python by [Alexander Joulego](http://twitter.com/alex_joulgo)

[Code in Javascript](http://github.com/mind-it/game-off-2012)

