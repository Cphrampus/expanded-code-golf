# original
f = lambda x, a, b: ['#'] + [[x[i:i + 2] for i in range(1, len(x), 2)][i] for i in [a[1::2].index(i) for i in b[1::2]]]

# let's expand on that

# let's make it a function

def color_swap(x,a,b):
    return ['#'] + [[x[i:i + 2] for i in range(1, len(x), 2)][i] for i in [a[1::2].index(i) for i in b[1::2]]]

# let's get some better parameter names

def color_swap(color, from_string, to_string):
    return ['#'] + [[color[i:i + 2] for i in range(1, len(color), 2)][i] for i in [from_string[1::2].index(i) for i in to_string[1::2]]]

# ok, let's break that return apart a bit

def color_swap(color, from_string, to_string):

    # get order of swaps to make
    swaps = [from_string[1::2].index(i) for i in to_string[1::2]]

    return ['#'] + [[color[i:i + 2] for i in range(1, len(color), 2)][i] for i in
                    swaps]

# still more breaking out to do

def color_swap(color, from_string, to_string):

    # get order of swaps to make
    swaps = [from_string[1::2].index(i) for i in to_string[1::2]]

    # get the two character pairs
    color_chunks = [color[i:i + 2] for i in range(1, len(color), 2)]

    return ['#'] + [color_chunks[i] for i in swaps]

# let's break up the swaps assignment a little more

def color_swap(color, from_string, to_string):

    # get the order of the two strings
    to_string_order = to_string[1::2]
    from_string_order = from_string[1::2]

    # get the swaps to make
    swaps = [from_string_order.index(i) for i in to_string_order]

    # get the two character pairs
    color_chunks = [color[i:i + 2] for i in range(1, len(color), 2)]

    # for each swap(index of needed one), get the correct color pair
    return ['#'] + [color_chunks[i] for i in swaps]

# tests
test_cases = [['#12345678', '#RRGGBBAA', '#AARRGGBB'], ['#1A2B3C4D', '#RRGGBBAA', '#AABBGGRR'],
              ['#DEADBEEF', '#AARRGGBB', 'GGBBAARR']]

for i in test_cases:
    print(f(i[0], i[1], i[2]))
    print(color_swap(i[0], i[1], i[2]))

