pin = "881120-1068234"
yyyymmdd = pin[:6]
print(yyyymmdd)
num = pin[7:]
print(num)

if pin[7] == '1':
    print('남')
else: print('여')
print(pin[7])



a = [1,3,5,4,2]
a.sort()
b = a
print(a)
print(b)
a.reverse()
print(a)


a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)