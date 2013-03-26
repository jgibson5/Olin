import serial  
import time
import math

try:  
    ser = serial.Serial('/dev/ttyUSB0', 9600)  
except:  
    print "Failed to connect on /dev/ttyUSB0"  

class robot():
    """represents the robot.
       attributes: position, color, arm, sketch
    """

    def ser_write(self, case, value):
        bytes = [255, case, value]
        for entry in bytes:
            ser.write(chr(entry))

    def move_arm(self, arm_pos):
         """moves arm to up or down position with servo1"""
         if arm_pos == "down":
            self.ser_write(1, self.servo1_down)
         if arm_pos == "up":
            self.ser_write(1, self.servo1_up)
         self.arm = arm_pos

    def switch_color(self, color):
        """switches marker color with servo2"""
        if self.arm == "down":
            self.move_arm("up")
        self.ser_write(2, self.color_pos[color])
        self.color = color

    def go_to_pos(self, position):
        """move robot to position moving only perpendicular to the x, y axis
        """
        x_dif = position[0] - self.position[0]
        y_dif = -position[1] + self.position[1]
        if x_dif != 0: direction = math.atan2(y_dif, x_dif) * 180 / math.pi
        elif y_dif > 0: direction = 90
        else: direction = 270
        if direction < 0: direction += 360
        distance = math.sqrt(x_dif**2 + y_dif**2)
        distance_inches = math.sqrt((x_dif * self.dimensions[0] / self.canvas_size[0])**2 +
                                    (x_dif * self.dimensions[1] / self.canvas_size[1])**2)
        print 'dist', distance_inches
        
        phi = direction
        section = 0
        group = 1
        while phi > 45:
            phi -= 45
            group += 1
        
        phi = 45 - phi
            
        if group % 2 == 0:
            section = 2
        else:
            section = 1
            
        if section == 1:
            motor2 = int(math.sin((phi * math.pi / 180)) * 242.5 /
			             math.sin(math.pi / 2))
            motor4 = motor2
            motor1 = int(math.sqrt((.95 * 255)**2 - motor2**2))
            motor3 = motor1
            print direction, phi, section, group, motor1, motor2, motor3, motor4
            print math.sqrt(motor2**2 + motor1**2)
        if section == 2:
            motor1 = int(math.sin((phi * math.pi / 180)) * 100 /
			             math.sin(math.pi / 2))
            motor3 = motor1
            motor2 = int(math.sqrt((.95 * 255)**2 - motor1**2))
            motor4 = motor2
            print direction, phi, section, group, motor1, motor2, motor3, motor4
            print math.sqrt(motor2**2 + motor1**2)
        
        if group == 1 or group == 8:
            self.ser_write(3, motor1)
            self.ser_write(5, motor2)
            self.ser_write(7, motor3)
            self.ser_write(9, motor4)
        if group == 2 or group == 3:
            self.ser_write(3, motor1)
            self.ser_write(6, motor2)
            self.ser_write(8, motor3)
            self.ser_write(9, motor4)
        if group == 4 or group == 5:
            self.ser_write(4, motor1)
            self.ser_write(6, motor2)
            self.ser_write(8, motor3)
            self.ser_write(10, motor4)
        else:
            self.ser_write(4, motor1)
            self.ser_write(5, motor2)
            self.ser_write(7, motor3)
            self.ser_write(10, motor4)
            
        
        self.ser_write(11,0)
        
        print self.scaling_factor * distance_inches
        time.sleep(self.scaling_factor * distance_inches)
            
        self.position = position
    
    def draw_item(self):
        for item in self.sketch:
            coords = item[1]
            color = item[0]
            if color != self.color:
                self.switch_color(color)
            self.go_to_pos(coords[0])
            self.move_arm("down")
            self.go_to_pos(coords[1])
            time.sleep(1)
            self.move_arm("up")
        self.ser_write(11,0)

    def __init__(self, sketch, dimensions):
        self.position = [0, 0]
        self.color = "black"
        self.arm = "down"
        self.sketch = sketch
        self.canvas_size = [342, 290]
        self.dimensions = dimensions
        self.scaling_factor = 60.0 / 501

        #constants

        #servo arm positions
        self.servo1_down = 25
        self.servo1_up = 50
        #color wheel positions
        self.color_pos = {"red": 20, "blue": 176, "yellow": 100, "black": 140, 
                          "lightBlue": 120, "green": 160, "orange": 80, "purple": 60}


