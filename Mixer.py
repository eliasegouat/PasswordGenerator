
# List creation from an existing wordlist file
def toList():
    file_name = input("Choose a file name to open from the project repository : ")
    f = open(file_name+'.txt', mode='r', encoding='utf-8')
    wordlist = f.read().split('\n')
    return(wordlist)
            
# Wordlist Writting to a file
def toFile(wordlist):
    response = input("Save the new wordlist in a text file ? (yes|no) : ")
    if response == 'yes' or response == 'y' or response == 'YES' or response == 'Y':
        file_name = input("Enter a new filename : ")
        with open(file_name+'.txt', mode='w', encoding='utf-8') as f:
            for word in wordlist:
                f.write(word)
                f.write('\n')
                
# Specify several inter-word patterns
def interWordRule(wordlist):
    result = list()
    for word in wordlist :
        word = word.replace(" ", "")
        result.append(word)
    return(result)

# Special characters addition instead of vowels
def specialCharsRule(wordlist):
    result = list()
    for word in wordlist :
        word = word.replace("a", "@")
        word = word.replace("e", "€")
        word = word.replace("i", "1")
        result.append(word)
    return(result)

# Replacement of uppercase by lowercase char
def lowercaseRule(wordlist):
    result = list()
    for word in wordlist :
        word = word.lower()
        result.append(word)
    return(result)

# Generation of a new list per selected rule
def modeMultiList(wordlist, rulelist):
    result = list()
    for rule in rulelist :
        if rule == '1':
            result.extend(interWordRule(wordlist))
        elif rule == '2':
            result.extend(specialCharsRule(wordlist))
        elif rule == '3':
            result.extend(lowercaseRule(wordlist))
        else :
            print("Select valid rule(s) number(s)")
            selectRuleMode(wordlist)
    return result

# Generation of a list of combination lists of n length
def nLengthCombination(lst, n):
    result = []
    rem_list = []
    m = ''
    if n == 0:
        return [[]]
    for i in range(0, len(lst)):
        m = lst[i]
        rem_list = lst[i + 1:]  
        for j in nLengthCombination(rem_list, n-1):
            result.append([m]+j) 
    return result

# Generation of a new list for each possible combination of selected rules 
def modeEveryList(wordlist, rulelist):
    combination_list = list()
    for i in range(1, (len(rulelist)+1)):
        for combination in nLengthCombination(rulelist, i):
            combination_list.append(combination)
    
    result = list()
    for combination in combination_list :
        current_list = wordlist.copy()
        for rule in combination :
            print(rule)
            if rule == '1':
                current_list = interWordRule(current_list)
            elif rule == '2':
                current_list = specialCharsRule(current_list)
            elif rule == '3':
                current_list = lowercaseRule(current_list)
            else :
                print("Select valid rule(s) number(s)")
                selectRuleMode(wordlist)
        result.extend(current_list)
    return result

# Generation of a unique list combining every selected rules
def modeUniqueList(wordlist, rulelist):
    for rule in rulelist :
        if rule == '1':
            wordlist = interWordRule(wordlist)
        elif rule == '2':
            wordlist = specialCharsRule(wordlist)
        elif rule == '3':
            wordlist = lowercaseRule(wordlist)
        else :
            print("Select valid rule(s) number(s)")
            selectRuleMode(wordlist)
    return wordlist

# Rule Mode Selection
def selectRuleMode(wordlist):
    rule_id = input("""Select one or several rules to apply :
    1. Inter-Word Rule
    2. Special Characters Rule
    3. Lowercase Rule
    Enter the rules numbers separated by space : """)
    
    rule_id_list = rule_id.split()
    result = list()

    if len(rule_id_list) > 1 :
        rule_mode = input("""Select a mode :
        1. Unique list (one list for every selected rules)
        2. Multiple lists (one list per selected rules)
        3. Every lists (every possible rules combinations)
        Enter the mode number : """)

        if rule_mode == '1':
            result = modeUniqueList(wordlist, rule_id_list)
        elif rule_mode == '2':
            result = modeMultiList(wordlist, rule_id_list)
        elif rule_mode == '3':
            result = modeEveryList(wordlist, rule_id_list)
        else :
            print("Select valid mode number")
            selectRuleMode()
    return result       
                        
old_wordlist = toList()
new_wordlist = selectRuleMode(old_wordlist)
print(new_wordlist)
toFile(new_wordlist)