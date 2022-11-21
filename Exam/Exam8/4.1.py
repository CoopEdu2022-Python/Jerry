def check_if_pangram(sentence: str) -> bool:
    all_n = str("abcdefghijklmnopqrstuvwxyz")
    list_all_number = []
    for _ in range(26):
        list_all_number.append(all_n[_])
    print(list_all_number)
    i = 0

    sentence = set(sentence)
    sentence = list(sentence)
    while 1:
        if list_all_number == []:
            return True


        for x in range(len(list_all_number)):
            if sentence[i] == list_all_number[x]:
                print(sentence)
                list_all_number.pop(x)
                i += 1
                break
            else:
                print("3")
                continue
        else:
            print("1")
            return False






print(check_if_pangram("CoopEdu"))