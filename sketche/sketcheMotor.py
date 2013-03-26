class robot():
    """represents the robot.
       attributes: position, color, arm, sketch
    """

    def move_arm(self, arm_p):
         """moves arm to up or down position with servo1"""
         if arm_p == "down":
            print 'move arm down'
         if arm_p == "up":
            print 'move arm up'
         self.arm = arm_p

    def switch_color(self, color):
        """switches marker color with servo2"""
        color_pos = {"red": 20, "#003399": 60, "yellow": 100, "black": 140}
        if self.arm == "down":
            self.move_arm("up")
        print 'move servo2 to ' + str(color_pos[color])
        self.color = color
        print "current color is " + str(self.color)

    def go_to_pos(self, position):
        """move robot to position moving only perpendicular to the x, y axis
        """
        x_dif = position[0] - self.position[0]
        y_dif = position[1] - self.position[1]
        if x_dif > 0: 
            print "run motors x-dir, forward"
            #stop motors     
        if x_dif < 0:
            print "run motors x-dir, backward"
            #stop motors 
        if y_dif > 0: 
            print "run motors y-dir, forward"
            #stop motors
        if y_dif < 0:
            print "run motors y-dir, backward"
            #stop motors
        self.position = position
        print "current position is " + str(self.position)
    
    def draw_item(self):
        for item in self.sketch:
            values = self.sketch[item]
            color = values[0]
            coords = values[1]
            if color != self.color:
                self.switch_color(color)
            self.go_to_pos(coords[0])
            self.move_arm("down")
            for i in range(len(coords)-1):
                self.go_to_pos(coords[i+1])
            self.move_arm("up")

    def __init__(self, sketch):
        self.position = [0, 0]
        self.color = "black"
        self.arm = "down"
        self.sketch = sketch 





