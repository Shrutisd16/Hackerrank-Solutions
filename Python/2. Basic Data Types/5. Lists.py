# Lists

if __name__ == '__main__':
    N = int(input())
    list1 = list()
    
    for _ in range (N):
        lst = input().split()
        if (lst[0]== "print"):
            print(list1)
        elif (lst[0] == "insert"):
            list1.insert(int(lst[1]), int(lst[2])) 
        elif (lst[0] == "remove"):
            list1.remove(int(lst[1]))
        elif (lst[0] == "append"):
            list1.append(int(lst[1]))
        elif (lst[0] == "sort"):
            list1 = sorted(list1)
        elif (lst[0]=="pop"):
            list1.pop()
        elif(lst[0] == "reverse"):
            list1.reverse()
