#include <iostream>

using namespace std;

int main()
{
    int qntdAlunos, minAlunos, alnPresentes = 0;
    scanf("%d %d", &qntdAlunos, &minAlunos);
    
    int horAlunos[qntdAlunos];
    bool foi = false;
    
    for (int x = 0; x < qntdAlunos; x++)
    {
        scanf("%d", &horAlunos[x]);
        if (horAlunos[x] <= 0)
        {
            alnPresentes += 1;
        }
        if (minAlunos <= alnPresentes)
        {
            foi = true;
            break;
        }
        if (alnPresentes + (qntdAlunos - (x + 1)) < minAlunos)
        {
            break;
        }
    }
    
    if (foi)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }

    return 0;
}
