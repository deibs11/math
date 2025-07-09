def runge_kutta(f, x0, y0, h, n):
    results = []
    x = x0
    y = y0
    for i in range(n):
        results.append((i, x, y))
        k1 = f(x, y)
        k2 = f(x + h/2, y + h*k1/2)
        k3 = f(x + h/2, y + h*k2/2)
        k4 = f(x + h, y + h*k3)
        y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        x = x + h
    results.append((n, x, y))
    return results