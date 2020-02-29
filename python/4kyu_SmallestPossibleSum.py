def solution(a):
    if len(a)==1:
        return a[0]
    def fun(a,b):
        if a%b==0:
            return b
        else:
            return fun(b,a%b)
    min = 0
    for i in range(len(a)-1):
        if a[i]<a[i+1]:
            min = fun(a[i+1],a[i])
        else:
            min = fun(a[i],a[i+1])
        a[i+1]=min
    return min*len(a)  # smallest possible sum of all numbers in Array