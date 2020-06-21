def longestPalindromeSubstring(string: str) -> str:
    """
    -- Return the longest palindrome substring of a string
    -- In case of two or more longest panlindrome substrings, returns the one with
    the least starting index in the original string

    >>> longestPalindromeSubstring('mom')
    'mom'

    >>> longestPalindromeSubstring('nitik')
    'niti'

    """

    length = len(string)

    substrings = [string[i:j+1] for i in range(length) for j in range(i, length)]
    palindrome_substrings = list(filter(lambda i: i == i[::-1], substrings))
    max_length = max(map(lambda i: len(i), palindrome_substrings))
    max_palindromes = list(filter(lambda i: len(i) == max_length, palindrome_substrings))

    return max_palindromes[0]

if __name__ == '__main__':

    print('Enter string:')
    string = input()

    length = len(string)
    
    result = longestPalindromeSubstring(string)
    
    print('The longest palindrome substring is:')
    print(result)