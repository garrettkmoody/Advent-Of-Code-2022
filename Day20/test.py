#!/usr/bin/env python3
# 2022 Day 20: Grove Positioning System

def process_input(filename):
    """Acquire input data"""
    with open(filename) as file:
        input = file.read().splitlines()

    encrypted = [int(x) for x in input]

    return encrypted


def decode(encrypted, decoded):

    for i, number in enumerate(encrypted):
        encrypted_number = (i,number)
        current_position = decoded.index(encrypted_number)
        if number == 0:
            continue        # 0 doesn't move

        # The original item has to be removed FIRST, because it can be
        # moved left or right for more positions than the length of the
        # list, in which case it doesn't count the position it was 
        # previoulsy at -- because the number is MOVING
        del decoded[current_position]

        new_position = current_position + number
        new_position %= len(decoded)
        if new_position < 0:
            new_position += len(decoded)
        decoded.insert(new_position,encrypted_number)

    return decoded


def nth_number(decoded,from_pos,n):
    """Return nth number after from_pos"""
    pos = from_pos + n
    pos %= len(decoded)
    i, nth = decoded[pos]
    return nth

#-----------------------------------------------------------------------------------------

filename = 'input.txt'
#filename = 'sample.txt'

decryption_key = 811589153
mix_count = 1

encrypted = process_input(filename)

encrypted = [x * decryption_key for x in encrypted]
print(encrypted)

# Change each number to a tuple: (original_position,number)
# This allows the number to be uniquely identified in the list, even
# though input numbers are NOT unique
decoded = [(i,x) for i,x in enumerate(encrypted)]

for n in range(mix_count):
    decoded = decode(encrypted,decoded)
    break

print(decoded)
encrypted_zero_pos = encrypted.index(0)
zero_number = (encrypted_zero_pos,0)
zero_pos = decoded.index(zero_number)

coord1 = nth_number(decoded,zero_pos,1000)
coord2 = nth_number(decoded,zero_pos,2000)
coord3 = nth_number(decoded,zero_pos,3000)
coord_sum = coord1 + coord2 + coord3
print()
print('Coordinate sum =', coord_sum)
print()
