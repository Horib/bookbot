
def char_count(text):
    lowered_text = text.lower()
    lowered_text = "".join(char for char in lowered_text if char.isalpha())  

    char_dict = {}
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def word_count(text):
    return len(text.split())


def sort_on(char_dict):
    # Convert dictionary to a sorted list of dictionaries based on 'value' (frequency)
    return sorted(
        [{'key': k, 'value': v} for k, v in char_dict.items()],
        key=lambda x: x['value'],
        reverse=True
    )


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        
        dicts = char_count(file_contents)
        list_of_dicts = sort_on(dicts)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count(file_contents)} words found in the document")
        print("")
        for char_dict in list_of_dicts:
            print(f"The '{char_dict['key']}' character was found {char_dict['value']} times")
        print("--- End report ---")


main()
