def descending_order(num):
    string_Num = str(num)
    string_Num = sorted(string_Num, reverse=True)
    string_Num = int("".join(string_Num))
    return string_Num
