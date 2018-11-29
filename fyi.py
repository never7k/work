print("----------------------------------Korn----------------------------------")
say = input("冯毅是什么？")
if say =="冯裤子":
        print("猜对了！")
else:
        print("猜错了！") 
        while say != "冯裤子":
                say = input("冯毅是什么？")
                if say == "冯裤子":
                        print("猜对了！")
                else:
                        print("猜错了！")

print("行吧，先这么着吧！")
