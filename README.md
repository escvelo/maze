# Maze Pioneer
We assume that maze is divided up into “squares.” Each square is either free or occupied by obstacle. We could only pass through the free spaces. If we bump into obstacle we must try different direction. Given the start position in the Maze the algorithm must find the way out to exit. Exit is defined by outside edge not occupied by the wall.

We employ following procedure to find the exist:
  1) From start position we try going one step to NORTH and recursively repeat the procedure.
  2) If we fail to find the path going NORTH, we try to find by going one step to SOUTH and recursively repeat procesure.
  3) If we fail going NORTH and SOUTH we try WEST and EAST, each one followed by recursive calls as above.
  4) If none of these directions works then we fail to find the path.
  
 # Requirement
 Python 3.7.* and higher. Additionally we need `numpy` library which could installed using 
 `pip install numpy`
 
 # Execution
 Follow the steps mentioned in Google Colab link (https://colab.research.google.com/drive/1_mAt_vAGv1JGgx_TslVqcm0hUaWX1WOv?usp=sharing) 
 to run the `main.py` script 

 ```Shell commands
 git clone https://github.com/escvelo/maze.git
 cd ./maze/
 python main.py ./maze1.txt
 ```
 The data file `maze1.txt` contains following example of `6 x 5` maze:
 ```
 XOXXXX
 XOXOOX
 XOXOXX
 XOOOSX
 XXXXXX
 ```
 where 'S' denotes starting position, 'X' denotes obstacle and 'O' denotes free space.
 
 The output is printed on the console. It prints below list.
 ```
 [['X' '+' 'X' 'X' 'X' 'X']
  ['X' '+' 'X' '-' '-' 'X']
  ['X' '+' 'X' '-' 'X' 'X']
  ['X' '+' '+' '+' '+' 'X']
  ['X' 'X' 'X' 'X' 'X' 'X']]
 ```
 where '+' denotes the solution path to exit.
 
 # Optional bonus questions
 
 ## Find the shortest path ?
   We could use breadth first search algorithm. When there are multiple paths from start to exit, we could keep track of distance via each path. We could traceback from destination to start that has shortest distance recorded.
   
 ## Find all paths
 We could do this using backtracking. After reaching destination we could assign a unique id to the solution path.
 
 ## Optimise algorithm to find any path as quickly as possible.
 We could use A* algorithm. Because it has property of completeness and optimality. By optimality it finds best possible solution.
 
 ## Expand to 3 dimensional mazes.
 This has 3 degrees of freedom. Hence using naive recusive approach is computationally intensive. We could use A* 
 
 
 
 

