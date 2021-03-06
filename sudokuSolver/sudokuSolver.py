from Tkinter import *
from operator import attrgetter

class Gui():
    """Gui object that constructs and contains widgets."""
    def __init__(self, n = 630):
        """Creates Gui object and runs construction function.

        args:
            n is int of pixel width/heighth of sudoku grid

        sets:
            gridSize is n
            nSolved is known values of sudoku boxes
        """
        self.gridSize = n
        self.nSolved = 0
        self.constructGui()


    def constructGui(self):
        """Constructs widgets in Gui."""
        self.root = Tk()
        self.root.geometry("%dx%d" %(int(1.2 * self.gridSize), 
                                     int(1.2 * self.gridSize)))

        self.grid = Grid(self.root, height = self.gridSize + 6, 
                         width = self.gridSize + 6, bg = 'white')
        self.grid.setup(self.root, self.gridSize / 9)
        self.grid.pack(padx = .1 * self.gridSize)
        
        self.solveButton = Button(self.root, text = 'Solve', 
                                  font = (self.grid.font, self.grid.fontSize),
                                  command = lambda: self.collectVals())
        self.solveButton.pack()
        
        self.root.mainloop()
        
    def collectVals(self, fileDir = 'test1.txt'):
        """Callback to solveButton.

        If fileDir is specified, inputs sudoku puzzle from file.

        args:
            fileDir is a string file directory for sudoku puzzle.
        """
        if fileDir:
            self.parseData(fileDir)
        for i in range(len(self.grid.squares)):
            x = i % 9
            y = i / 9
            box = self.grid.numbers.findBox(x, y)
            val = self.grid.squares[i].get()
            if val != '':
                self.nSolved += 1
                box.val = int(val)
                box.valType = 'int'
        self.solve()
				
    def solve(self):
        """Given the input values, runs through the solving algorithm."""
        while self.nSolved < 81:
            numbers = self.grid.numbers
            
            numbers.sortRow()
            n = numbers.checkNumbers(self.grid)
            self.nSolved += n
            
            numbers.sortColumn()
            n = numbers.checkNumbers(self.grid)
            self.nSolved += n
            
            numbers.sortGroup()
            n = numbers.checkNumbers(self.grid)
            self.nSolved += n
            
    def parseData(self, fileDir):
        """Opens up the txt file at fileDir and parses the file and inputs
        it into the canvas.squares list.

        args:
            fileDir is a str file directory of a sudoku puzzle
        """
        fin = open(fileDir)
        x = 0
        for line in fin:
            for y in range(9):
                index = 9 * x + y
                if str(line[y]) != ' ':
                    self.grid.squares[index].insert(0, str(line[y]))
            x += 1
			
		
class Grid(Canvas):
    """Inherits from Canvas to give drawing functionality but adds attributes
    to manage sudoku numbers and squares."""
    
    def setup(self, root, n):
        """After Grid is initiated, setup sets attributes and creates entry
        widgets for sudoku input.

        args:
            root is the Gui root
            n is the pixel size of the sudoku square (found by gui.gridSize/9)

        sets:
            squares is a list of entry widgets
            numbers is a NumberList of Numbers
            fontSize is size of font for entry widgets
            font is font type
        """
        self.squares = []
        self.numbers = NumberList()
        self.fontSize = int(n/2.4)
        self.font = "Helvetica"

        coords = [[3, 3], [9 * n - 3, 9 * n + 6]]
        self.create_rectangle(coords, width = 4)

        groupNum = 0

        for x_loc in range(9):
            x = x_loc * n
            x += 3

            for y_loc in range(9):
                y = y_loc * n
                y += 3

                coords = [[x + 2, y + 2], [3*(x + n) - 5, 3*(y + n) - 5]]
                if x_loc % 3 == 0 and y_loc % 3 == 0:
                    self.create_rectangle(coords, width = 2)

                groupNum = self.calcGroup(x_loc, y_loc)
                self.numbers.append(Number([], x_loc + 1, y_loc + 1, groupNum))

                coords = [[x, y], [x + n, y + n]]
                self.create_rectangle(coords)

                tempSq = Entry(root, width = 2, justify = 'center',
                               font = (self.font, self.fontSize),
                               bg = 'white', bd = 0)
                self.squares.append(tempSq)
                tempSq.place(x = x + n - 3, y = y + 3)
			
    def calcGroup(self, m, n):
        """Calculates group number of Number object from row and column value.

        args:
            m is row int starting at 0
            n is column int starting at 0

        returns:
            group number int
        """
        m /= 3
        n /= 3
        return m + 1 + n * 3
		
class NumberList(list):
    """List of Number objects.

    Inherits from list for data structure but adds methods for specific
    sorting based on Number attributes."""
    def sortRow(self):
        """Sorts self based Number attributes in order:
            row, valType, column
        """
        self.sort(key = attrgetter('row', 'valType', 'column'))
		
    def sortColumn(self):
        """Sorts self based Number attributes in order:
            column, valType, row
        """
        self.sort(key = attrgetter('column', 'valType', 'row'))
		
    def sortGroup(self):
        """Sorts self based Number attributes in order:
            group, valType, row, column
        """
        self.sort(key = attrgetter('group', 'valType', 'row', 'column'))

    def sortVal(self):
        """Sorts self based Number attributes in order:
            row, valType, column, group
        """
        self.sort(key = attrgetter('val', 'group'))
		
    def findBox(self, x, y):
        """Returns the Number object corresponding to row x and column y.

        args:
            x is row int
            y is column int
        """
        self.sortRow()
        return self[9 * x + y]
		
    def checkNumbers(self, grid):
        """Takes the NumberList from grid and removes all known values
        from possible values in units of 9 (i.e. row, column, group).
        
        args:
            grid is Grid object
        """
        nSolved = 0
        for i in range(9):
            solvedNums = []
            solvedNums2, nums = self.findPairs(i)
            for j in range(9):
                index = 9 * i + j
                num = self[index]
                if type(num.val) == int:
                    solvedNums.append(num.val)
                else:
                    flag = False
                    if num not in nums:
						flag = num.removeVals(solvedNums2)
                    flag = flag or num.removeVals(solvedNums)
                    if flag:
                        nSolved += 1
                        loc = 9 * (num.column - 1) + num.row - 1
                        grid.squares[loc].insert(0, str(num.val))
                        grid.update()
        return nSolved
       
    def findPairings(self, i):
        pairings = {}
        solvedNums = []
        nums = []
        for j in range(9):
            index = 9 * i + j
            num = self[index]
            if type(num.val) == list:
                tup = tuple(num.val)
                if tup not in pairings:
                    pairings[tup] = []
                pairings[tup].append(num)
        for key, pair in pairings.items():
            if len(key) == len(pair):
                for x in key:
                    solvedNums.append(x)
                for n in pair:
                    nums.append(n)
        return solvedNums, nums
		
    def findPairs(self, i):
        solvedNums = []
        nums = []
        sortedNums = []
        for j in range(9):
            pairings = {}
            index = 9 * i + j
            num = self[index]
            if type(num.val) == list:
                sortedNums.append(num)
                sortedNums.sort(key = lambda x: len(x.val))
            #print [num.val for num in sortedNums]
            for num in sortedNums:
                for i in range(4):
                    group = set([])
                    for n in range(9):
                        group.add(n+1)
                    print group
                    pairings[frozenset(group)] = []
                    for key, val in pairings.items():
                        if group.issubset(key):
                            pairings[key].append(num.val)
                        else:
                            pairings[group] = [num.val]
                            print group, num.val
                    print pairings, "pairings"
                #pairings[group] = pairings.get(group, [])
                #pairings[group].append(num.val)
            #print pairings
        return sortedNums, nums
                
    
    def findPairN(self, sortedNums, pairings, count):
        while count >= 1:
            for n in sortedNums:
                if len(n.val) == n:
                    tup = set(n.val)
                    for tups, vals in pairings.items():
                        if tup.issubset(tups):
                            pairing[tups].append(n)
                    else:    
                        pairings[tup] = []
                        pairings[tup].append(n)
            count -= 1
        return pairings
					
			
		
class Number():
    """Object representing a box in sudoku, containing methods for
    changing the val."""
    
    def __init__(self, val = [], row = 0, column = 0, group = 0, valType = 'int'):
        """Creates Number object and sets attributes.
        
        args:
            val is a list of possible values
            row is int row
            column is int column
            group is int group
            valType is either 'int' or 'list'
        
        sets:
            val is set to list of [1-9] if give []
            row
            column
            group
            valType corresponds to list if val is list, int if val is int
        """
        if val == []:
            val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            valType = 'list'
        self.val = val
        self.row = row
        self.column = column
        self.group = group
        self.valType = valType

    def checkVal(self):
        """If len of self.val is 1, changes self.val to int of list index.
        
        returns:
            True if valType changed
        """
        if len(self.val) == 1:
            self.val = self.val[0]
            self.valType = 'int'
            return True

    def removeVals(self, vals):
        """Removes all values in vals from self.vals
        
        No changes made if self.val is int.
        
        args:
            vals is list of ints
        
        returns:
            True if self.val changed to int
            False if self.val remains list
        """
        for val in vals:
            if val in self.val:
                self.val.remove(val)
        if self.checkVal():
            return True
        return False

gui = Gui()
