value = 122

quarters = int(value / 25)
value -= quarters * 25

dimes = int(value / 10)
value -= dimes * 10

pennies = value

print('quarters:{} dimes:{} pennies:{}'.format(quarters, dimes, pennies))