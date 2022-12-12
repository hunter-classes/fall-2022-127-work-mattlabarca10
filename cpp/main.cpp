#include<iostream>
using namespace std;

int largest(int arr[], int n){   // use of function; takes in array and size of array, returns the largest element
    int max = arr[0];
    for (int i = 1; i < n; i++)  // use of for loop
        if (arr[i] > max)        // use of if statement
            max = arr[i];
    return max;
}

int doub(int a){                 // takes in an integer and returns it doubled
    return a*2;
}

int main()
{
    cout<<"Hello World!"<<endl;  // base project
    
    int a = 1;
    int b = 5;
    int c = 9;

    cout<<"Right now a = "<<a<<", b = "<<b<<", and c = "<<c<<"."<<endl;
    b = doub(b);
    cout<<"The variable b has now been doubled."<<endl;
    int array[] = {a,b,c};
    cout<<"Out of these numbers, the largest number is "<<largest(array,3)<<" since b was doubled."<<endl;
    return 0;
}
