


# return the amount of words by creating a word count function
def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    
    character_dictionary = {}
    for character in file_contents:
        character = character.lower()
        if character not in character_dictionary:
            character_dictionary[character] = 1
        else:
            character_dictionary[character] += 1
    return character_dictionary

def sort_on(character_dictionary):
    return character_dictionary["num"]



def main():
    #turn text file into a variable
    with open("books/frankenstein.txt") as f:
        #turn the contents of the text file into a variable
        file_contents = f.read()
        # call the word count function of the contents
        word_count_result = word_count(file_contents)
        character_count_result = character_count(file_contents)

        char_list = []
        for char, count, in character_count_result.items():
            if char.isalpha():
                new_dict = {
                    "char": char,
                    "num": count
                }
                char_list.append(new_dict)

        char_list.sort(reverse=True, key=sort_on)
        
        
    #print results of word count function
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count_result} words found in the document\n")
    #print character count
    for character_dictionary in char_list:
        print(f"The '{character_dictionary['char']}' was found {character_dictionary['num']} time")
    


main()