
flag = False
# Pawan Kumar
# ID: 2046222
coef_a = int(input())
coef_b = int(input())
coef_c = int(input())
coef_d = int(input())
coef_e = int(input())
coef_f = int(input())


for x in range(-10, 10):
    for y in range(-10, 10):
        if (coef_d * x + coef_e * y == coef_f) and (coef_a * x + coef_b * y == coef_c):
            flag = True
            print(x,y)

if flag == False:
    print('No solution')