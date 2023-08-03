
"""
Module 3 - PyDICTIONARY

PyDictionary is a dictionary (as in the English language dictionary) module for Python2 and Python3.
PyDictionary provides the following services for a word:
1. Meanings
2. Translations
3. Synonyms
4. Antonyms

"""

from PyDictionary import PyDictionary
dict = PyDictionary()

print("\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
print("\t\t\t\t\t\t\t\tWelcome to this program!\n\nWe provide you the following services for a word:"
      "\n\t1. Meanings\n\t2. Antonyms \n\t3. Synonyms\n\t4. Translations")

while True:
    print("----- ----- ----- ----- -----")
    choice_input = int(input("\t\nEnter the serial number of the service that you want to avail: "))

    if choice_input == 1: 
        print("\nMEANING SECTION")
        input_meaning = input("Enter the word whose meaning is to be shown: ")
        print(f"\nHere's the meaning of {input_meaning.capitalize()}:")
        print(dict.meaning(input_meaning))

        print("\n\tTo check it's synonyms     - Press 1\n\tTo check it's antonyms     - Press 2\n\t"
              "To return to the main menu - Press 9\n\tTo exit the program\t\t   - Press 0")
        input_sub = int(input("\tEnter your choice: "))

        if input_sub == 1:
            print(f"\nHere are the synonyms of {input_meaning.capitalize()}:")
            print(dict.synonym(input_meaning))
            print("\n\t\t\t\t\t\t   Thank you for using this program!\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break
        if input_sub == 2:
            print(f"\nHere are the antonyms of {input_meaning.capitalize()}:")
            print(dict.antonym(input_meaning))
            print("\n\t\t\t\t\t\t   Thank you for using this program!\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break
        if input_sub == 9:
            continue
        if input_sub== 0:
            print("\n\t\t\t\t\t\t   Thank you for using this program!\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break
        else:
            print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break

    if choice_input == 2:
        print("\nANTONYM SECTION")
        input_ant = input("Enter the word whose antonym is to be shown: ")
        print(f"\nHere are the antonyms of {input_ant.capitalize()}:")
        print(dict.antonym(input_ant))

        print("\n\tTo check it's synonyms     - Press 1\n\tTo return to the main menu - Press 9\n\t"
              "To exit the program\t\t   - Press 0")
        input_sub = int(input("\tEnter your choice: "))

        if input_sub == 1:
            print(f"\nHere are the synonyms of {input_ant.capitalize()}:")
            print(dict.synonym(input_ant))
            print("\n\t\t\t\t\t\t   Thank you for using this program!\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break
        if input_sub == 9:
            continue
        if input_sub== 0:
            print("\n\t\t\t\t\t\t   Thank you for using this program!\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break
        else:
            print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break

    if choice_input == 3:
        print("\nSYNONYM SECTION")
        input_syn = input("Enter the word whose synonym is to be shown: ")
        print(f"\nHere are the synonyms of {input_syn.capitalize()}:")
        print(dict.synonym(input_syn))

        print("\n\tTo check it's antonyms     - Press 1\n\tTo return to the main menu - Press 9\n\t"
              "To exit the program\t\t   - Press 0")
        input_sub = int(input("\tEnter your choice: "))

        if input_sub == 1:
            print(f"\nHere are the antonyms of {input_syn.capitalize()}:")
            print(dict.antonym(input_syn))
            print("\n\t\t\t\t\t\t   Thank you for using this program!\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break
        if input_sub == 9:
            continue
        if input_sub== 0:
            print("\n\t\t\t\t\t\t   Thank you for using this program!\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break
        else:
            print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break

    if choice_input == 4:
        from PyDictionary import PyDictionary
        dict = PyDictionary()
        print("\nTRANSLATING SECTION")
        print("Welcome! Here you can translate your word to the following languages:\n\t1.  English\n\t2.  Hindi\n\t3.  French"
              "\n\t4.  German\n\t5.  Spanish\n\t6.  Russian\n\t7.  Japanese\n\t8.  Arabic\n\t9.  Greek\n\t10. Urdu")

        input_trans = input("Enter the word you want to translate: ")
        input_langt = int(input("Enter the language number (from the list above) to which you want the word to be translated: "))
#harshil sharma is the best
        if input_langt == 1:
            print(dict.translate(input_trans,'en'))

        if input_langt == 2:
            print(dict.translate(input_trans,'hi'))

        if input_langt == 3:
            print(dict.translate(input_trans,'fr'))

        if input_langt == 4:
            print(dict.translate(input_trans,'de'))

        if input_langt == 5:
            print(dict.translate(input_trans,'es'))

        if input_langt == 6:
            print(dict.translate(input_trans,'ru'))

        if input_langt == 7:
            print(dict.translate(input_trans,'ja'))

        if input_langt == 8:
            print(dict.translate(input_trans,'ar'))

        if input_langt == 9:
            print(dict.translate(input_trans,'el'))

        if input_langt == 10:
            print(dict.translate(input_trans,'ur'))

        else:
            print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t****** DICTIONARY AND TRANSLATOR ******")
            break
