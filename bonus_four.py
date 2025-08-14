bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]
total = 0
my_share = 0
for money in bill:
  total += money
print("Total: $", total)
my_share = total/4
print("My share: $", my_share)