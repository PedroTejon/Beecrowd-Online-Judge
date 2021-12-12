#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    float f;
    int cedulas[7] = {100, 50, 20, 10, 5, 2, 1};
    
    scanf("%f", &f);
    
    printf("%.0f\n", f);
    
    for (int x = 0; x < 7; x++)
    {
        printf("%d nota(s) de R$ %d,00\n", (int)((f * 100) / 100) / cedulas[x], cedulas[x]);
        f -= (int)((int)(f * 100) / 100) / cedulas[x] * cedulas[x];

    }
    

    return 0;
}