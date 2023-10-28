#include<stdio.h>
#include <iostream>
#include <iomanip>
using namespace std;
//Problem 3
//this program  gets the average and identify if pass or fail

int main() {

	//Declaration,initialization
	float finals = 0.0, midterms = 0.0, ave = 0.0;

	//input
	printf("Please enter your grade in Finals: ");
	scanf_s("%f", finals);

	printf("Please enter your grade in Midtems: ");
	scanf_s("%f", midterms);

	//process

	ave = (midterms + finals) / 2;

	if (ave >= 1.0 && ave <= 3.12)
		printf("Passed");
	else
		printf("Failed");
}

