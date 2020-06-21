def binarySum(firstBinaryString: str, secondBinaryString: str) -> str:
    """
    -- Return the binary sum of two binary numbers
    -- Binary numbers must be strings

    >>> binarySum('1111', '1110')
    '11101'

    >>> binarySum('101', '101')
    '1010'

    """
    if len(firstBinaryString) > len(secondBinaryString):
        secondBinaryString = secondBinaryString.zfill(len(firstBinaryString))
    elif len(firstBinaryString) < len(secondBinaryString):
        firstBinaryString = firstBinaryString.zfill(len(secondBinaryString))

    length = len(firstBinaryString)

    carry = 0
    revResult = ''

    for i in range(length-1, -1, -1):
        firstBit = int(firstBinaryString[i])
        secondBit = int(secondBinaryString[i])
        
        # Ripple Full Adder circuit imitation
        revResult = revResult + str(firstBit ^ secondBit ^ carry)
        carry = (firstBit and secondBit) or (secondBit and carry) or (carry and firstBit)

    if carry == 1:
        revResult = revResult + str(carry)

    return revResult[::-1]

if __name__ == '__main__':
    print("Enter the first binary string:")
    first = input()

    print("Enter the second binary string:")
    second = input()

    result = binarySum(first, second)

    print("The sum of binary strings is:")
    print(result, end = '')