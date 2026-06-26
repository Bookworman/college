import math

def solve(a,b,c):
    if a == 0:
        return(-c / b)
    
    D = b**2 - 4*a*c

    if D == 0:
        root = -b / (2*a)
        return(root)
    else:
        sqrt_D = math.sqrt(D)
        x1 = (-b - sqrt_D) / (2 * a)
        x2 = (-b + sqrt_D) / (2 * a)
        return(min(x1, x2),max(x1, x2))

print(solve(1, -4, -5))
print(solve(-2, 7, -5))
print(solve(1, 2, 1))
