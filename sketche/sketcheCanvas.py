from Tkinter import *

class sketcheCanvas(Canvas):
    """Inherits from tk.Canvas. Additional methods for mouse click callbacks.
    e.g. drawing lines, curves, etc."""

    def setVals(self):
        """Sets attributes needed in sketcheGui."""
        self.click = False
        self.items = []
        self.tool = self.drawLine
        self.color = 'black'
        self.ordered_pairs_final = []
        self.ordered_pairs_init = []
        self.coord_dict = {}
        self.lines = []
        self.dimensions = [36, 36]
        
        self.bind("<Button-1>", self.draw)
        self.bind("<Motion>", self.drawUpdate)

    def changeColor(self, color):
        """Sets the color"""
        self.color = color
        
    def drawLine(self, coords):
        """Draws a line on the canvas if self.click is true. 
        If self.click is false, just stores event coordinates in self.coords.
        args:
            coords: list of 2 floats
        """
        if self.click == False: 
            self.coords = coords
            self.ordered_pairs_init.append(coords)
        else:
            self.items.append(self.create_line([self.coords, coords], fill=self.color))
            self.ordered_pairs_final.append(coords)
            if len(self.ordered_pairs_final) % 2 == 0:
                self.coord_dict[self.items[1]] = [self.color, [self.ordered_pairs_init[0], self.ordered_pairs_final[0]]]
                self.lines.append((self.color, [self.ordered_pairs_init[0], 
                                                self.ordered_pairs_final[0]]))
                self.items = []
                self.ordered_pairs_final = []
                self.ordered_pairs_init = []

    def drawRectangle(self, coords):
        """Draws a rectangle on the canvas if self.click is true.
        If self.click is false, just stores event coordinates in self.coords.

        args:
            coords: list of 2 floats
        """
        if self.click == False: 
            self.coords = coords
            self.ordered_pairs_init.append(coords)
        else:
            self.items.append(self.create_rectangle([self.coords, coords], outline=self.color))
            self.ordered_pairs_final.append(coords)
            if len(self.ordered_pairs_final) % 2 == 0:
                x1 = self.ordered_pairs_init[0][0]
                y1 = self.ordered_pairs_init[0][1]
                x2 = self.ordered_pairs_final[0][0]
                y2 = self.ordered_pairs_final[0][1]
                rect_coords = [[x1, y1],[x2, y1],[x2, y2],[x1, y2]]
                self.coord_dict[self.items[1]] = [self.color, rect_coords]
                self.lines.append((self.color, [x1, y1]))
                self.lines.append((self.color, [x1, y2]))
                self.lines.append((self.color, [x2, y2]))
                self.lines.append((self.color, [x2, y1]))
                self.items = []
                self.ordered_pairs_final = []
                self.ordered_pairs_init = []
    
    def drawFreeHand(self, coords):
        """Draws a series of lines following the path of the mouse."""
        if self.click == False:
            self.coords = coords
        else:
            self.coord_dict[self.create_line([self.coords, coords], fill = self.color)] = [self.color, [self.coords, coords]]
            self.lines.append((self.color, [self.coords, coords]))
            self.coords = coords

    def draw(self, event):
        """Runs the tool function stored in self.tool as a callback to
        left mouse click event."""
        if self.tool != None: self.tool([event.x, event.y])
        self.click = not self.click
        self.motionLen = 0
        
    def drawUpdate(self, event):
        """Updates the shape being drawn as a callback to mouse motion."""
        if self.click == True:
            if self.motionLen > 0:
                if self.tool != self.drawFreeHand:
                    self.delete(self.items[-1])
                    self.items.pop(-1)
                    self.ordered_pairs_final.pop(-1)
            self.tool([event.x, event.y])
            self.motionLen += 1
