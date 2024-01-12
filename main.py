#task_1

lst =[1, 4, 5, 3, 13, 7]
result = 0

def find(lst, result):
    for x in lst:
        result+=x
    print(result)




find(lst, result)

#task_2

L = ["Xushnoza", "Sardor", "Odina", "Asad", "Malika", "Asliddin"]
x = input("Enter the letter:")

def task(L, x):
    lst =[]
    for y in L:
      if x in y:
          lst.append(y)
    return sorted(lst)



print(task(L, x))

#task_3
names = ["Sardor", "Odina", "Malika", "Xushnoza", "Della"]


def search(names):
    if "Odina" in names:
     return  names.index("Odina")
    else:
        return -1



print(search(names))

#task_4
lst = ["arrey", "print", "return", "index", "reverse"]
lst2 = ["arrey", "print", "return", "index", "reserve"]

def clone(msv, msv2):
    for num in msv:
        for num2 in msv2:
            if num == num2:
                print("1")
                break
        else:
            print("-1")


clone(lst,lst2)


#task_5
ls5 = [3,4]
ls6 = [4,7]

def subset(ls5, ls6):
    for x in ls5:
        if x in ls6:
            return True
        break
    else:
        return False
print(subset(ls5, ls6))


#Task_6
unique_sort = [1, 4, 3, 2, 3]


def search(unique_sort):
    a = sorted(unique_sort)
    for x in a:
        if x in a.count(x)!=1:
            a.remove(x)
            print(a)





print(search(unique_sort))


#task_7

arguement = ["scumbag", "idiot", "stupid", "foolish", "acc"]
total = []

for x in arguement:
    lst = ["idiot", "moron", "scumbag"]
    if x ==lst:
        total.append(x)
        print(total)
    else:
        print("It is not a insulting word")
        break


#Task_8

lst = [-5, -3, 7, -12, 5, -1, 3]
lst2 = []

def morethan0(msv, msv2):
    for num in msv:
        if num > 0:
            lst2.append(num)
    print(msv2)


morethan0(msv=lst, msv2=lst2)

#Task_9
d = [1, 2, 3, 4, 5]
a = []

def high_low(d):
    result = max(d)
    result1 = min(d)
    a.append(result)
    a.append(result1)
    print(a)


high_low(d)

# #Task_10
lst = [10, 5, 3, 7, 8]
inp = int(input("Enter number: "))

def append(msv, input):
    for num in msv:
        if num == input:
            lst.remove(num)
            lst.append(num)
            print(msv)
            break
    else:
        print("we don't have this number")


append(lst, inp)






