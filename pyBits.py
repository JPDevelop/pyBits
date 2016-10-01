def readBitsFromFile(fileName):  # Returns a two-dimensional list: in 
each byte 8 bits
    """
    Example: text.txt with the content of: abc
    Gets 'text.txt'
    Returns: [[0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 0], [0, 
1, 1, 0, 0, 0, 1, 1]]
    """

    with open(fileName, "rb") as inputFile:  # Open the file
        fileContent = inputFile.read()  # Reads the file as bytes and 
saves it to fileContent
        # Example: Returns b'abc'
    unpackedData = list((i for i in fileContent)) # Separate each 
character into a list
    # Example: [b'a', b'b', b'c']
    stringBytesArray = list(bin(i).replace('0b', '') for i in 
unpackedData)  # Convert the values into real binary numbers which are 
represented in Unicode
    # Example: ['1100001', '1100010', '1100011']
    for i in range(0, len(stringBytesArray)):
        stringBytesArray[i] = stringBytesArray[i].zfill(8)  # Fill the 
bytes with zeros to 8 bits (left side zero padding)
        # Example: ['01100001', '01100010', '01100011']

    bitsArray = [[0 for x in range(8)] for y in 
range(len(stringBytesArray))]  # Create a two-dimensional array with 
the length of the file's data and 8 for bits (bytes length)
    # Example: [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0]] the length of the characters in the text(number of 
bytes) is 3 and 8 bits in each byte

    for i in range(0, len(stringBytesArray)):  # Range from zero to the 
length of characters in the text(number of bytes)
        for k in range(0, 8):  # 0 - 7 to cycle through each bit
            bitsArray[i][k] = int(stringBytesArray[i][k]) # Convert 
each bit to int and insert it to "bitArray"
    return bitsArray  # Return the two-dimensional array
    # Example: [[0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 0], [0, 
1, 1, 0, 0, 0, 1, 1]]


def bits2bytes(bytesArray):  # Gets a two-dimensional list of bits and 
converts it into one-dimensional list of bytes
    """
    Example: Gets A two-dimensional bits array:
    [[0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 
0, 0, 1, 1]]

    Returns: ['01100001', '01100010', '01100011']
    """

    newBytes = []  # Create an empty list which will contain the bytes
    for i in bytesArray:  # Cycle through the first dimension of the 
list (Through the bytes)
        bits = ''  # Create an empty string which will join all the 
bits into one byte
        for k in i:  # Cycle through the second dimension of the list 
(Through the bits)
            bits += str(k)  # Join each bit to the final byte
        newBytes.append(bits)  # Append the new byte as a string into 
the final list
    return newBytes


def writeBytesToFile(fileName, Bytes):
    """
    Example: Gets a filename of 'output.txt' and this list of bytes:
    ['01100001', '01100010', '01100011']
    Writes it to a the file 'output.txt' with the content of 'abc'
    Returns None
    """
    with open(fileName, "wb") as output:  # Opens a file and writes to 
it in bytes
        for i in Bytes:  # Cycles through each byte
            output.write(int(i, 2).to_bytes(1, 'big'))  # Convert the 
byte into real byte class and writes it to the file as a byte
    return None


def readBitsFromText(data):  # Gets plain text and returns 
two-dimensional array of bits
    """
    Example: Gets 'abc'
    Returns: [[0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 0], [0, 
1, 1, 0, 0, 0, 1, 1]]
    """
    encodedData = data.encode()  # Encode the data into a byte type
    # Example: 'abc' into b'abc'
    unpackedData = list(i for i in encodedData)  # Separate each 
character into a list
    # Example: [b'a', b'b', b'c']
    stringBytesArray = list(bin(i).replace('0b', '') for i in 
unpackedData)  # Convert the values into real binary numbers which are 
represented in Unicode
    # Example: ['1100001', '1100010', '1100011']

    for i in range(0, len(stringBytesArray)):
        stringBytesArray[i] = stringBytesArray[i].zfill(8)  # Fill the 
bytes with zeros to 8 bits (left side zero padding)

    bitsArray = [[0 for x in range(8)] for y in 
range(len(stringBytesArray))]  # Create a two-dimensional array with 
the length of the input text and 8 for bits (bytes length)

    for i in range(0, len(stringBytesArray)):  # 0 - 7 to cycle through 
each bit
        for k in range(0, 8):
            bitsArray[i][k] = int(stringBytesArray[i][k])  # Convert 
each bit to int and insert it to "bitArray"
    return bitsArray  # Return the two-dimensional array
    # Example: [[0, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 0], [0, 
1, 1, 0, 0, 0, 1, 1]]


def getTextFromBytes(bytesArray):  # Gets bytes array and returns plain 
text
    """
    Example:
    Gets ['01100001', '01100010', '01100011']
    Returns: 'abc'
    """
    joinedData = ''  # Create an empty string which will store the 
joined text after the conversion
    for i in range(0, len(bytesArray)):  # Cycle through each byte
        # Example: i = o, bytesArray[i] = '01100001'
        bytesArray[i] = '0b' + bytesArray[i]  # Add 0b to represent a 
byte type
        # Example: bytesArray[i] = '0b01100001'
        bytesArray[i] = int(bytesArray[i], 2)  # Convert the byte type 
into base 10 number (regular number)
        # Example: bytesArray[i] = 97
        bytesArray[i] = chr(bytesArray[i])  # Convert the number into a 
character which is represented in Unicode
        # Example: bytesArray[i] = 'a'
        joinedData += bytesArray[i]  # Join all the characters into one 
string
        # Example: i = o, joinedData = 'a', i = 1, joinedData = 'ab', i 
= 2, joinedData = 'abc'
    return joinedData  # Return the joined string (plain text)
    # Example: 'abc'

