gcd = lambda x, y: x if y == 0 else gcd (y, x%y)
a, b = map(int, raw_input().split('/'))
c = gcd(a, b)
print '%d/%d' % (a/c, b/c)
