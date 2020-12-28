"""
WEEK 1 ASSESSMENT
Files and CSV
"""
#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

with open("travel_plans.txt", "r") as df:

    num = 0
    for line in df.readlines():
        num = num + len(line)


#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
with open("emotion_words.txt", "r") as df:
    num_words = 0
    for line in df.readlines():
        row_words = line.split(" ")
        num_words += len(row_words)


#Assign to the variable num_lines the number of lines in the file school_prompt.txt.
with open("school_prompt.txt", "r") as df:
    num_lines = 0
    for line in df.readlines():
        num_lines += 1


#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
with open("school_prompt.txt", "r") as df:
    beginning_chars = df.read(30)


#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
with open("school_prompt.txt", "r") as df:
    three = []
    start_index = 2
    for line in df.readlines():
        prompt = line.split(" ")
        #print(prompt)
        three.append(prompt[2])

#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
emotions = []
with open("emotion_words.txt", "r") as df:
    for line in df.readlines():
        emotions.append(line.split(" ")[0])


#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
with open("travel_plans.txt", "r") as df:
    first_chars = df.read(33)


#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
with open("school_prompt.txt", "r") as df:
    p_words = []
    for line in df.readlines():
        line = line.replace("\n", "")
        list_of_words = line.split(" ")
        for word in list_of_words:
            if "p" in word:
                p_words.append(word.replace("\n", ""))
            else:
                pass

"""
WEEK 2 ASSESSMENT
Dictionary Mechanics
Dictionary Accumulation
"""

#At the halfway point during the Rio Olympics, the United States had 70 medals, Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and Germany had 17 medals. Create a dictionary assigned to the variable medal_count with the country names as the keys and the number of medals the country had as each key’s value.
medal_count = {
    "United States": 70,
    "Great Britain": 38,
    "China": 45,
    "Russia": 30,
    "Germany": 17
}


#Given the dictionary swimmers, add an additional key-value pair to the dictionary with "Phelps" as the key and the integer 23 as the value. Do not rewrite the entire dictionary.
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}

swimmers["Phelps"] = 23


#Add the string “hockey” as a key to the dictionary sports_periods and assign it the value of 3. Do not rewrite the entire dictionary.
sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}

sports_periods["hockey"] = 3


#The dictionary golds contains information about how many gold medals each country won in the 2016 Olympics. But today, Spain won 2 more gold medals. Update golds to reflect this information.
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

golds["Spain"] = 21


#Create a list of the countries that are in the dictionary golds, and assign that list to the variable name countries. Do not hard code this.
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

countries = []
for key in golds:
    countries.append(key)


#Provided is the dictionary, medal_count, which lists countries and their respective medal count at the halfway point in the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value for "Belarus" to the variable belarus. Do not hardcode this.
medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}

belarus = medal_count["Belarus"]


#The dictionary total_golds contains the total number of gold medals that countries have won over the course of history. Use dictionary mechanics to find the number of golds Chile has won, and assign that number to the variable name chile_golds. Do not hard code this!
total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}

chile_golds = total_golds["Chile"]


#Provided is a dictionary called US_medals which has the first 70 metals that the United States has won in 2016, and in which category they have won it in. Using dictionary mechanics, assign the value of the key "Fencing" to a variable fencing_value. Remember, do not hard code this.
US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}

fencing_value = US_medals["Fencing"]


#The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}

credits = 0
for key in Junior.keys():
    credits = credits + Junior[key]

#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
str1 = "peter piper picked a peck of pickled peppers"

freq = {}

for c in str1:
    if c not in freq:
        freq[c] = 0
    freq[c] = freq[c] + 1

#Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
s1 = "hello"

counts = {}
for c in s1:
    if c not in counts:
        counts[c] = 0
    counts[c] = counts[c] + 1


#Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

freq_words = {}
for word in str1.split(" "):
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] = freq_words[word] + 1


#Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

wrd_d = {}
for word in sent.split(" "):
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] = wrd_d[word] + 1

#Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.
sally = "sally sells sea shells by the sea shore"

characters = {}

for letter in sally:
    if letter not in characters:
        characters[letter] = 0
    characters[letter]=characters[letter]+1

maximum = max(characters.values())
for key, value in characters.items():
    if value==maximum:
        best_char = key
    else:
        pass

#Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.
sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for letter in sally:
    if letter not in characters:
        characters[letter] = 0
    characters[letter]=characters[letter]+1

keys = list(characters.keys())
worst_char = keys[0]

for key in characters:
    if characters[key] < characters[worst_char]:
        worst_char = key

#Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."

letter_counts = {}

for c in string1:
    lower_case = c.lower()
    if lower_case not in letter_counts:
        letter_counts[lower_case] = 0
    letter_counts[lower_case] = letter_counts[lower_case] + 1 


#Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

low_d = {}
for c in p.lower():
    if c not in low_d:
        low_d[c] = 0
    low_d[c] = low_d[c] + 1
    


"""
WEEK 3 ASSESSMENT
Functions
Tuples
"""
#Write a function called int_return that takes an integer as input and returns the same integer.
def int_return(i):
    return i

#Write a function called add that takes any number as its input and returns that sum with 2 added.
def add(x):
    return x+2

#Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.
def change(string):
    new_string = string + "Nice to meet you!"
    return new_string

#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(list_of_int):
    total = 0
    for i in list_of_int:
        total = total + i
    return total

#Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(some_list):
    if len(some_list) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"

#You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.
def divide(x):
    return x/2

def sum(x):
    divided_num = divide(x)
    new_num = divided_num + 6
    return new_num


#Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.
olympics = ("Beijing", "London", "Rio", "Tokyo")


#The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this list to the variable country.
tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]

country = []
for item in tuples_lst:
    country.append(item[1])

#With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.
olymp = ('Rio', 'Brazil', 2016)

city, country, year = olymp

#Define a function called info with five parameters: name, gender, age, bday_month, and hometown. The function should then return a tuple with all five parameters in that order.
def info(name, gender, age, bday_month, hometown):
    return (name, gender, age, bday_month, hometown)


#Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in the 2016 Olympics. Create a list, num_medals, that contains only the number of medals for each country. You must use the .items() method. Note: The .items() method provides a list of tuples. Do not use .keys() method.
gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}

num_medals = []
for key, value in gold.items():
    num_medals.append(value)



"""
WEEK 4 ASSESSMENT
More about Iteration
Advanced Functions
"""
#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
def sublist(list_of_num):
    sublist = []
    item = 0
    while item < len(list_of_num):
        print(item)
        if list_of_num[item] != 5:
            sublist.append(list_of_num[item])
            item = item + 1
        elif list_of_num[item] == 5:
            break

    return sublist

#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
def check_nums(list_of_num):
    item = 0
    new_list = []
    while item < len(list_of_num):
        if list_of_num[item] != 7:
            new_list.append(list_of_num[item])
            item = item + 1
        elif list_of_num[item] == 7:
            break
    return new_list

#Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist(list_of_strings):
    new_list = []
    item = 0
    while item < len(list_of_strings):
        if list_of_strings[item] != "STOP":
            new_list.append(list_of_strings[item])
            item = item + 1
        elif list_of_strings[item] == "STOP":
            break
    return new_list
        

#Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.
def stop_at_z(list_of_strings):
    new_list = []
    item = 0
    while item < len(list_of_strings):
        if list_of_strings[item] != "z":
            new_list.append(list_of_strings[item])
            item = item + 1
        elif list_of_strings[item] == "z":
            break
    return new_list

#Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x


sum2 = 0
item = 0
while item < len(lst):
    sum2 = sum2 + lst[item]
    item = item + 1
    

#Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
def beginning(list_of_strings):
    item = 0
    new_list = []
    while item <= 9:
        if list_of_strings[item] != "bye":
            new_list.append(list_of_strings[item])
            item = item + 1
        elif list_of_strings[item] == "bye":
            break
    while item >= 10:
        break
    return new_list


#Create a function called mult that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.
def mult(integer, num = 6):
    return integer * num

#The following function, greeting, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

#Below is a function, sum, that does not work. Change the function definition so the code works. The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.
def sum(intx, intz=5):
    return intz + intx

#Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.
def test(some_integer, some_bool = True, dict1 = {2:3, 4:5, 6:8}):
    if some_bool==True:
        if some_integer in dict1:
            return dict1[some_integer]
        else:
            return False
    else:
        return False

#Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.
#But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.
def checkingIfIn(string, direction = True, d = 
                 {"apple": 2, 
                  "pear": 1, 
                  "fruit": 19,
                  "orange": 5,
                  "banana": 3, 
                  "grapes": 2, 
                  "watermelon": 7,
                 }):
    if direction == True:
        if string in d:
            return True
        else:
            return False
    elif direction == False:
        if string not in d:
            return True
        else:
            return False


#We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions in the active code window for specific variable assignmemts.
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn("cherry", direction = True)

# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn("cherry", direction = False)

# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn("fruit", direction = True)

# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn("cherry", d = {"cherry": 8})


"""
WEEK 5 ASSESSMENT
Sorting
"""
#Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse = True)

#Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']

animals_sorted = sorted(animals)

#The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)


#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three = sorted(medals, reverse = True, key = lambda country: medals[country])[0:3]
print(top_three)


#We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries, reverse = True, key = lambda x: groceries[x])
print(most_needed)


#Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
def last_four(x):
    string_id = str(x)
    return string_id[-4:]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key = lambda x: last_four(x))


#Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
print(ids)
sorted_id = sorted(ids, key = lambda x: str(x)[-4:])
print(sorted_id)


#Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, reverse = False, key = lambda elem: elem[1])
print(lambda_sort)


"""
COURSE PROJECT
Part 1: Sentiment Classifier
Part 2: Sentiment Analysis (submit chart)
"""

"""
We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)
"""
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(my_string):
    for punc in punctuation_chars:
        my_string = my_string.replace(punc, "")

    return my_string


"""
Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
"""
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# Count number of positive words
def get_pos(my_string):
    positive_word_count = 0
    my_string = strip_punctuation(my_string).lower()
    for word in my_string.split(" "):    
        if word in positive_words:
            positive_word_count = positive_word_count + 1        
        else: 
            positive_word_count
    return positive_word_count


"""
Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
"""
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(my_string):
    negative_word_count = 0
    my_string = strip_punctuation(my_string).lower()
    for word in my_string.split(" "):    
        if word in negative_words:
            negative_word_count = negative_word_count + 1        
        else: 
            negative_word_count
    return negative_word_count


"""
Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.
"""
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(my_string):
    for punc in punctuation_chars:
        my_string = my_string.replace(punc, "")
    return my_string


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
            
# Count number of positive words
def get_pos(my_string):
    positive_word_count = 0
    my_string = strip_punctuation(my_string).lower()
    for word in my_string.split(" "):    
        if word in positive_words:
            positive_word_count = positive_word_count + 1        
        else: 
            positive_word_count
    return positive_word_count            

# Count the number of negative words
def get_neg(my_string):
    negative_word_count = 0
    my_string = strip_punctuation(my_string).lower()
    for word in my_string.split(" "):    
        if word in negative_words:
            negative_word_count = negative_word_count + 1        
        else: 
            negative_word_count
    return negative_word_count

with open("project_twitter_data.csv", "r") as df:
    '''
    Now, you will write code to create a csv file called resulting_data.csv, 
    which contains the Number of Retweets, Number of Replies, 
    Positive Score (which is how many happy words are in the tweet), 
    Negative Score (which is how many angry words are in the tweet), and the 
    Net Score (how positive or negative the text is overall) for each tweet.
    The file should have those headers in that order.
    '''

    outfile = open("resulting_data.csv", "w")
    # output the header row
    outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    outfile.write('\n')
    
    # Read in all the lines
    lines = df.readlines()
    
    # See what original headers were
    orig_headers = lines[0]
    
    # Now loop through each line and grab what we need
    for line in lines[1:]:
        tweet = line.split(",")[0].lower()
        tweet = strip_punctuation(tweet)
        
        retweets = int(line.split(",")[1])
        replies = int(line.split(",")[2])
        
        positive_score = get_pos(tweet)
        negative_score = get_neg(tweet)
        net_score = positive_score - negative_score
        
        # New row to output
        row_string = '{}, {}, {}, {}, {}\n'.format(str(retweets), str(replies), str(positive_score), str(negative_score), str(net_score))
        outfile.write(row_string)
    outfile.close()
        