import unittest
"""
Routing number validation

Check Digit algorithm test
Input is a string
When 3(d1 + d4) + 7(d2 + d5 + d8) + 1(d3 + d6 + d9) mod 10 = 0, return True - Passed digits are a valid routing number
When False - Digits are not a valid number

Take input of string
Separate numbers to different elements
Do a validation for 9 digits total, otherwise False
Pass each digit into the stated equation to check for validity

Definitions
Checksum: A type of hash function to verify the input file sent is the same as the initial file that was hashed. Typical hashing algorithms used for checksum MD5, SHA-1, SHA-256, and SHA-512.
checksums are used to ensure the file has not changed during transmission

Check digit:

Collision attack: The ability to generate the same hash for two different inputs. E.g. Two rental agreements with different rents but they generate the hash output, you can falsify the rental agreement by having the identical output.
md5 and SHA-1=> both are severely compromised

SHA-256/SHA-3 are the new standard

Salt:
Adding salt to a password for hashing ensures additional security. Salt should not be too short and should not be reused for multiple users as it makes it brittle.

"""

def is_valid_routing_number(input: str) -> bool:
    try:
        digits = [int(digit) for digit in input]
    except (ValueError, TypeError):
        return False

    if len(digits) != 9:
        return False
    else:
        d1 = digits[0]
        d2 = digits[1]
        d3 = digits[2]
        d4 = digits[3]
        d5 = digits[4]
        d6 = digits[5]
        # d7 = digits[6] - not used for the verification
        d8 = digits[7]
        d9 = digits[8]

        total = (3 * (d1 + d4) + 7 * (d2 + d5 + d8) + 1 * (d3 + d6 + d9)) % 10

        if total == 0:
            return True
        else: 
            return False


if __name__ == "__main__":

    # check for valid routing number
    num = '111000025'
    result = is_valid_routing_number(num)
    assert result == True

    # check for invalid routing number
    num = '111000026'
    result = is_valid_routing_number(num)
    assert result == False

    # checks routing number length
    num = '11100002'
    result = is_valid_routing_number(num)
    assert result == False

    # non-numeric
    num = '111abcd25'
    result = is_valid_routing_number(num)
    assert result == False

    # null/undefined
    num = None
    result = is_valid_routing_number(num)
    assert result == False

    # empty string
    num = ""
    result = is_valid_routing_number(num)
    assert result == False

