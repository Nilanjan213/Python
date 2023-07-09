l=[4,1,2,7,3,5,9]
print('The list is',l)
l.sort()
print('The sorted list is',l)
a=int(input('Enter a number: '))
if a<l[0] or a==l[0]:
     l.insert(0,a)
if a>l[len(l)-1] or a==l[len(l)-1]:
     l.insert(len(l),a)
else:
     s=a
     while a>l[0] :
          p=s-1
          if s not in l:
               s=s-1
          if p in l:
               x=l.index(p)
               l.insert(x+1,a)
               break
print('After insertion the list is',l)
               
          
