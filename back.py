def dis_calc (a, b, c):

    di = ((b**2) - (4 * a * c))

    if di > 0:
        x = (- b + di**0.5) / (2 * a)
        y = (- b - di**0.5) / (2 * a)
        return x, y
    if di == 0:
        x = - b / 2 * a
        return x
    if di < 0:
        return 0