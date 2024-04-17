z = ['1', '2', '3', '彩色是', 'a']

for p in z:
    if p.isalnum() or not p:
        z.remove(p)

print(z)
