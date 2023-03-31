# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

foo = ["Hi! Hello!", "", "Oh, no!!!"]

def remove_exclamation_marks(s):
    foo_1 = [y.replace('!', '') for y in foo]
    foo_2 = str(foo_1).strip('[]')
    return foo_2   
print(remove_exclamation_marks(foo))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
remove = ["Hi! Hello!", "", "Oh, no!!!"]

def remove_last_em(s):
    res = list(map(lambda i: i[: -1], remove))
    result = str(res).strip('[]')
    return result
print(remove_last_em(remove))



# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    pass