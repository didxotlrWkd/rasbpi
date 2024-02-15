#include <iostream>
#include <wiringPi.h>
#include <softPwm.h>

#define	ENA	15	//ENA
#define	DIR	16	//DIR
#define	PUL	1	//PUL

using namespace std;

void setup(){
	wiringPiSetup();
  	pinMode(ENA, OUTPUT);
	pinMode(DIR, OUTPUT);
	pinMode(PUL, OUTPUT);

//	digitalWrite(ENA, LOW);
//	digitalWrite(DIR, LOW);
//	digitalWrite(PUL, LOW);
}

int main(){
	setup();
	cout << "wiring pi" << endl;

	while(1){
		for(int i = 0; i < 1000; i++){
		        digitalWrite(DIR, LOW);
		        digitalWrite(ENA, LOW);
			digitalWrite(PUL, HIGH);
			delay(1);
			digitalWrite(PUL, LOW);
			delay(1);
		}

	        for(int i = 0; i < 1000; i++){
	                digitalWrite(DIR, HIGH);
	                digitalWrite(ENA, LOW);
	                digitalWrite(PUL, HIGH);
	                delay(1);
	                digitalWrite(PUL, LOW);
       		        delay(1);
        	}
	}

        digitalWrite(ENA, LOW);
        digitalWrite(DIR, LOW);

	return 0;
}