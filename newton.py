def newton_raphson(f, df, x0, tol=1e-7, max_iter=100):
    results = []
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("La derivada es cero. No se puede continuar.")
        x_new = x - fx/dfx
        results.append((i, x, fx))
        if abs(x_new - x) < tol:
            results.append((i+1, x_new, f(x_new)))
            break
        x = x_new
    return results