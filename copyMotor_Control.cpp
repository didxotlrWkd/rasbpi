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
    digitalWrite(ENA, LOW);
//	digitalWrite(ENA, LOW);
//	digitalWrite(DIR, LOW);
//	digitalWrite(PUL, LOW);
}

int main(){
	setup();
    delay(3000);
	cout << "wiring pi" << endl;

	while(1){
		for(int i = 0; i < 5000; i++){
		        digitalWrite(DIR, LOW);
		        digitalWrite(ENA, HIGH);
			digitalWrite(PUL, HIGH);
			delay(0.5);
			digitalWrite(PUL, LOW);
			delay(0.5);
		}

	        for(int i = 0; i < 1000; i++){
	                digitalWrite(DIR, HIGH);
	                digitalWrite(ENA, HIGH);
	                digitalWrite(PUL, HIGH);
	                delay(2);
	                digitalWrite(PUL, LOW);
       		        delay(2);
        	}
	}

        digitalWrite(ENA, HIGH);
        digitalWrite(DIR, LOW);

	return 0;
}
