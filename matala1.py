import  math

#Question number 1
def factorSum(n):
    # Initialize result
    sum = 0

    # Print the number of 2s that divide n
    if n % 2 == 0:
        sum += 2
        n = n / 2

    # n must be odd at this point, thus skip the even numbers and iterate only for odd
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            sum += i
            n = n / i

    # This condition is to handle the case when n is a prime number greater than 2
    if n > 2:
        sum += n

    return sum

#Question number 2.1
def f1(x):
    #Terms if the x is positive
    if x>0:
        return x+1
    # Terms if the x is positive
    else:
        return x-1

#Question number 2.2
def onlyPositive(f):
    def g(x):
        return abs(f(x))
    return g

#Question number 3
def printNumbers(start, end, index): #4
    #check if we need to skip the index
    if index==start:
        return printNumbers(start+1, end, index)
    #check if we need to print
    if start<=end:
        print(start, end=" ")
        return printNumbers(start+1, end, index)

#Question number 4
def interceptPoint(tuple1, tuple2):
    #initialize x and y
    try:
        x=abs((tuple1[1]-tuple2[1])/(tuple1[0]-tuple2[0]))
        y=(tuple1[0]*x+tuple1[1])
    #Handle division by zero
    except ZeroDivisionError:
        return "none"
    else:
        return (x,y)

#Question number 5
def listProduct(list):
    #initialize the new list
    new_list=[]
    for i in range(len(list[0])):
        for j in range(list[1][i]):
            new_list.append(list[0][i])
    return new_list


#Question number 6
def analyze(string):
    tmp_str = ""
    tmp = 0
    # Iterate over the string
    for i in range(len(string)):
        if string[i] != ',' and string[i] != ' ':
            tmp_str += string[i]
        else:
            if tmp_str and float(tmp_str) >= 85:
                tmp += 1
            tmp_str = ""
    # Check if the last term is Exellent
    if float(tmp_str) >= 85:
        tmp += 1
    return tmp


if __name__ == "__main__":
    #Question number 1
    print(factorSum(36))

    #Question number 2
    g = onlyPositive(f1)
    print(g(-2))

    #Question number 3
    print(interceptPoint((3,11), (5,1)))

    #Question number 4
    printNumbers(1, 5, 3)

    #Question number 5
    list=[[6,7,8], [2,1,3]]
    print(listProduct(list))

    #Question number 6
    grades="45 , 65, 70.4 , 82.6 , 20.1 , 90.8 , 76.1 , 67.1 , 79.9, 85.1"
    print(analyze(grades))






