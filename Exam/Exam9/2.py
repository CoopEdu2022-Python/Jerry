# You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:
# - If the length of the word is 1 or 2 letters, change all letters to lowercase.
# - Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.
def capitalize_title(title: str) -> str:
    title = title.lower()
    title = list(title.split(" "))

    if len(title) > 2:
        title[0] = title[0][0].upper() + title[0][1:]
        return (" ".join(title))
    else:
        return (" ".join(title))

print(capitalize_title("capiTalIze tHe lEtTeR OF titLe"))
