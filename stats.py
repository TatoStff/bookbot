def word_count(book):
    return len(book.split())

def letter_count(book):
    count = {}
    book = book.lower()
    for chara in book:
        if chara in count:
            count[chara] += 1
        else:
            count[chara] = 1

    
    return count

def sorted_dicts(input_dict):
    characters = []
    for chara in input_dict:
        new_dict = {}
        new_dict = {"char": chara, "num": input_dict[chara]}
        characters.append(new_dict)
    characters.sort(key=lambda char: char["num"], reverse=True)

    return characters


