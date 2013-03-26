#include <AFMotor.h>

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

int sum = 0;
int pin2status_old = 0;
int pin2status = 0;

void setup() {                
  // initialize the digital pin as an output.
  // Pin 13 has an LED connected on most Arduino boards:
  Serial.begin(9600);
  pinMode(13, OUTPUT);    
  pinMode(2, INPUT);
  
  motor4.setSpeed(100);
  
  motor4.run(RELEASE);
}

void loop() {
//  motor4.run(FORWARD);
  digitalWrite(13, HIGH);   // set the LED on
//  delay(10);              // wait for a second
//  digitalWrite(13, LOW);    // set the LED off
//  delay(10);              // wait for a second  
  
  pin2status = digitalRead(2);
  if (pin2status_old == 1)
{
    if (pin2status == 0)
{
      sum++;
}
}
  pin2status_old = pin2status;
  Serial.println(sum);
}
