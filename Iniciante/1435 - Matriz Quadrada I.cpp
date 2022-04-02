#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n = 1;
    while (n != 0){
        scanf("%d", &n);
        
        std::vector<vector<int>> matriz;
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                matriz[i][j] = 0;
            }
        }
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                cout << matriz[i][j] << " ";
            }
            cout << endl;
        }
        
    }
    
    return 0;
}