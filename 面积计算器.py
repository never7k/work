def rectangle(l,w):
    S =l*w
    S = float(S)
    print("长方形面积=",S)
def square(a):
    S =a*a
    print("正方形面积=",S)
def round(r):
    S =3.1415926535898*r*r
    print("圆形面积=",S)
print("--------------欢迎使用面积计算器----------------------")
print("请输入要计算面积的图形：\n1.长方形\n2.正方形\n3.圆形\n0.退出")
k = input()
k = int(k)
if k == 1:
    l = input("请输入长方形的长：")
    l = float(l)
    w = input("请输入长方形的宽：")
    w = float(w)
    rectangle(l,w)
    input()
if k == 2:
    a = input("请输入正方形的边长：")
    a = float(a)
    square(a)
    input()
if k == 3:
    r = input("请输入圆形的半径：")
    r = float(r)
    if r == 0:
        d = input("请输入圆形的直径：")
        d = float(d)
        r = d/2
        r = float(r)
        round(r)
        input()
    elif r != 0:
        round(r)
        input()
if k == 0:
    input("按任意键可退出")

