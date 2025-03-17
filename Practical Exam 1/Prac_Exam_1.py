def count_words(text):
    excluded_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}
    words = text.split()

    word_count = {}

    for word in words:
        filtered_word = word.strip(".,!?")  
        lower_word = filtered_word.lower()  

        if lower_word not in excluded_words:
            if filtered_word in word_count:
                word_count[filtered_word] += 1
            else:
                word_count[filtered_word] = 1

    lowercase_words = sorted([w for w in word_count if w.islower()])
    uppercase_words = sorted([w for w in word_count if w[0].isupper()])

    for word in lowercase_words:
        print(f"{word} - {word_count[word]}")
    for word in uppercase_words:
        print(f"{word} - {word_count[word]}")

    print(f"\nTotal words filtered: {sum(word_count.values())}")


text_input = input("Enter a string statement: ")
count_words(text_input)
