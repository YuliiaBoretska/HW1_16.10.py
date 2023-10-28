#-*- coding: <encoding-name> -*-
x = int(input('Enter a five-digit number:'))
#x = int(56789)
w = x % 10 #1
e = x % 100-w #20
r = x % 1000-w-e #300
t = x % 10000-w-e-r #4000
y = x // 10000 #5
x = int((w*10000) + (e*100) + r + (t/100) + y)
print(w, e, r, t, y, x)

#w = int(x/10000) #5
#e = int(x-w*10000)//1000*10#40
#r = int(x-w*10000-e*100)//100*100 #300
#t = int(x-w*10000-e*100-r)//10*1000 #2000
#y = int(x-w*10000-e*100-r-t/100)*10000 #10000
#p = w+e++r+t+y
#print(p)
