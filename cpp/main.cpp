#include<iostream>
using namespace std;

int largest(int arr[], int n){
    int max = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > max)
            max = arr[i];
    return max;
}

int doub(int a){
    return a*2;
}


int main()
{
    int a = 1;
    int b = 5;
    int c = 9;

    cout<<"Right now, a = "<<a<<", b = "<<b<<", and c = "<<c<<"."<<endl;
    b = doub(b);
    cout<<"The variable b has now been doubled."<<endl;
    int array[] = {a,doub(b),c};
    cout<<"Out of these numbers, the largest number is "<<largest(array,3)<<" since b was doubled."<<endl;
    return 0;
}
