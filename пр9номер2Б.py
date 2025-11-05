def second_largest():
    num= []
    c= int(input())

    for i in range(c):  
        n = int(input("Введите число: "))
        num.append(n)  
    max1 = max(num) 
    num.remove(max1)  
    max2 = max(num)  
    return max2
max2 = second_largest()
print("Второе наибольшее число:", max2)
