import pprint
import random

def make_maze(size, lvl, current_pos):
  matrix = [[random.randint(0,10) for col in range(size)] for row in range(size)]
  for row in range(len(matrix)):
    for col in range(len(matrix)):
      if matrix[row][col] > lvl:
        matrix[row][col] = "."
      else:
        matrix[row][col] = "|"
  x,y = current_pos
  matrix[x][y] = "S"
  matrix[-1][-1] = "E"

  return matrix

matrix = make_maze(10,3,[0,0])

def find_edges(pos, maze):
  arr = []
  x,y = pos
  length = len(maze)
  for x,y in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
    if 0 <= x < length and 0 <= y < length:
      if maze[x][y] != "|":
        arr.append([x,y])
  return arr

pprint.pprint(matrix)
#print(find_edges([0,0], matrix))

# def bfs(maze, node):
  #queue = [node]
  #explored = []
  #while queue:
    #FIFO
    #path = queue.pop(0)
    #check path
    #if path not in explored:
     # explored.append(path)
      #edges = find_edges(path, matrix)
      #for edge in edges:
       # if edge not in explored:
        #  queue.append(edge)
      #path = None
  #return explored

def dfs(maze, node):
  queue = [[node]]
  explored = []
  goal = [len(maze)-1, len(maze)-1]

  while queue:
    path = queue.pop(0)
    node = path[-1]

    if node not in explored:
      explored.append(node)
      edges = find_edges(node, maze)

      for edge in edges:
          new_list = list(path)
          new_list.append(edge)
          queue.append(new_list)
          if edge == goal:
            for x,y in new_list:
              maze[x][y] = 'X'
            return maze

  return explored

pprint.pprint(dfs(matrix,[0,0]))
