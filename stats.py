def count_words_in_text(text):
    number_of_words = len(text.split())
    return number_of_words

def count_characters(text):
    count = {}
    for letter in text:
        current_letter = letter.lower()
        if current_letter in count:
            count[current_letter] += 1
        else:
            count[current_letter] = 1
    return count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list_of_dicts = []
    for char, count in dict.items():        
        list_of_dicts.append({"char": char, "num": count})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return(list_of_dicts)