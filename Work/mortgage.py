# mortgage.py
#
# Exercise 1.7
mortgage = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month =108
extra_payment=1000
now_payment = payment
while mortgage > 0:
    month += 1
    mortgage = mortgage * (1 + rate / 12)
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        now_payment =payment + extra_payment
    else:
       now_payment = payment
    if (mortgage < now_payment):
        now_payment = mortgage
    mortgage = mortgage - now_payment
    total_paid += now_payment
    print(f"{month:>8}{mortgage:>10.2f}{total_paid:>10.2f}")
print('Total_paid:',total_paid)
print('month:',month)
