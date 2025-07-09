def euler_mejorado(f, x0, y0, h, n):
    results = []
    x = x0
    y = y0
    for i in range(n):
        results.append((i, x, y))
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y = y + (h / 2) * (k1 + k2)
        x = x + h
    results.append((n, x, y))
    return results