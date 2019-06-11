#include "Arduino.h"

void setup() {
  pinMode(2,OUTPUT);// 
  pinMode(3,OUTPUT);//
  pinMode(4,OUTPUT);//
  pinMode(5,OUTPUT);//
  pinMode(6,OUTPUT);//
  pinMode(7,OUTPUT);//
  pinMode(8,OUTPUT);//
}
void segment(int A, int B, int C, int D, int E,int F, int G)
{
digitalWrite(2,A);
digitalWrite(3,B);
digitalWrite(4,C);
digitalWrite(5,D);
digitalWrite(6,E);
digitalWrite(7,F);
digitalWrite(8,G);
}
void loop () 
{
 delay(1000);
 segment(0,0,0,0,0,0,1);
 delay(1000); 
  segment(1,0,0,1,1,1,1);
  delay(1000);
  segment(0,0,1,0,0,1,0);
}

