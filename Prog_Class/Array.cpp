#include <stdio.h>
#include <windows.h>




void waitForKeyPress() {
    printf("Press any key to exit...\n");
    exit(0);
}
int main()
{
    int numbers[20];
    int sum = 0;
    int input_number = 0;

    printf("Enter how many numbers to input: ");
    scanf("%d", &input_number);

    for (int i = 0; i < input_number; i++)
    {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &numbers[i]);
        system("cls");
    }

    printf("Even numbers are: \n");
    for (int i = 0; i < input_number; i++)
    {
        if (numbers[i] % 2 == 0)
        {
            sum += numbers[i];

            printf("%d, ", numbers[i]);
        }
    }
    if (sum == 0)
    {

        system("cls");
        printf("No Even Numbers Found!");
         waitForKeyPress();
    }
    else
    {
    }






printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");


}
