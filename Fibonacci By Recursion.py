def fib(n,a=0,b=1,s=0):
     if s<1:
          print(a,b,end=' ')
          s=2
     if s>1:
          if s==n:
               return 0
          else:
               c=a+b
               print(c,end=' ')
               a=b
               b=c
               s=s+1
               fib(n,a,b,s)
n=int(input('Enter the no. of terms: '))
fib(n)
               
          
          
