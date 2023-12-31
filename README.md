<p align="center">
  <img src="https://github.com/ScruffyTheMoose/cellularAutomata/blob/main/Diamoeba.gif" alt="animated" />
</p>

This is an in-progress project where I am developing and testing different Cellular Automata rulesets. We use PyGame as the engine where to render and run the rulesets which allows us to see how different initialization patterns evolve for each time-step. The world is a 2-dimensional array of cells. Every cell is either alive or dead, and this state depends on the states of the surrounding cells.

The most common ruleset is known as "Conway's Game of Life" which is annotated in the typical format as B3/S23. This notation means that a cell will be "Born" if 3 surrounding cells are alive, and a cell will "Survive" if either 2 or 3 surrounding cells are alive. Any other cases result in the cell's state becoming dead.

<p align="center">
  <img src="https://github.com/ScruffyTheMoose/cellularAutomata/blob/main/Life.gif" alt="animated" />
</p>

There are numerous different rulesets which can be applied. The world is a 2-d binary array which is, by necessity, finite. However, even a small world has an extremely large number of permutations. For example, a world with a shape (10, 10) would have 2<sup>100</sup> potential initialization states.

At the moment, the current algorithm which updates the world allows for the use of any 2-d Bx/Sy ruleset. My goal is to use this same system to explore how similar automata may evolve with simple evolutionary neural networks. 
