def to_upper_case(quote) -> str:
    quote = quote.split(' ')
    new_quote = []
    for i in quote:
        new_quote.append(i.capitalize())
    return ' '.join(map(str, new_quote))


# print(to_upper_case("How can mirrors be real if our eyes aren't real"))
assert to_upper_case("How can mirrors be real if our eyes aren't real") == "How Can Mirrors Be Real If Our Eyes Aren't Real"

# Поиск решения

# quote = "How can mirrors be real if our eyes aren't real"
# new = quote.split(' ')
# new_quote = []
#
# for i in new:
#     new_quote.append(i.capitalize())
#
# print(' '.join(map(str, new_quote)))
