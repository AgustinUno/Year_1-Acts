#include <iostream>
#include <iomanip>
using namespace std;

//Compiler version g++ 6.3.0

int main()
{
    //declaration 
    string  classification = " ";
    int peso;
    double rate, total;
    //inputs
    cout << "Enter #1 to convert peso to US DOLLAR" << endl;
    cout << "Enter #2 to convert peso to EURO" << endl;
    cout << "Enter #3 to convert peso to JAPANESE YEN" << endl;
    cout << "Enter #4 to convert peso to POUND STERLING" << endl;
    cout << "Enter #5 to convert peso to AUSTRALIAN DOLLAR" << endl;
    cout << "Enter a number from 1-5: ";
    cin >> classification;
    cout << "Please enter peso(s): ";
    cin >> peso;
    cout << "Enter the rate of the currency: ";
    cin >> rate;
    //if statements
    if (classification == "1") {
        total = peso / rate;
        cout << "-------------------------";
        cout << endl << peso << " peso(s) is equal to: " << fixed << setprecision(2) << total << " USD";
    }
    else
        if (classification == "2") {
            total = peso / rate;
            cout << "-------------------------";
            cout << endl << peso << " peso(s) is equal to: " << fixed << setprecision(2) << total << " EU";
        }
        else
            if (classification == "3") {
                total = peso / rate;
                cout << "-------------------------";
                cout << endl << peso << " peso(s) is equal to: " << fixed << setprecision(2) << total << " JPY";
            }
            else
                if (classification == "4") {
                    total = peso / rate;
                    cout << "-------------------------";
                    cout << endl << peso << " peso(s) is equal to: " << fixed << setprecision(2) << total << " GBP";
                }
                else
                    if (classification == "5") {
                        total = peso / rate;
                        cout << "-------------------------";
                        cout << endl << peso << " peso(s) is equal to: " << fixed << setprecision(2) << total << " AUD";
                    }
                    else
                        cout << "----------------------" << endl << "You input a invalid number from 1-5!!";

}//end of program