import random
def XOR(a, b):
    t = ""
    for i in range(0, len(a)):
        if int(a[i]) == int(b[i]):
            t += "0"
        else:
            t += "1"
    return t
# Generate a random binary number of 1520 bytes
lenMx = 1520 * 8
Mx='1' + ''.join([random.choice('01') for i in range(0,lenMx-1)])
print ("The random binary number of 1520 bytes : \n %s \n" % Mx)
rawMx = Mx

# Generate standard CRC-32 polynomial
a = [32,26,23,22,16,12,11,10,8,7,5,4,2,1,0]
Gx = ['0']* (a[0]+1)
for i in a:
    Gx[i] = '1'
Gx.reverse()
Gx = ''.join(Gx)

# Calculate the CRC string
Gx = Gx[1:]
n = len(Gx)
for i in range(0, n):
    Mx += "0"
Rx = "0" * n
t = [ "0" * n, Gx ]
for i in range(0,len(Mx)):
    tmp = Rx[0]
    Rx = Rx[1:] + Mx[i]
    Rx = XOR(Rx,t[int(tmp)])
    Px = rawMx + Rx

# define # of frames that generated and being detected
count0 = 0
count1 = 0
count2 = 0
fcount0 = 0
fcount1 = 0
fcount2 = 0

# repeat generate frames and check for 1000 times
for i in range(0,1000):
    Tag = random.choice([0,1,2])
    Px = list(Px)
    if Tag == 0:
        n = random.randint(33,len(Px))
        fcount0 += 1
    if Tag == 1:
        n = 32
        fcount1 += 1
    if Tag == 2:
        n = random.randint(1,31)
        fcount2 += 1
    errorPlace = random.sample(range(0,len(Px)),n)
    for i in errorPlace:
        if Px[i] == '1':
            Px[i] = '0'
        else:
            Px[i] = '1'
    Px = ''.join(Px)
    for i in range(0, len(Px)):
        tmp = Rx[0]
        Rx = Rx[1:] + Px[i]
        Rx = XOR(Rx, t[int(tmp)])
    if Tag == 0:
        if Rx == "0" * n:
            print ("No error.\n")
        else:
            count0 += 1
    if Tag == 1:
        if Rx == "0" * n:
            print ("No error.\n")
        else:
            count1 += 1
    if Tag == 2:
        if Rx == "0" * n:
            print ("No error.\n")
        else:
            count2 += 1

print( "# of frames(error > 32bits) : %s \n # of frames that error are detected(error < 32bits) : %s \n" %(str(fcount0),str(count0)))
print( "# of frames(error = 32bits) :" + str(fcount1) + "# of frames that error are detected(error < 32bits) :" + str(count1) +"\n")
print( "# of frames(error < 32bits) :" + str(fcount2) + "# of frames that error are detected(error < 32bits) :" + str(count2))