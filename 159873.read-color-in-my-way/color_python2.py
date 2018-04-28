#!/bin/python

# original
f = lambda c, o, t: '#' + ''.join(c[o.find(v):][:2] for v in t[1::2])

# let's expand on this

# make it a function to work with it a little more easily
def color_swap(c,o,t):
    return '#' + ''.join(c[o.find(v):][:2] for v in t[1::2])

# better parameter names
def color_swap(color, from_string, to_string):
    return '#' + ''.join(color[from_string.find(v):][:2] for v in to_string[1::2])


# break out getting the order to put the pairs in
def color_swap(color, from_string, to_string):

    to_order = to_string[1::2]

    return '#' + ''.join(color[from_string.find(v):][:2] for v in to_order)

# break out list comprehension
def color_swap(color, from_string, to_string):
    to_order = to_string[1::2]

    color_pairs = []

    for item_index in to_order:

        # get index in the from string
        index_in_from = from_string.find(item_index)

        # get everything in the string after that point
        index_on_string = color[index_in_from:]

        # get the pair of characters
        color_pair = index_on_string[:2]

        color_pairs.append(color_pair)

    color_string = ''.join(color_pairs)


    return '#' + color_string

# tests
print f('#12345678', '#RRGGBBAA', '#AARRGGBB')  # 78123456
print f('#1A2B3C4D', '#RRGGBBAA', '#AABBGGRR')  # 4D3C2B1A
print f('#DEADBEEF', '#AARRGGBB', '#GGBBAARR')  # BEEFDEAD

print color_swap('#12345678', '#RRGGBBAA', '#AARRGGBB')   # 78123456
print color_swap('#1A2B3C4D', '#RRGGBBAA', '#AABBGGRR')   # 4D3C2B1A
print color_swap('#DEADBEEF', '#AARRGGBB', '#GGBBAARR')   # BEEFDEAD
