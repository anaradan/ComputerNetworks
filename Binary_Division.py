## Modulo-2 binary divison

# Returns XOR of 'a' and 'b' (both of same length)
def xor(a, b):
    # initialize result
    result = []
 
    # Traverse all bits, if bits are same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
 
 
# Performs Modulo-2 division
def mod2div(divident, divisor):
    result = ""
    # Number of bits to be XORed at a time.
    pick = len(divisor)
 
    # Slicing the divident to appropriate length for particular step
    tmp = divident[0 : pick]
 
    while pick < len(divident):
        if tmp[0] == '1':
            
            # replace the divident by the result of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + divident[pick]
            result = result + "1"  # append 1 to result
 
        else:

            # If leftmost bit is '0' we need to use an all-0s divisor.
            tmp = xor('0'*pick, tmp) + divident[pick]
            result = result + "0"
 
        # increment pick to move further
        pick += 1
 
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
        result = result + "1"
    else:
        tmp = xor('0'*pick, tmp)
        result = result + "0"
 
    print ("Result is: ", result)
    print ("Reminder is :", tmp)

# Driver code
data = "1001110"
key = "1011"

mod2div(data, key)
