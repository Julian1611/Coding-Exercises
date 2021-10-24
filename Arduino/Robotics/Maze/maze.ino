#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"
//front
int Echo1 = A8;
int Trig1 = A9;
//left
int Echo2 = A11;
int Trig2 = A12;
//right
int Echo3 = A14;
int Trig3 = A15;

long duration;
long distanceFront; //in cm
long distanceRight; //in cm
long distanceLeft;  //in cm

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield();

// Select which 'port' M1, M2, M3 or M4.
Adafruit_DCMotor *myMotor = AFMS.getMotor(1);
Adafruit_DCMotor *myMotor2 = AFMS.getMotor(2);

const int maxSpeed=100;

void setup() 
{
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Adafruit Motorshield v2 - DC Motor test!");
  //front
  pinMode(Echo1, INPUT);
  pinMode(Trig1, OUTPUT);
  //left
  pinMode(Echo2, INPUT);
  pinMode(Trig2, OUTPUT);
  //right
  pinMode(Echo3, INPUT);
  pinMode(Trig3, OUTPUT);

  AFMS.begin();  // create with the default frequency 1.6KHz

  // Set the speed to start, from 0 (off) to 255 (max speed)
  myMotor->setSpeed(maxSpeed);
  myMotor->run(RELEASE);

  myMotor2->setSpeed(maxSpeed);
  myMotor2->run(RELEASE);

  //int coordinateArray[30][30]; //array fuer Koordinaten und die Information zu jedem einzelnen

  //coordinateArray[0][0]=starttile;
}

void forward()
{
  //default mode
  //WHITE WIRES OUTSIDE
  myMotor->setSpeed(maxSpeed);
  myMotor->run(FORWARD);

  myMotor2->setSpeed(maxSpeed);
  myMotor2->run(FORWARD);

  Serial.println("Forward");
}

void stopMove()
{
  //if wall, or black tile
  myMotor->run(RELEASE);
  myMotor2->run(RELEASE);

  Serial.println("STOP");
}

void backward()
{
  //only if black tile
  myMotor->run(BACKWARD);
  myMotor2->run(BACKWARD);

  Serial.println("Back");
}

void left()
{
  //turn left (time must be tested)
  myMotor->run(FORWARD);
  myMotor2->run(BACKWARD);

  Serial.println("Left");
  delay(3000);
}

void right()
{
  //turn right (time must be tested)
  myMotor->run(BACKWARD);
  myMotor2->run(FORWARD);

  Serial.println("Right");
  delay(3000);
}

void loop() //needs to be changed, Tremaux-Alogrithm
{
  forward();
  digitalWrite(Trig1, LOW);
  delayMicroseconds(5);
  digitalWrite(Trig1, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig1,LOW);
  duration = pulseIn(Echo1, HIGH);
  distanceFront = (duration/2) / 29.1;
  Serial.print("distance Front in cm: ");
  Serial.println(distanceFront);

  if(distanceFront <= 6)
  {
    stopMove();
    //Seiten checken
    //links
    digitalWrite(Trig2, LOW);
    delayMicroseconds(5);
    digitalWrite(Trig2, HIGH);
    delayMicroseconds(10);
    digitalWrite(Trig2,LOW);
    duration = pulseIn(Echo2, HIGH);
    distanceLeft = (duration/2) / 29.1;
    Serial.print("distance left in cm: ");
    Serial.println(distanceLeft);

    //rechts
    digitalWrite(Trig3, LOW);
    delayMicroseconds(5);
    digitalWrite(Trig3, HIGH);
    delayMicroseconds(10);
    digitalWrite(Trig3,LOW);
    duration = pulseIn(Echo3, HIGH);
    distanceRight = (duration/2) / 29.1;
    Serial.print("distance right in cm: ");
    Serial.println(distanceRight);

    if (distanceLeft >= 20)
    {
      //turn left (later: Tremaux-Algorithm, but for now: the left-hand-method)
      left();
    }
    else if (distanceRight >= 20)
    {
      //turn right
      right();
    }
    else
    {
      //go back!
      right();
      right();
    }
  }
}
