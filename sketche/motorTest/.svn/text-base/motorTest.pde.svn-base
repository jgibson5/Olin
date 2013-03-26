// Adafruit Motor shield library
// copyright Adafruit Industries LLC, 2009
// this code is public domain, enjoy!

#include <AFMotor.h>
#include <Servo.h> 

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

Servo servo1;
Servo servo2;

int startbyte;
int CASE;
int val;
int angle;

int USB1 = A0;
int USB2 = A1;

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
  
  // turn on servo
  servo1.attach(9);
   
}

void loop() {
  uint8_t i;
  
  Serial.print("tick");
  
  if (Serial.available() > 2) {
    startbyte = Serial.read();
    if (startbyte == 255) {
      CASE = Serial.read();
      val = Serial.read();
      angle = val;
    }
  }
  switch (CASE) {
    case 1:
      //servo1 (arm)
      servo1.write(angle);
      break;
    
    case 2://motor1-forward
      motor1.run(FORWARD);
      motor1.setSpeed(val);
      break;
    
    case 3://motor1-backward
      motor1.run(BACKWARD);
      motor1.setSpeed(val);
      break;
      
    case 4://motor1-backward
      motor1.run(RELEASE);
      break;
  }
  
}

    
