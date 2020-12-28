"""
WEEK 1 ASSESSMENT
"""

#Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.
class Bike():
    def __init__(self, color, price):
        self.color = color
        self.price = price

testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)

#Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples." (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)
class AppleBasket():
    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity
   
    def increase(self):
        self.apple_quantity = self.apple_quantity + 1
        return self.apple_quantity
    
    def __str__(self):
        statement = "A basket of {} {} apples."
        return statement.format(self.apple_quantity, self.apple_color)

a1 = AppleBasket("red", 2)
print(a1)
print(a1.increase())


#Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount, you see "Your account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with "Bob" as the name and 100 as the amount. Save this to the variable t1.​

class BankAccount():
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt
    def __str__(self):
        statement = "Your account, {}, has {} dollars."
        return statement.format(self.name, self.amt)
    
t1 = BankAccount("Bob", 100)


"""
WEEK 2 ASSESSMENT
"""
#The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create. 
#Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are different.
#For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a lot of different moves!". Create an instance of this class with the name as "Belle". Assign this instance to the variable p1.

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    def __init__(self, name, level = 5):
        Pokemon.__init__(self, name, level = 5)
        
    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        statement = "{} knows a lot of different moves!"
        return statement.format(self.name)

p1 = Grass_Pokemon("Belle", 5)
print(p1.action())


#Modify the Grass_Pokemon subclass so that the attack strength for Grass_Pokemon instances does not change until they reach level 10. At level 10 and up, their attack strength should increase by the attack_boost amount when they are trained.
#To test, create an instance of the class with the name as "Bulby". Assign the instance to the variable p2. Create another instance of the Grass_Pokemon class with the name set to "Pika" and assign that instance to the variable p3. Then, use Grass_Pokemon methods to train the p3 Grass_Pokemon instance until it reaches at least level 10.
class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def train(self):
        self.update()
        if self.level >= 10:
            self.attack_up()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

p2 = Grass_Pokemon("Bulby", 5)
p3 = Grass_Pokemon("Pika", 5)
p3.train()
print(p3.train())


#Along with the Pokemon parent class, we have also provided several subclasses. Write another method in the parent class that will be inherited by the subclasses. Call it opponent. It should return which type of pokemon the current type is weak and strong against, as a tuple.
#Grass is weak against Fire and strong against Water
#Ghost is weak against Dark and strong against Psychic
#Fire is weak against Water and strong against Grass
#Flying is weak against Electric and strong against Fighting
#For example, if the p_type of the subclass is 'Grass', .opponent() should return the tuple ('Fire', 'Water')

class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3

class Fire_Pokemon(Pokemon):
    p_type = "Fire"

class Flying_Pokemon(Pokemon):
    p_type = "Flying"


"""
WEEK 3 ASSESSMENT
Test Cases
Exceptions
"""
#The function mySum is supposed to return the sum of a list of numbers (and 0 if that list is empty), but it has one or more errors in it. Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.
assert mySum([2]) == 2
assert mySum([]) == 0
assert mySum([1, 4, -2]) == 3
assert mySum([1,2,3]) == 6

#test-4-1: Which of the following cases fail for the mySum function?
#A. an empty list
#C. a list with more than one item


#test-4-2: Are there any other cases, that we can determine based on the current structure of the function, that also fail for the mySum function?
#B. No


"""
The class Student is supposed to accept two arguments in its constructor:
A name string
An optional integer representing the number of years the student has been at Michigan (default:1)
Every student has three instance variables:
self.name (set to the name provided)
self.years_UM (set to the number of years the student has been at Michigan)
self.knowledge (initialized to 0)
There are three methods:
.study() should increase self.knowledge by 1 and return None
.getKnowledge() should return the value of self.knowledge
.year_at_umich() should return the value of self.years_UM
There are one or more errors in the class. Use this space to write test cases to determine what errors 
there are. You will be using this information to answer the next set of multiple choice questions.
"""
me = Student("A", 3)
print(me.name())
print(me.year_at_umich())
assert me.study() == None
print(me.getKnowledge())

#test-4-3: Which of the following cases fail for the Student class?
#C. the attributes/instance variables are not correctly assigned in the constructor
#D. the method study does not increase self.knowledge


#test-4-4: Are there any other cases, that we can determine based on the current structure of the class, that also fail for the Student class?
#A. Yes


#The code below takes the list of country, country, and searches to see if it is in the dictionary gold which shows some countries who won gold during the Olympics. However, this code currently does not work. Correctly add try/except clause in the code so that it will correctly populate the list, country_gold, with either the number of golds won or the string “Did not get gold”.
gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []
for x in country:
    try:
        country_gold.append(gold[x])
    except:
        country_gold.append("Did not get gold")

#Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes.
di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except:
        pass

print("Total number of puppies:", total)


#The list, numb, contains integers. Write code that populates the list remainder with the remainder of 36 divided by each number in numb. For example, the first element should be 0, because 36/6 has no remainder. If there is an error, have the string “Error” appear in the remainder.
numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
remainder = []
for i in numb:
    try:
        r = 36 % i
        remainder.append(r)
    except:
        remainder.append("Error")


#Provided is buggy code, insert a try/except so that the code passes.
lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]
lst_three = []
for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
    except ZeroDivisionError:
        pass

#Write code so that the buggy code provided works using a try/except. When the codes does not work in the try, have it append to the list attempt the string “Error”.
full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']
attempt = []
for elem in full_lst:
    try:
        attempt.append(elem[1])
    except IndexError:
        attempt.append("Error")

#The following code tries to append the third element of each list in conts to the new list third_countries. Currently, the code does not work. Add a try/except clause so the code runs without errors, and the string ‘Continent does not have 3 countries’ is appended to countries instead of producing an error.
conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'], ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'], ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'], ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]
third_countries = []
for c in conts:
    try:
        third_countries.append(c[2])
    except IndexError:
        third_countries.append("Continent does not have 3 countries")


#The buggy code below prints out the value of the sport in the list sport. Use try/except so that the code will run properly. If the sport is not in the dictionary, ppl_play, add it in with the value of 1.
sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]
ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}
for x in sport:
    try:
        print(ppl_play[x])
    except KeyError:
        ppl_play[x] = 1

#Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes. If the key is not there, initialize it in the dictionary and set the value to zero.
di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except KeyError:
        diction["Puppies"] = 0
        

print("Total number of puppies:", total)


"""
COURSE PROJECT
"""
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self, amt):
        self.prizeMoney = self.prizeMoney + amt
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self, prize):
        self.prizes.append(prize)
    def __str__(self):
        statement = "{} (${})"
        return statement.format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here

class WOFHumanPlayer(WOFPlayer):
    def getMove(category, obscuredPhrase, guessed):
        statement = '''
        {} has {} \n
        Category: category \n
        Phrase: obscured_phrase \n
        Guessed: guessed \n
        Guess a letter, phrase, or type "exit" or "pass":
        '''

        print(
            input(statement.format(self.name, self.prizeMoney))
        )

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"
    
    def __init__(self, name, difficulty):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        self.difficulty = difficulty
        
    def smartCoinFlip(self):
        if random.randint(1, 10) > self.difficulty:
            return True
        else:
            return False
        
    def getPossibleLetters(self, guessed):
        list_of_letters = []

        if self.prizeMoney >= 250:
            for l in LETTERS:
                if l not in guessed:
                    list_of_letters.append(l)
        else:
            for l in LETTERS:
                if l not in VOWELS:
                    if l not in guessed:
                        list_of_letters.append(l)

        return list_of_letters
    
    def getMove(self, category, obscuredPhrase, guessed):
        list_of_letters = self.getPossibleLetters(guessed)
        
        coin_flip = self.smartCoinFlip()
        
        if len(list_of_letters) == 0:
            return "pass"
        else:
            if coin_flip == True:
                return list_of_letters[0]   
            elif coin_flip == False:
                return random.choice(list_of_letters)


