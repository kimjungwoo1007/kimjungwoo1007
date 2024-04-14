n=int(input("몇단까지 출력할까요?"))
for i in range (1,n+1) :
    print("------[",i,"단]------")
    for j in range (1,20) :
         print(i,"x",j,"=",i*j)