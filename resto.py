#!/usr/bin/env python3

fxrate = 1.955803

def bgn_to_eur(amount_bgn):
    return amount_bgn / fxrate
def eur_to_bgn(amount_eur):
    return amount_eur * fxrate

if __name__ == "__main__":
    bill = float(input("Enter amount to be payed: "))
    customer_gave = input("Enter currency the customer gave (BGN or EUR): ").strip().upper()
    amount = float(input("Enter amount given by the customer: "))
    
    if customer_gave == "BGN":
        resto = bill - bgn_to_eur(amount)
    elif customer_gave == "EUR":
        resto = bill - amount
    
    resto_bgn = eur_to_bgn(resto)
    print(f"Change to give back: {resto_bgn:.2f} BGN")
    print(f"Change to give back: {resto:.2f} EUR")
