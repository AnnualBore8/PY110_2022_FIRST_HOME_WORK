def base64_to_base10(code):
    base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base10 = 0
    for i in code:
        base10 = base10 * 64 + base64.find(i)
    return base10


print(base64_to_base10("A"))
print(base64_to_base10("/"))
print(base64_to_base10("BA"))
print(base64_to_base10("//"))
print(base64_to_base10("WIN"))

assert (base64_to_base10("A")) == 0
assert (base64_to_base10("/")) == 63
assert (base64_to_base10("BA")) == 64
assert (base64_to_base10("//")) == 4095
assert (base64_to_base10("WIN")) == 90637
