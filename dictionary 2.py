dic = {}

while True:
    print("1.create vocab")
    print("2.print all info")
    print("3.english to chinese")
    print("4.chinese to english")
    print("5.test")
    print("6.leave system")
    sel = input("insert option: ")
    if sel=="1":
        en = input("enter english: ")
        ch = input("enter chinese: ")
        dic[en]=ch
    elif sel=="2":
        for k,v in dic.items():
            print(k,":",v)
    elif sel=="3":
       search = input("search english: ")
       print(dic[search])
    elif sel=="4":
       search1 = input("search chinese: ")
       for k,v in dic.items():
           if search1 == v:
               print(k)
    elif sel=="5":
        score=0
        for k,v in dic.items():
            print(v,":")
            ans = input("insert answer: ")
            if ans==k:
                print("u got it right")
                score=score + 1
        print("your score: ",score)
       
    elif sel=="6":
        break
            