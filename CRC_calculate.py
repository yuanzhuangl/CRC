star_string = '*' * 30;

def XOR(a, b):
    t = ""
    for i in range(0, len(a)):
        if int(a[i]) == int(b[i]):
            t += "0"
        else:
            t += "1"
    return t


def computeCRC():
    Mx = input("Input the message unit that are transmitted: ")
    rawMx = Mx
    Gx = input("Input the reference polynomial: ")
    Gx = Gx[1:]
    n = len(Gx)
    for i in range(0, n):
        Mx += "0"
    Rx = "0" * n
    t = ["0" * n, Gx]
    for i in range(0, len(Mx)):
        tmp = Rx[0]
        Rx = Rx[1:] + Mx[i]
        Rx = XOR(Rx, t[int(tmp)])
    print("\n\n %s \nThe Reminder is : %s and the string to be transmitted is : %s \n %s" % (star_string, Rx, rawMx + Rx,star_string))


def CRCcheck():
    Px = input("Input the transmission string: ")
    Gx = input("Input the reference polynomial: ")
    Gx = Gx[1:]
    n = len(Gx)
    Rx = "0" * n
    t = ["0" * n, Gx]
    for i in range(0, len(Px)):
        tmp = Rx[0]
        Rx = Rx[1:] + Px[i]
        Rx = XOR(Rx, t[int(tmp)])
    if Rx == "0" * n:
        print("No error.")
    else:
        print("The frame is in error! And the reminder is : %s \n" % Rx)

if __name__ == '__main__':
    Tag = '100'
    while Tag != '0':
        Tag = input("Input '1' to generate transmission message,input '2' to check transmission message,input '0' to exit: ")
        if Tag == "1":
            computeCRC()
        elif Tag == "2":
            CRCcheck()
        elif Tag == "0":
            break
        else:
            print(Tag)
            print("Illegal input, please try again!\n")
