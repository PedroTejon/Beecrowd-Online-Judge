#include <iostream>

using namespace std;

int main()
{
    int a;
    float b, valorTotal;
    cin >> a;
    cin >> b;
    valorTotal = a / b;
    
    printf("%.3f km/l\n", valorTotal);

    return 0;
}
