def CommonPrifix(arr):
    # res = [""]
    # for i in range(len(arr[0])):
    if(len(arr) == 0):
        return ""
    elif(len(arr) == 1):
        return arr[0]
    elif("" in arr):
        return ""
    i=0
    flag = True
    while(flag):
        for j in range(0,len(arr)-1):
            print("began",i,j)
            # print("elements",arr[j][i],arr[j+1][i])
            if(len(arr[j]) <= i or len(arr[j+1]) <= i or arr[j][i] != arr[j+1][i]):
                print("NE")
                flag = False
                break
            print("EE")
        i+=1
    print("end",i)
    return arr[0][:i-1]

    # for i in range(len(arr[0])):
    #     flag = True
    #     for j in range(1,len(arr)):
    #         if(len(arr[j]) <= i):
    #             break
    #         if(arr[0][i] != arr[j][i]):
    #             return "".join(res)
    #         if(arr[0][i] not in res):
    #             res.append(arr[0][i])
    # return "".join(res)
# strs = ["flow","flower","flight"]
strs = ["abc","ab"]
result = CommonPrifix(strs)
print(result)


        