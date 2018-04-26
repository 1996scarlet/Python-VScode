#coding=utf-8
import sys
def okok(n,s,m,count):
    if(len(s)>n): 
        return 10000
    if(len(s)==n):
        return count
    else:
        return min(okok(n,s+m,m,count+1),okok(n,s+s,s,count+1))
    
if __name__ == "__main__":    
    print(okok(int(sys.stdin.readline().strip()),"a","a",0))