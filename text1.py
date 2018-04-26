#coding=utf-8
import sys
if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))

    n = values[0]
    k = values[1]

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int,line.split()))
    # values = array(set(values))

    newlit = [i + k for i in values]

    print(len(set(values) & set(newlit)))