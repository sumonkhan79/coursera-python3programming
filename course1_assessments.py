"""
WEEK 1 ASSESSMENT
Programming in Python
Turtle Graphics
"""
#There is a function we are providing in for you in this problem called square. It takes one integer and returns the square of that integer value. Write code to assign a variable called xyz the value 5*5 (five squared). Use the square function, rather than just multiplying with *.
x=5

def square(x):
    return x*x

xyz = square(x)

#Write code to assign the number of characters in the string rv to a variable num_chars.
rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

num_chars = len(rv)

#data-19-1: The code below initializes two variables, z and y. We want to assign the total number of characters in z and in y to the variable a. Which of the following solutions, if any, would be considered hard coding?
#A. a = len("hello worldwelcome!")
#B. a = 11 + 8
#D. a = len("hello world") + len("welcome!")


#turtle-11-1: What are correct ways to tell a turtle named Tex to move forward 20 pixels? Select as many as apply.
#A. Tex.forward(20)
#E. Tex.forward(10 + 10)


#turtle-11-2: Which is the correct way to make a new instance of the Turtle class?
#B. turtle.Turtle()


#turtle-11-3: What does each instance of the Turtle class represent?
#C. A unique 'turtle' that you can use to draw.


#turtle-11-4: True or False, attributes/instance variables are just like other variables in Python.
#A. True


#turtle-11-4: Select all of the following things that methods can do:
#A. Change the value of an attribute.
#B. Return values.
#C. Create new attributes of an instance and set their values.


#turtle-11-5: For an instance of a class that is assigned to the variable student, what is the proper way to refer to the title attribute/instance variable?
#E. student.title



#turtle-11-6: What is the name of jane’s attribute (not method) that is referred to in the following code?
import turtle

jane = turtle.Turtle()
jane.forward(20)
print(jane.x)

#The attribute is: x


#turtle-11-7: What are the names of the instances in the following code? Please put one instance per blank space and enter them in the order that the computer would read them.
import turtle
wn = turtle.Screen()

jazz = turtle.Turtle()
jazz.forward(50)
jazz.right(90)
pop = turtle.Turtle()
pop.left(180)
pop.forward(76)

#wn, jazz, pop


"""
WEEK 2 ASSESSMENT
Lists and Strings
Week 2 Assignment
"""
#sequences-10-1: What will the output be for the following code?
let = "z"
let_two = "p"
c = let_two + let
m = c*5
print(m)

#C. pzpzpzpzpz


#Write a program that extracts the last three items in the list sports and assigns it to the variable last. Make sure to write your code so that it works no matter how many items are in the list.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

last = sports[-3:]

#Write code that combines the following variables so that the sentence “You are doing a great job, keep it up!” is assigned to the variable message. Do not edit the values assigned to by, az, io, or qy.
by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

message = by + " " + az + io + ", " + qy


#sequences-10-2: What will the output be for the following code?
ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)

#C. ['travel', 'lights']

#sequences-10-3: What is the type of m?
l = ['w', '7', 0, 9]
m = l[1:2]
#D. list

#sequences-10-4: What is the type of m?
l = ['w', '7', 0, 9]
m = l[1]
#A. string

#sequences-10-5: What is the type of x?
b = "My, what a lovely day"
x = b.split(',')
#D. list

#sequences-10-6: What is the type of a?
b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)

#A. string



#Write one for loop to print out each character of the string my_str on a separate line.
my_str = "MICHIGAN"

for char in my_str:
    print(char)


#Write one for loop to print out each element of the list several_things. Then, write another for loop to print out the TYPE of each element of the list several_things. To complete this problem you should have written two different for loops, each of which iterates over the list several_things, but each of those 2 for loops should have a different result.
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for element in several_things:
    print(element)

for element in several_things:
    print(type(element))


#Write code that uses iteration to print out the length of each element of the list stored in str_list.
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

for i in str_list:
    print(len(i))


#Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a variable num_chars. Do NOT use the len function to solve the problem (if you use it while you are working on this problem, comment it out afterward!)
original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars = 0
for word in original_str:
     num_chars += 1

#addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).
addition_str = "2+5+10+20"
values_to_add = addition_str.split("+")

sum_val = 0
for i in values_to_add:
    sum_val = sum_val + int(i)
    print(sum_val)


#week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

week_temps = week_temps_f.split(",")

sum_temp = 0
for i in week_temps:
    sum_temp += float(i)
    
avg_temp = sum_temp / len(week_temps)


#Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list.
nums = range(0, 68)

#Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).
original_str = "The quick brown rhino jumped over the extremely lazy fox"

num_words_list = []
for word in original_str.split(" "):
    num_words_list.append(len(word))

print(num_words_list)


#Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").
lett = ""
for i in range(8):
    lett = "b"*i

#Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated, but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)
import turtle
wn = turtle.Screen()
ted = turtle.Turtle()

ted.color("red")
ted.speed(0)

for i in range(4):
    ted.forward(10)
    ted.right(35)
    ted.forward(5)


"""
WEEK 3 ASSESSMENT
"""
#rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.
#Hard-coded answers will receive no credit.
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

rainfall_list = rainfall_mi.split(",")
print(rainfall_list)
num_rainy_months = 0
for item in rainfall_list:
    if float(item) > 3.0:
        num_rainy_months += 1
    else:
        num_rainy_months

print(num_rainy_months)


#The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
same_letter_count = 0
for word in sentence.split(" "):
    if word[0]==word[-1]:
        same_letter_count += 1
    else:
        same_letter_count


#Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
#HINT 1: Use the accumulation pattern!
#HINT 2: the in operator checks whether a substring is present in a string.
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num = 0
count_word_list = []
for i in items:
    count_word = 0
    for letter in i:
        if letter=="w":
            count_word += 1
        else:
            count_word
    count_word_list.append(int(count_word))

for i in count_word_list:
    if i > 0:
        acc_num += 1
    else:
        acc_num

#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.
#Note 1: be sure to not double-count words that contain both an a and an e.
#HINT 1: Use the in operator.
#HINT 2: You can either use or or elif.
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

num_a_or_e = 0
for word in sentence.split(" "):
    if ("a" in word) or ("e" in word):
        num_a_or_e += 1
    else:
        num_a_or_e


#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
num_vowels = 0
for i in s:
    for v in vowels:
        if i == v:
            num_vowels += 1
        else:
            num_vowels


"""
WEEK 4 ASSESSMENT
Sequence Mutation
Lists and Strings
Accumulating Lists and Strings
Way of the Programmer Week 4
"""
#seqmut-1-5: Could aliasing cause potential confusion in this problem?
#A. Yes

#seqmut-1-6: Could aliasing cause potential confusion in this problem?
sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"
# B. No

#seqmut-1-1: Which of these is a correct reference diagram following the execution of the following code?
lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]

#A. I

#seqmut-1-7: Which of these is a correct reference diagram following the execution of the following code?
x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']
#D. IV


#seqmut-1-8: Which of these is a correct reference diagram following the execution of the following code?
sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)

#A. I


#seqmut-1-2: Which method would you use to figure out the position of an item in a list?
#D. index()

#seqmut-1-3: Which method is best to use when adding an item to the end of a list?
#C. append()

#Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

sports.insert(2, "horseback riding")

#Write code to take ‘London’ out of the list trav_dest.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']

trav_dest.remove("London")


#Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']

trav_dest.append("Guadalajara")


#Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z.
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']

winners.sort()
print(winners)

#Write code to switch the order of the winners list so that it is now Z to A. Assign this list to the variable z_winners.
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']

z_winners = winners
z_winners.reverse()


#seqmut-1-9: Which of these is the accumulator variable?
byzo = 'hello world!'
c = 0
for x in byzo:
    z = x + "!"
    print(z)
    c = c + 1
#D. c


#seqmut-1-10: Which of these is the sequence?
cawdra = ['candy', 'daisy', 'pear', 'peach', 'gem', 'crown']
t = 0
for elem in cawdra:
    t = t + len(elem)
#A. cawdra


#seqmut-1-11: Which of these is the iterator (loop) variable?
lst = [5, 10, 3, 8, 94, 2, 4, 9]
num = 0
for item in lst:
    num += item

#A. item


#seqmut-1-12: What is the iterator (loop) variable in the following?
rest = ["sleep", 'dormir', 'dormire', "slaap", 'sen', 'yuxu', 'yanam']
let = ''
for phrase in rest:
    let += phrase[0]

#The iterator variable is: phrase


#Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. Each character in str1 should be its own element in the list chars.
str1 = "I love python"
chars = []
for letter in str1:
    chars.append(letter)



#seqmut-1-1: Which of these is a correct reference diagram following the execution of the following code?
lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]
#A. I


#seqmut-1-4: What will be the value of a after the following code has executed?
a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")

#The value of a will be: ["holiday", "celebrate!", "company"]


#seqmut-1-5: Could aliasing cause potential confusion in this problem?
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)
#A. yes


#seqmut-1-13: Given that we want to accumulate the total sum of a list of numbers, which of the following accumulator patterns would be appropriate?
nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = s + n
#C. III


#seqmut-1-14: Given that we want to accumulate the total number of strings in the list, which of the following accumulator patterns would be appropriate?
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for item in lst:
    if type(item) == type("string"):
        s = s + 1
#D. 4

#seqmut-1-15: Which of these are good names for an accumulator variable? Select as many as apply.
#C. total
#D. accum

#seqmut-1-16: Which of these are good names for an iterator (loop) variable? Select as many as apply.
#A. item
#C. elem
#D. char

#seqmut-1-17: Which of these are good names for a sequence variable? Select as many as apply.
#A. num_lst
#C. sentence
#D. names

#seqmut-1-18: Given the following scenario, what are good names for the accumulator variable, iterator variable, and sequence variable? You are writing code that uses a list of sentences and accumulates the total number of sentences that have the word ‘happy’ in them.
#D. accumulator variable: total | iterator variable: sentence |sequence variable: sentence_lst


#For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"

app = []
for char in ael:
    app.append(char)


#For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]

past_wrds = []
for word in wrds:
    past_wrds.append(word + "ed")

"""
COURSE PROJECT
"""
#Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

a_scores = 0
for score in scores.split(" "):
    if int(score) >= 90:
        a_scores += 1
    else:
        a_scores

#Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

acro = ""
for word in org.split(" "):
    if word not in stopwords:
        acro = acro + word[0].upper()
    else:
        acro

#Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

number = len(sent.split(" "))

acro = ""
for i, word in enumerate(sent.split(" ")):
    if (word not in stopwords) and (i <= number - 2):
        acro = acro + word[0:2].upper() +  ". "
    if (word not in stopwords) and (i == number - 1):
        acro = acro + word[0:2].upper()
    else:
        acro

#A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
p_phrase = "was it a car or a cat I saw"

r_phrase = ""
for letter in p_phrase:
    r_phrase = letter + r_phrase   

#Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]


statement = "The store has {} {}, each for {} USD."

for elem in inventory:
    print(statement.format(elem.split(", ")[1], 
                           elem.split(", ")[0], 
                           elem.split(" ")[2]))