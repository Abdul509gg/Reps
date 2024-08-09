
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

principal = float(input("500"))
rate = float(input("10"))
time = float(input("3"))

simple_interest = calculate_simple_interest(principal, rate, time)
print(" simple interest ")
