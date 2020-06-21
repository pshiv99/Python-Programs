def binarySum(firstBinaryString: str, secondBinaryString: str) -> str:
    """
    -- Return the binary sum of two binary numbers
    -- Binary numbers must be strings

    >>> binarySum('1111', '1110')
    '11101'

    >>> binarySum('101', '101')
    '1010'

    """
    carry = 0
    revResult = ''

    iter1 = iter(firstBinaryString[::-1])
    iter2 = iter(secondBinaryString[::-1])

    for firstBit, secondBit in (map(int, i) for i in zip(iter1, iter2)):
        # Ripple Full Adder circuit imitation
        revResult = revResult + str(firstBit ^ secondBit ^ carry)
        carry = (firstBit and secondBit) or (secondBit and carry) or (carry and firstBit)

    for firstBit in map(int, iter1):
        revResult = revResult + str(firstBit ^ carry)
        carry = firstBit and carry

    for secondBit in map(int, iter2):
        revResult = revResult + str(secondBit ^ carry)
        carry = secondBit and carry

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