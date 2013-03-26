# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  """
  
  visited = set()
  start = problem.getStartState()

  def dfsRecursive(current, path):
    if problem.isGoalState(current):
      return path

    possible = problem.getSuccessors(current)

    for node in possible:
      if not node[0] in visited:
        visited.add(node[0])
        attempt = dfsRecursive(node[0], path + [node[1]])
        if attempt:
          return attempt
    return False

  return dfsRecursive(start, [])

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"

  q = util.Queue()
  visited = set()
  start = problem.getStartState()

  def bfsRecursive(current):
    if problem.isGoalState(current[0]):
      return current[3]

    possible = problem.getSuccessors(current[0])

    for node in possible:
      if not node[0] in visited:
        visited.add(node[0])
        q.push(node + (current[3] + [node[1]],))

    next = q.pop()
    attempt = bfsRecursive(next)
    if attempt:
      return attempt

    return False

  return bfsRecursive((start, None, 0, []))

      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "

  q = util.PriorityQueue()
  visited = set()
  start = problem.getStartState()

  def ucsRecursive(current):
    if problem.isGoalState(current[0]):
      return current[3]

    possible = problem.getSuccessors(current[0])

    for node in possible:
      if not node[0] in visited:
        visited.add(node[0])
        q.push(node + (current[3] + [node[1]],), node[2])

    next = q.pop()
    attempt = ucsRecursive(next)
    if attempt:
      return attempt

    return False

  return ucsRecursive((start, None, 0, []))

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  
  q = util.PriorityQueue()
  visited = set()
  start = problem.getStartState()

  def astarRecursive(current):
    if problem.isGoalState(current[0]):
      return current[3]

    possible = problem.getSuccessors(current[0])

    for node in possible:
      if not node[0] in visited:
        visited.add(node[0])
        cost = util.manhattanDistance(current[0], node[0])
        q.push(node + (current[3] + [node[1]],), cost)

    next = q.pop()
    attempt = astarRecursive(next)
    if attempt:
      return attempt

    return False

  return astarRecursive((start, None, 0, []))
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch