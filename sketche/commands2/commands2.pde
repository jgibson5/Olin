// Adafruit Motor shield library
// copyright Adafruit Industries LLC, 2009
// this code is public domain, enjoy!

#include <AFMotor.h>
#include <Servo.h> 

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

int startbyte;
int CASE;
int val;
int angle;

Servo servo1;
Servo servo2;

   
void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");

  // turn on motors
  motor1.setSpeed(255);
  motor2.setSpeed(255);
  motor3.setSpeed(255);
  motor4.setSpeed(255);
 
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  
  // turn on servos
  servo1.attach(10);
  servo2.attach(9);
  
  servo1.write(25);
  servo2.write(0);
  //servo2.attach(10);
}

void loop() {
  uint8_t i;
  
  //Serial.print("tick");
  
  if (Serial.available() > 2) {
    startbyte = Serial.read();
    if (startbyte == 255) {
      CASE = Serial.read();
      val = Serial.read();
    }
  }
  switch (CASE) {
    
    case 1: //servo1 (arm)

    if (val == 25) {
      servo1.detach();
    }
    else {
      servo1.attach(10);
      servo1.write(val);
    }
    break;
    
    case 2: //servo2 (color wheel)
      servo2.write(val);
      break;
    
    case 3://motor 1 forward
      motor1.run(FORWARD);
      motor1.setSpeed(val);
      break;
      
    case 4://motor 1 backward
      motor1.run(BACKWARD);
      motor1.setSpeed(val);
      break;
    
    case 5://motor 2 forward
      motor2.run(FORWARD);
      motor2.setSpeed(val);
      break;
      
    case 6://motor 2 backward
      motor2.run(BACKWARD);
      motor2.setSpeed(val);
      break;
          
    case 7://motor 3 forward
      motor3.run(FORWARD);
      motor3.setSpeed(val);
      break;
      
    case 8://motor 3 backward
      motor3.run(BACKWARD);
      motor3.setSpeed(val);
      break;
          
    case 9://motor 4 forward
      motor4.run(FORWARD);
      motor4.setSpeed(val);
      break;
      
    case 10://motor 4 backward
      motor4.run(BACKWARD);
      motor4.setSpeed(val);
      break;

    case 11://all motors stop
      motor1.run(RELEASE);
      motor2.run(RELEASE);
      motor3.run(RELEASE);
      motor4.run(RELEASE);
      break;         
      
   }
}
