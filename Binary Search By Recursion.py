L=[2,4,6,1,2,3,7]
print("The given list is",L)
x=int(input('Enter the element to be searched: '))
def fun(L,l,u):
     L.sort()
     m=int((l+u)/2)
     if L[m]==x:
          print('In sorted list',L,'the element is present in',m+1,'th position')
          if L[m+1]==x:
               m=m+1
               print('In sorted list',L,'the element is present in',m+1,'th position')
          else:
               return 0
     elif x<L[m]:
          u=m+1
          fun(L,l,u)
     else:
          l=l+1
          fun(L,l,u)
l=0
u=len(L)
fun(L,l,u)
