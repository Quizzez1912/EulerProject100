# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Findthe sum of all the multiples of 3 or 5 below 1000.
a = 1
b = 2
c = 0
sum = 2
while c < 4000000:
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        print(c, "c is ")
        sum += c

print(sum)
