## Implements CRC 32

import codecs

# create table creates lookup table for faster calculating
# it's possible to calculate reminder for given divisior and divider
# message is calculated byte by byte instead of bit by bit
def create_table():
    #table declaration
    table = []
    #calculates reminder of each possible divider
    for i in range(256):
        rem = i  #reminder
        for j in range(8):
            #MSB is set so there will be XOR operation with generic polynom
            #because only MSB has 1 at the end
            #generic polynom is: 0xEDB88320
            if rem & 1:
                rem >>= 1
                rem ^= 0xEDB88320
            #if MSB is not set XOR will not be executed
            #and we are moving to the next bit
            else:
                rem >>= 1
        # appending result in the table
        table.append(rem)
    return table

#function calculates CRC32 of given word
def crc_update(buf):
    #set initial value CRC to 1
    crc = 0xffffffff
    #result from the table is looked for each sign for current sign based on
    #last 8 bits
    for k in buf:
        crc = (crc >> 8) ^ crc_table[(crc & 0xff) ^ k]

    return crc ^ 0xffffffff

#Main code
crc_table = create_table()
# message that needs CRC in hex value 
message = 'FAFAFA'
#coversion to binary
message_bin = bin(int(message, 16))

#print message in hex and binary
print ("Ulazna poruka je: %s (%s)" %(message_bin, '0x' + message))

#crc_update calculates rest of message
checksum = crc_update(codecs.decode(message, 'hex'))

#print reminder in binary and hex
print ("Rezultat je: %s (%s)" %(bin(checksum), hex(checksum)))

#forming message that is sent through canal drom original mesaage and checksum
send_mess = message_bin + bin(checksum)[2:]

#print message that is sent
print("Poruka koja se salje je: ")
print (send_mess)

