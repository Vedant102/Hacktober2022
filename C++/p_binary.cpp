//C++ code
//https://codeforces.com/contest/1225/problem/C
#include<bits/stdc++.h>
using namespace std;
#define ll long long
long long takat(long long a,long long b){
    long long c=a;
    if(b==0){
        a=1;
    }
    for(long long i=0;i<b-1;i++){
        a=(a*c)%(ll)(1e9+7);
    }
    return a;
}
string st[1001][1001];
string d="";
int main (){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    ll n,k,m,a=0,b=1,j=0;
    cin>>n>>m;
    char c;
    string s="",s1="",s2="";
    map<string,bool> mp;
    for(ll i=0;i<m;i++){
        c='a'+i;
        s1+=c;
    }
    for(ll i=0;i<m;i++){
        s+=s1[i];
        for(ll j=i+1;j<m;j++){
            s+=s1[i];
            s+=s1[j];
        }
    }
    s1="";
    m=s.size();
    while(s1.size()!=n){
        s1+=s[j%m];
        j++;
    }
    cout<<s1;
}
