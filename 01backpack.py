#n个物体的重量(w[0]无用)
w=[0,2,2,6,5,4]
#n个物体的价值(p[0]无用)
p = [0,6,3,5,4,6]
#计算n的个数
n=len(w)-1
#背包的载重量
m=10
#装入背包的物体,元素为True时,对应物体被装入（x[0[无用)
x=[False for raw in range(n+1)]
v=0
#optp[i][j]表示在前i个物体中，能够装入载重量为j的背包中的物体的最大价值
optp = [[0 for col in range(m+1)]for raw in range(n+1)]

def knapsack_dynamic(w,p,n,m,x):
    #计算optp[i][j]
    for i in range(1,n+1):
        for j in range(1,m+1):
            optp[i][j] = optp[i-1][j]
            if (j >= w[i]) and (optp[i-1][j-w[i]]+p[i]):
                optp[i][j]=optp[i-1][j-w[i]]+p[i]

    #递推装入背包的物体
    j=m
    for i in range(n,0,-1):
        if optp[i][j]>optp[i-1][j]:
            x[i]=True
            j=j-w[i]

    #返回最大价值
    v=optp[n][m]
    return v
print('最大值为:'+ str(knapsack_dynamic(w,p,n,m,x)))
print(x[1:])