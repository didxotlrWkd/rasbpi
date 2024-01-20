#include <iostream>
#include <wiringPi.h>
#include <softPwm.h>

#define	ENA	3	//ENA
#define	DIR	0	//DIR
#define	PUL	2	//PUL

using namespace std;

void setup(){
	wiringPiSetupGPIO();
  	pinMode(ENA, OUTPUT);
	pinMode(DIR, OUTPUT);
	pinMode(PUL, OUTPUT);

//	digitalWrite(ENA, LOW);
//	digitalWrite(DIR, LOW);
//	digitalWrite(PUL, LOW);
}

int main(){
	setup();
	digitalWrite(ENA , HIGH);
	cout << "ENA HIGH" << endl;
	delay(2);
	digitalWrite(ENA , LOW);
	cout << "ENA LOW" << endl;
	cout << "wiring pi" << endl;

	while(1){
		for(int i = 0; i < 1000; i++){
		    digitalWrite(DIR, LOW);
			digitalWrite(PUL, HIGH);
			delay(1);
			digitalWrite(PUL, LOW);
			delay(1);
		}

		cout << "CHANGE DIR" << endl;
		
	    for(int i = 0; i < 1000; i++){
	            digitalWrite(DIR, HIGH);
	            digitalWrite(PUL, HIGH);
	            delay(1);
	            digitalWrite(PUL, LOW);
       	        delay(1);
        }
	}

	return 0;
}