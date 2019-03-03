#for loop
languages = ['C', 'C++', 'Perl', 'Python']
for x in languages:
	print(x)

#for + break
sites = ['Baidu', 'Google', 'Runoob', 'Taobao']
for site in sites:
    if site == 'Runoob':
        print('菜鳥教程')
        break
    print('循環數據' + site)
else:
    print('沒有循環數據!')
print('完成循環!') 

#for + break
for letter in 'Runoob':#案例一
    if letter == 'b':
    	break
    print('當前字母為:', letter)	

var = 10
while var > 0:
    print('當期變量值為:', var)
    var = var -1
    if var == 5:
        break
print('good bye')

#for + else

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等於', x, '*', n//x)
            break
    else:
        #循環中沒有找到元素
        print(n, '是質數')  

#pass 語句
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('執行pass塊')
    print('當前字母為:', letter)
print('good bye') 

#循環語句測驗題
if None:     #測驗1
    print('hello')

for i in [1, 0]:  #測驗2
    print(i + 1)  

ia = sum = 0  #測驗3 

while ia <= 4:
    sum += ia
    ia = ia + 1

print(sum)    


for char in 'PYTHON STRING':
	if char == ' ':
		break

	print(char, end='')	

	if char == 'o':
		continue