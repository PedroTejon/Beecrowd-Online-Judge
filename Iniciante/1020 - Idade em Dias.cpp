#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int dias, a, m, d;
    scanf("%d", &dias);

    a = floor(dias / 365);
    dias = floor(dias % 365);
    m = floor(dias / 30);
    d = floor(dias % 30);
    
    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", a, m, d);

    return 0;
}