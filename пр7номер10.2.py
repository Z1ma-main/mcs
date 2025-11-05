def reverse_words_in_line(s):
    words = s.split()  
    r_words = []
    for i in range(len(words) - 1, -1, -1):
        r_words.append(words[i])  
    return " ".join(r_words)
line = input("Введите строку: ")
print("Результат:", reverse_words_in_line(line))
