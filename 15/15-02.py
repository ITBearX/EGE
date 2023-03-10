'''
Для какого наибольшего целого числа A формула
(x + 2y ≠ 60) ∨ (A < y) ∨ (y < x)
тождественно истинна при любых целых неотрицательных x и y?
'''

for a in range(1000):
    ok = True
    for x in range(60):
        for y in range(60):
            if not (x + 2*y != 60 or a < y or y < x):
                ok = False
    if ok:
        print(a)
