def check_string_starts_with_vowel(string):
    vowels = "a,e,i,o,u"
    starting = string[0]

    if starting.lower() in vowels:
        return "Valid"
    else:
        return "Not Valid"

if __name__ == "__main__":

    string = "animal"

    result = check_string_starts_with_vowel(string)
    print(result)