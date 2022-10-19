#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;   
    int*ptr = new int (n);
    int arr[n];

    cout<<"Enter the array"<<endl;

    for(int i=1;i<=n;i++)
    {
        cin>>arr[i];
        cout<<endl;
    }
    cout<<"reverse of the array is :"<<endl;
    for(int i=n;i>0;i--)
    {
        cout<<arr[i]<<endl;
        
    }
    return 0;
}
