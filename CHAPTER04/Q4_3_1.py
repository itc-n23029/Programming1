def concat_words(*args, separator="."):
    return separator.join(args)


print(concat_words("a", "b", "c", "d", separator="_"))
