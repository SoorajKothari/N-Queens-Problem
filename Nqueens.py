import random 
#class board

class Board:            
  def __init__(self, n):
    self.totalqueens = n  
    self.totalPositon = n * n
    self.constraints = []
    self.constraints = [0] * self.totalPositon
    self.queen = []

  def getPossibleMoves(self):
    # possibleMoves[] moves that can be made (if numOfConstraint zero) 
    possibleMoves = []
    for move, numOfConstraints in enumerate(self.constraints):
      if(numOfConstraints == 0):
        possibleMoves.append(move)
    return possibleMoves
    
  def makeMove(self, move):
    
    self.queen.append(move)
    self.addOrRemoveConstraints(move, add=True)

  def removeMove(self, move):
    self.queen.remove(move)
    self.addOrRemoveConstraints(move, add=False)

  # Function for checking conflicts in row,column,upper and lower diagonal
  def addOrRemoveConstraints(self, move, add):

    # callFunction for addConstraint / removeConstraint
    if(add):
      callFunction = self.addConstraint
    else:
      callFunction = self.removeConstraint

    # n queens so divides gives row number 
    row = move // self.totalqueens
    # n queens so modulus gives row number 
    col = move % self.totalqueens
    updiag = row + col
    lodiag = row - col

    for i in range(self.totalqueens):

      callFunction(self.getPos(row, i))

      callFunction(self.getPos(i,col))


      if(updiag > -1):
        callFunction(self.getPos(updiag, i))
        updiag -= 1

      if(lodiag < self.totalqueens):
        callFunction(self.getPos(lodiag, i))
        lodiag += 1

  def addConstraint(self, move):
    if(not move == -1):
      self.constraints[move] += 1

  def removeConstraint(self, move):
    if(not move == -1):
      self.constraints[move] -= 1

  # getting Postion for (row, col), n=8 (1,3) = 1*8 + 3 = 11 
  def getPos(self, row, col):
    pos = row * self.totalqueens + col
    if(pos >= self.totalPositon or pos < 0):
      return -1
    else:
      return pos

  def printSolution(self):
    print('*'*20)
    print("Final Result")
    print('*'*20)
    for i in range(self.totalqueens):
      row = ''
      for j in range(self.totalqueens):
        if(self.getPos(i, j) in self.queen):
          row += 'Q'
        else:
          row += '-'
        row += '  '    
      print(row)                                



#constructor board called
print('*'*20)
print("N*N Queens Problem")
print('*'*20)
    
b = Board(8)
# first queen placed randomly in column 0 (placing random queen)
print("Generating Random Number for placing First Queen")  
r = random.randint(0, b.totalqueens - 1)
print('random number = ', r)
move = r*b.totalqueens
print('first queen placed at: (',r,',',move%b.totalqueens,')')
b.makeMove(move)


# for first call to solve if wrongly place backtrack ---- > removeMove()
j=1 
def solveNQueens(j):  
  for i in b.getPossibleMoves():
    if(j == 1):
      isValid = solveNQueens(j-1)
      if(isValid):
        return True
      else:
        b.removeMove(move)  
    b.makeMove(i)
    if(len(b.queen) == b.totalqueens):
      return True
    else:
      isValid =  solveNQueens(j-1)
      
      if(isValid):
        return True

      else:
        b.removeMove(i)
  return False

if(solveNQueens(j)):
  print('Solution exists')
  b.printSolution()
else:
  print('Solution does not exists.')  