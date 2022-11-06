# 定义一个函数 reverse_vowels(s)，参数为字符串，将其中的元音字母的顺序反转（a、e、i、o、u），返回新的字符串
def reverse_vowels(s: str) -> str:
    AEIOU_list = ["A","E","I","O","U","a","e","i","o","u"]
    safe_list = []
    new_list = []
    carry = 0
    for _ in range(0,len(s)):
        if s[_] in AEIOU_list:
            safe_list.append(s[_])
        else:
            continue

    safe_list = safe_list[::-1]
    for _ in range(0,len(s)):

        if s[_] in AEIOU_list:
            new_list.append(safe_list[carry])
            carry += 1
        else:
            new_list.append(s[_])
    return "".join(new_list)
print(reverse_vowels("CoopEdu2022"))