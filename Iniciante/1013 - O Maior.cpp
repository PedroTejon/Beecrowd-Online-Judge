#include <iostream>

using namespace std;

int main()
{
    int a, b, c, maiorAb, maiorTodos;
    cin >> a;
    cin >> b;
    cin >> c;
    maiorAb = (a + b + abs(a - b)) / 2;
    maiorTodos = (maiorAb + c + abs(maiorAb - c)) / 2;
    
    printf("%d eh o maior\n", maiorTodos);

    return 0;
}
