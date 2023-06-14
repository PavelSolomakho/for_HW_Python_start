from fractions import Fraction

def sum_and_product(frac1, frac2):
    numerator1, denominator1 = map(int, frac1.split("/"))
    numerator2, denominator2 = map(int, frac2.split("/"))
    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)
    sum_fraction = fraction1 + fraction2
    product_fraction = fraction1 * fraction2
    return sum_fraction, product_fraction
  
frac1 = input("Введите первую дробь: ")
frac2 = input("Введите вторую дробь: ")
sum_frac, product_frac = sum_and_product(frac1, frac2)
print("Сумма дробей:", sum_frac)
print("Произведение дробей:", product_frac)
