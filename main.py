
import numpy as np
from custom_types import Point2D
import matplotlib.pyplot as plt 
from enum import Enum

START_POS = "S"
OBSTACLE = "X"
SOLUTION_PATH = "+"
TRIED = "."
DEAD_END = "-"            
class Path:
  Found = True

class Maze:
  def __init__(self, filename):
    self.maze_mat = []
    fh = open(filename, 'r')
    for line in fh:
      self.maze_mat.append([char for char in line.strip()])
    self.maze_mat = np.array(self.maze_mat)
    self.rowsInMaze, self.colsInMaze = self.maze_mat.shape
    self.start_pos = self.get_start_position()
    self.solution_path = []

  def get_start_position(self):
    row, col = np.where(self.maze_mat == 'S')
    return Point2D(row[0], col[0])

  def get_maze_for_plot(self):
    # set obstacles to value 0 (black in pcolor plot) and 
    # space to 255 (yellow in pcolor)
    maze_mat = np.where(self.maze_mat == OBSTACLE, 0, 255)
    # color solution path with blue
    maze_mat = np.where(self.maze_mat == SOLUTION_PATH, 50, maze_mat)
    # color start position with green
    maze_mat[self.start_pos.x, self.start_pos.y] = 200 

    return maze_mat

  def isDestination(self, pos):
      return (pos.x == 0 or
              pos.x == self.rowsInMaze-1 or
              pos.y == 0 or
              pos.y == self.colsInMaze-1 )
    
  def __getitem__(self, pos):
    return self.maze_mat[pos.x, pos.y]
  def __setitem__(self, pos, val):
    self.maze_mat[pos.x, pos.y] = val

  def updatePosition(self, pos, val=None):
        if val:
          self.__setitem__(pos, val)
        if val == SOLUTION_PATH:
            self.solution_path.append(pos)

def searchSolutionPath(maze, start_pos):
  #  Base cases:
  #  1. We have run into an obstacle, return false
  if maze[start_pos] == OBSTACLE :
    return (not Path.Found)
  #  2. We have found a square that has already been explored
  if maze[start_pos] == TRIED or maze[start_pos] == DEAD_END:
    return (not Path.Found)
  #  3. Success, an outside edge not occupied by an obstacle
  if maze.isDestination(start_pos):
    maze.updatePosition(start_pos, SOLUTION_PATH)
    return Path.Found
  maze.updatePosition(start_pos, TRIED)

  # try each direction 
  start_row, start_col = start_pos.x, start_pos.y
  found = searchSolutionPath(maze, Point2D(start_row-1, start_col) ) or \
          searchSolutionPath(maze, Point2D(start_row+1, start_col) ) or \
          searchSolutionPath(maze, Point2D(start_row, start_col-1) ) or \
          searchSolutionPath(maze, Point2D(start_row, start_col+1) )
  if found:
    maze.updatePosition(start_pos, SOLUTION_PATH)
  else:
    maze.updatePosition(start_pos, DEAD_END)
  return found

def run(filename)
  maze = Maze(filename)
  result = searchSolutionPath(maze, maze.start_pos)
  if result:
    plt.pcolor(mazeobj.get_maze_for_plot())
    plt.gca().invert_yaxis()
    plt.show()
    print(maze.maze_mat)
    print("Squares in Blue indicate solution path")
    print("Green indicates start position")
  else:
    print("Path Not Found")


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('filename')
  args = parser.parse_args()
  run(args)



  
