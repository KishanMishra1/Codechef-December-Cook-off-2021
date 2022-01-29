'''You are given a string S of length N,
which consists of digits from 0 to 9. You can apply the following operation to the string:

Choose an integer L with 1≤L≤N and apply Si=(Si+1)mod10 for each 1≤i≤L.
For example, if S=39590, then choosing L=3 and applying the operation yields
the string S=406⎯⎯⎯⎯⎯⎯90.

The prefix of string S of length l(1≤l≤∣S∣) is string S1S2…Sl.
A prefix of length l is called good if S1=0,S2=0,…,Sl=0.
Find the length of the longest good prefix that can be obtained in string S
by applying the given operation maximum K times.'''
def solve(m,s):
    sm=0
    for i in range(m,-1,-1):
        k=(int(s[i])-int('0')+sm)%10
        if k==0:
            continue
        sm+=10-k
    return sm


if __name__=="__main__":
    for _ in range(int(input())):
        n,k=map(int,input().split())
        s=input()
        l,r,ans=0,n-1,0
        while(l<=r):
            mid=(l+r)//2
            if solve(mid,s)>k:
                r=mid-1
            else:
                ans=mid+1
                l=mid+1
        print(ans)
