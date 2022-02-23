
# List creation from an existing wordlist file
def toList():
    file_name = input("Choose a file name to open from the project repository : ")
    f = open(file_name+'.txt', mode='r', encoding='utf-8')
    wordlist = f.read().split('\n')
    return(wordlist)
            
# Wordlist Writting to a file
def toFile(wordlist):
    response = input("Save the new wordlist in a text file ? (yes|no) : ")
    if response == 'yes' or response == 'y':
        file_name = input("Enter a new filename : ")
        with open(file_name+'.txt', mode='w', encoding='utf-8') as f:
            for word in wordlist:
                f.write(word)
                f.write('\n')
                
# Specify several inter-word patterns
def interWordRule(wordlist):
    spaceless_list = list()
    for word in wordlist :
        word = word.replace(" ", "")
        spaceless_list.append(word)
    return(spaceless_list)

# Special characters addition instead of vowels
def specialCharsRule(wordlist):
    special_list = list()
    for word in wordlist :
        word = word.replace("a", "@")
        word = word.replace("e", "€")
        word = word.replace("i", "1")
        special_list.append(word)
    return(special_list)

# Rule Selection
def selectRule(wordlist):
    result = list()
    rule_id = input("""Select one or several rules to apply :
    1. Inter-Word Rule
    2. Special Characters Rule
    Enter the rules numbers separated by space : """)
    
    for rule in rule_id.split() :
        if rule == '1':
            result.extend(interWordRule(wordlist))
        elif rule == '2':
            result.extend(specialCharsRule(wordlist))
        else :
            print("Select valid rules numbers")
            selectRule()
    return result
                  
                        
old_wordlist = toList()
new_wordlist = selectRule(old_wordlist)
print(new_wordlist)