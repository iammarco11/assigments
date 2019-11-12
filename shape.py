X=[0,100,100,0]
Y=[0,0,100,100]

main=[]
for i in range(len(X)):
    temp=[]
    for j in range(1):
        temp.append(X[i])
        temp.append(Y[i])
        main.append(temp)
print(main)