from Tkinter import *
from sketcheCanvas import *
from sketcheMotor2 import *

class SketcheGui(object):
    """Object to encapsulate GUI methods and create memory of GUI attributes,
    e.g. values in the canvas."""
        
    def constructGui(self):
        """Puts together the GUI, creating all widgets."""

        self.root = Tk()
        self.root.title('Sketch-E')
        
        self.titleLabel = Label(self.root, text = 'Sketch-E Sketcher')
        self.titleLabel.grid(row = 0, column = 10)
        
        self.skCanvas = sketcheCanvas(self.root, bg = 'white')
        self.skCanvas.grid(row = 1, column = 0, rowspan = 20, columnspan = 20)
        self.skCanvas.setVals()

        self.clearButton = Button(self.root, text='Clear', command=self.clear)
        self.clearButton.grid(row = 21, column = 5) 

        self.drawButton = Button(self.root, text='Draw', command=self.draw)
        self.drawButton.grid(row = 21, column = 14)
        
        linePic = PhotoImage(file = "linePic.gif")
        self.drawLineButton = Button(self.root, image = linePic, 
                                     command = self.drawLineCB)
        self.drawLineButton.grid(row = 1, column = 21)
        
        rectanglePic = PhotoImage(file = "rectanglePic.gif")
        self.drawRectangleButton = Button(self.root, image = rectanglePic,
                                          command = self.drawRectangleCB)
        self.drawRectangleButton.grid(row = 1, column = 22)
        
        self.drawFreeHandButton = Button(self.root, bg = 'ivory',
                                         command = self.drawFreeHandCB)
        self.drawFreeHandButton.grid(row = 2, column = 21)

        redPic = PhotoImage(file = "red.gif")
        self.redButton = Button(self.root, image = redPic, 
                                 command = lambda: self.changeColorCB('red'))
        self.redButton.grid(row = 3, column = 21)

        orangePic = PhotoImage(file = "orange.gif")
        orangeHex = '#FF6700'
        self.orangeButton = Button(self.root, image = orangePic, 
                         command = lambda: self.changeColorCB('orange'))
        self.orangeButton.grid(row = 3, column = 22)

        greenPic = PhotoImage(file = "green.gif")
        greenHex = '#32CD32'
        self.greenButton = Button(self.root, image = greenPic, 
                         command = lambda: self.changeColorCB('green'))
        self.greenButton.grid(row = 4, column = 22)

        lightBluePic = PhotoImage(file = "lightBlue.gif")
        lbHex = '#00BFFF'
        self.lightBlueButton = Button(self.root, image = lightBluePic, 
                             command = lambda: self.changeColorCB('lightBlue'))
        self.lightBlueButton.grid(row = 4, column = 21)
        
        blueHex = '#003399'
        bluePic = PhotoImage(file = "blue.gif")
        self.blueButton = Button(self.root, image = bluePic, 
                                 command = lambda: self.changeColorCB('blue'))
        self.blueButton.grid(row = 5, column = 22)

        purplePic = PhotoImage(file = "purple.gif")
        purpleHex = '#BF00FF'
        self.purpleButton = Button(self.root, image = purplePic, 
                        command = lambda: self.changeColorCB('purple'))
        self.purpleButton.grid(row = 5, column = 21)

        yellowPic = PhotoImage(file = "yellow.gif")
        self.yellowButton = Button(self.root, image = yellowPic, 
                                   command = lambda: self.changeColorCB("yellow"))
        self.yellowButton.grid(row = 6, column = 21)
        
        blackPic = PhotoImage(file = "black.gif")
        self.blackButton = Button(self.root, image = blackPic, 
                                  command = lambda: self.changeColorCB("black"))
        self.blackButton.grid(row = 6, column = 22)

        self.root.mainloop()
        
    def drawLineCB(self):
        """Callback for the drawLine button. Sets self.tool to drawLine."""
        self.skCanvas.tool = self.skCanvas.drawLine
        
    def drawRectangleCB(self):
        """Callback for the drawRectangle button. Sets self.tool to 
        drawRectangle."""
        self.skCanvas.tool = self.skCanvas.drawRectangle
    
    def drawFreeHandCB(self):
        """Callback for the drawFreeHand button. Sets self.tool to drawFreeHand."""
        self.skCanvas.tool = self.skCanvas.drawFreeHand

    def changeColorCB(self,color):
        """Callback for the changeColor button."""
        self.skCanvas.changeColor(color)
    
    def clear(self):
        """Callback for the clear button. Clears the canvas"""
        self.skCanvas.delete('all')
        self.skCanvas.lines = []

    def draw(self):
        """Callback for the draw button. Sends the information from the 
        canvas to the robot so it can draw it"""
        print self.skCanvas.lines
        self.sketcheMotor = robot(self.skCanvas.lines, 
                                  self.skCanvas.dimensions)
        self.sketcheMotor.draw_item()
                
                
        

gui = SketcheGui()
gui.constructGui()
