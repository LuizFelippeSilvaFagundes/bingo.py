"""written for python 3x"""
def generate_card():
    import random
    bingocard = ['b', 'i','n', 'g', 'o'] * 5
    for i in range(25):
        if i == 13:
            bingocard.insert(i, 'free')
        else:
            val = (bingocard[i] + str(random.randint(1,25)))
            while val in bingocard:
                val = (bingocard[i] + str(random.randint(1,25)))
            else:
                bingocard.insert(i, val)
    
print(generate_card())
