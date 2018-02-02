#https://stepik.org/lesson/41562/step/3
big_prime = 1_000_000_007
prime_base = 263

def hash_func(word):
    hash_value = 0
    for letter in reversed(word):
        hash_value = (hash_value * prime_base + ord(letter)) % big_prime
    return hash_value

pattern, string = input(), input() + "+"
p, w = len(pattern), len(string) - len(pattern)

hash_pattern = hash_func(pattern)
hash_window = hash_func(string[w:])
additional = 1
for i in range(p-1):
    additional = (additional * prime_base) % big_prime

res = []
for i in range (w-1,-1,-1):
    #print(f"window = {string[i:i+p]}", end=' ')
    hash_window = (hash_window - ord(string[i+p]) * additional) * prime_base + ord(string[i])
    hash_window %= big_prime
    #print(hash_window)
    if hash_window == hash_pattern and string[i:i+p] == pattern:
        res.append(i)
print(*reversed(res))



