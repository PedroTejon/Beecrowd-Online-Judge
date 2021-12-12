#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int segundos, h, m, s;
    scanf("%d", &segundos);

    h = floor(segundos / 3600);
    segundos = floor(segundos % 3600);
    m = floor(segundos / 60);
    s = floor(segundos % 60);
    
    printf("%d:%d:%d\n", h, m, s);

    return 0;
}