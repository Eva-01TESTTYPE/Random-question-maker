# test1.py
import random

oper_lib = ["+", "-", "*", "/"]
temp  = input("Please input the number of problems you want:")
number_problems = int(temp)
    
while number_problems > 0:
    current_oper_number1 = random.randint(0,3)
    current_oper_number2 = random.randint(0,3)
    current_oper_number3 = random.randint(0,3)           #随机运算种类
    
    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    number3 = random.randint(0,100)
    number4 = random.randint(0,100)            #随机运算数字

    oper_number_choose = random.randint(2,3)             #随机符号个数2/3

    if oper_number_choose == 2:                #符号个数2时

        result = eval('%d%s%d%s%d'%(number1, oper_lib[current_oper_number1], number2,oper_lib[current_oper_number2], number3))   #important:eval()函数，将符号转变为相应计算

        if result == int(result):           #判断计算结果是否为整数，否则舍弃，且不占循环次数
            print(number1,oper_lib[current_oper_number1],number2,oper_lib[current_oper_number2], number3)

            print(result)

            result = int(result)            #此处虽为整数/整数，但可得出double型（与c语不同）

            f = open("C:\\Users\\11495\\Desktop\\subject.txt", "a")               #打开/不存在则建立一个文档
            f.write("%d %s %d %s %d = %d\r\n"%(number1, oper_lib[current_oper_number1], number2,oper_lib[current_oper_number2], number3, result))         #逐个输入
            f.close()           

            number_problems -= 1      #记循环次数

    else:       #符号个数3时
        result = eval('%d%s%d%s%d%s%d'%(number1, oper_lib[current_oper_number1], number2,oper_lib[current_oper_number2], number3, oper_lib[current_oper_number3], number4))

        if result == int(result):
            print(number1,oper_lib[current_oper_number1],number2,oper_lib[current_oper_number2], number3, oper_lib[current_oper_number3], number4)

            print(result)

            result = int(result)
            
            f = open("C:\\Users\\11495\\Desktop\\subject.txt", "a")
            f.write("%d %s %d %s %d %s %d = %d\r\n"%(number1, oper_lib[current_oper_number1], number2,oper_lib[current_oper_number2], number3, oper_lib[current_oper_number3], number4,result))
            f.close() 

            number_problems -= 1

            
            

    

    

