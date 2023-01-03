def get_the_mirror_string(n, string):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    mirror =    "zyxwvutsrqponmlkjihgfefcba"

    first_part = string[0 : n - 1]
    remaining_part = string[n - 1: ]

    mirror_string  = ""

    for letter in remaining_part:
        index = alphabets.index(letter)
        mirror_string += mirror[index]
    result = first_part + mirror_string
    return result



if __name__ == "__main__":
    n = 3
    string = 'paradox'
    mirror_string = get_the_mirror_string(n, string)
    print(mirror_string)