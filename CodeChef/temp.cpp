#include <stdio.h>
#include <iostream>
#include <string>
#include <cctype>
#include <cstring>
#include <map>
#include <numeric>
#include <bits/stdc++.h>
#include <unordered_map>
#include <vector>
#include <algorithm>
#define loop(i, a, b) for(int i=int(a); i<= int(b); i++) // loop variable i from a to b
#define ll long long
#define ull unsigned long long int
#define MAX INT_MAX
#define MIN INT_MIN
#define LMAX LONG_MAX
#define LMIN LONG_MIN
#define rep(i, n) for(int i=0;i<int(n);i++)
#define newline cout<<"\n"
using namespace std;
typedef vector<int> vi;
typedef pair<int, int> pii;

int gcd(int v,int b){
    if(v==0) return b;
    if(b==0) return v;
    if(v>b) return gcd(b,v);
    if(v==b) return b;
    if(b%v==0) return v;
    return gcd(v,b%v);
}

bool is_prime(int n) {
    if (n == 1) {
        return false;
    }
    int i = 2;
    while (i*i <= n) {
        if (n % i == 0) {
            return false;
        }
        i += 1;
    }
    return true;
}

vector<ll> prefix_sum(vector<int> &arr){
    int n = arr.size();
    ll currsum = 0ll;
    vector<ll> ans(n);
    rep(i, n){
        currsum+=arr[i];
        ans[i] = currsum;
    }
    return ans;
}


static bool isSorted(int arr[], int from, int to){
    for(int i=from;i<to;i++){
        if(arr[i+1] < arr[i]){
            return false;
        }
    }
    return true;
}
/*
static int sumofarr(int arr[], int n){
    int sum = 0;
    for(int i=0;i<n;i++){
        sum+=arr[i];
    }
    return sum;
}*/

//typedef vector<int, int>          vii;
void solve();

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
  
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("error.txt", "w", stderr);
    freopen("output.txt", "w", stdout);
#endif
  
    int t = 1;
    /is Single Test case?/cin >> t;
    int cas=1;
    while (t--) {
        //cout << "Case #"<<cas<<": ";
        solve();
        cas++;
        
    }
    //solve();
  
    cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl;
    return 0;
}


/*static int64_t helper(int64_t a, int64_t b, int64_t c){
    if(r == 0)return abs(a-b);



}*/
struct hashFunction 
{ 
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};

void solve(){

    int n; int k; cin>>n>>k;

    string s; string t; cin>>s>>t;
    unordered_map<char, int> memo;
    for(auto &i : s){
        memo[i]++;
    }
    for(auto &i : t){
        memo[i]--;
    }

    for(auto &i : memo){
        if(i.second != 0){
            cout<<"NO\n";
            return;
        }
    }

    if(k%2){
        if(t == s){
            if(s == "01" || s == "10"){
                cout<<"NO\n";
                return;
            }
        }
    }

    ll ans = 0ll;
    int cnt = 0;
    rep(i, n){
        if(t[i] != s[i]){
            ++ans;
            cnt+=s[i]-'0';
        }
    }
    if(ans == 2){
        if(s.length() == 2 && !(k%2)){
            cout<<"NO\n";
            return;
        }
    }
    if(ans == cnt*2 && k>=cnt){
        cout<<"YES\n";
    }else{
        cout<<"NO\n";
    }
}