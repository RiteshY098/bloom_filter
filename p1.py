
a = int(input("enter the number ")) 
arr = []                               # create empty list/ array
arr = [0 for k in range (8)]           # fill that list with zeros and range describes the number of zeros in that list 
def decimaltobinary(n):                # from line 5 - 9 i had converted a number into binary 
    return "{0:b}".format(int(n)) 
if __name__ == '__main__':
    b = decimaltobinary(a)
    print(b)
    c = [int(x) for x in str(b)]
    print(c)                          # here you can find the binary conversion of imput number
    for i in range(len(c)):           # this loop is usually for seperating even and odd 
        if c[i] % 2 != 0:              
            d = c[::2]
            print(d)
            ov = 0
            for ele in d:
                ov = (ov << 1) | ele    # converting back even binary number into its corresponding value 
            print(ov)                 
            e = c[1::2]               #for odd 
            print(e)
            pv = 0
            for ele in e:
                pv = (pv << 1) | ele   # converting back odd binary number into its corresponding value
            print(pv)
            break
        elif c[i] % 2 != 0:           #useless 
            d = c[1::2]
            print(d)
            e = c[::2]
            print(e)
print(arr) 

#replacing 0 by 1 at particular position we get from even and odd 
arr[ov] = 1   
arr[pv] = 1
print(arr)









