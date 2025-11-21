def calc(distance, litres_per_kilometres, price_per_litre):
    """

    args:
        distance, litres_per_kilometres, price_per_litre: float
    returns:
        float: total price, litres needed

    """

    total_litres = distance * (litres_per_kilometres / 100)
    total_price = total_litres * price_per_litre
    return total_price, total_litres

distance = float(input("Which distance(km) will you ride? "))
litres_per_kilometres = float(input("How much litres per 100 km? "))
price_per_litre = float(input("How much dollars per litre of gasoline? "))
total_price, total_litres = calc(distance, litres_per_kilometres, price_per_litre)

print("Need gasoline: ", total_litres, "\nTotal price of ride: ", total_price)