x = float(raw_input('Input:'))

def wurzel(x):
    if x > 1:
            return wurzel(x) / 2
    else:
        return 1
