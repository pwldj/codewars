class Primes:
    @staticmethod
    def stream():
        n=16000000
        l = [True]*n
        for i in range(3,int(len(l)**0.5)+1):
            if i&1 and l[i]:
                l[i*2::i] = [False]*((n-1)//i-1)
        yield 2
        for i in range(3,n,2):
            if l[i]:
                yield i