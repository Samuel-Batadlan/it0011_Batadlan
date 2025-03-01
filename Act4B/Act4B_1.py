A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

all_AB = A | B
print("a. Elements in A or B:", all_AB, "| Count:", len(all_AB))

only_B  = B - (A | C)
print("b. Elements in B but not in A or C:", only_B, "| Count:", len(only_B))

print("c.1. [h, i, j, k]:", C - (A | B))
print("c.2. [c, d, f]:", (A & C) - B)
print("c.3. [b, c, h]:", B & C)
print("c.4. [d, f]:", (A & C) - B)
print("c.5. [c]:", A & B & C)
print("c.6. [l, m, o]:", B - (A | C))