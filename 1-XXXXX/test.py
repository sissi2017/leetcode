s=['(',')','[',']']
a = {')':'(', ']':'[', '}':'{'}
l = []
for i in s:
    if i in a and a[i] == l[-1]:
        l.pop()
    else:
        l.append(i)
    print(i,'\n',a,'\n',l)
    print(len(l)==0)
