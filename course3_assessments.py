"""
WEEK 1 ASSESSMENT
"""

#The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

output = nested[1][2]


lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = "yellow" in lst[2]

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four = 3 in lst[1]

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = "orange" in lst[0]


L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = "hola" in L

# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = [5, 8, 7] in L

# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = 6.6 in L[2]



nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

#Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
if "data" in nested:
    data = True
else:
    data = False
    
#Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
if 24 in nested:
    twentyfour = True
else:
    twentyfour = False
    
#Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
if "whole" in nested:
    whole = True
else:
    whole = False
    
#Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
if "physics" in nested:
    physics = True
else:
    physics = False


#The variable nested_d contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics. Assign the value of Great Britain’s gold medal count from the London Olympics to the variable london_gold. Use indexing. Do not hardcode.
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

london_gold = nested_d["London"]["Great Britain"]



sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports["swimming"][2]

# Assign the string 'platform' to the name v2
v2 = sports["diving"][1]

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports["gymnastics"]["women"]

# Assign the string 'rings' to the name v4
v4 = sports["gymnastics"]["men"][3]


#Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary to the list US_count.
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []

US_count.append(nested_d["Beijing"]["USA"])
US_count.append(nested_d["London"]["USA"])
US_count.append(nested_d["Rio"]["USA"])



#Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = []
for item in l_of_l:
    third.append(item[2])


#Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it contains the letter “t”. If it does not contain the letter “t”, save the athlete name into list other.
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = []
other = []

for item in athletes:
    for person in item:
        if "t" in person:
            t.append(person)
        else:
            other.append(person)


"""
WEEK 2 ASSESSMENT
"""
# Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element using mapping.
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = map(lambda x: "Fruit: " + x, lst_check)

#Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.
countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = filter(lambda x: x[0]=="B", countries)


#Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [person[1] for person in people]

#Use list comprehension to create a list called lst2 that doubles each element in the list, lst.

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [item*2 for item in lst]


#Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = []
for student in students:
    if student[1] >= 70:
        passed.append(student[0])
        
passed = [student[0] for student in students if student[1] >= 70]


#Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

l3 = zip(l1, l2)
opposites = filter(lambda x: len(x[0]) > 3 and len(x[1]) > 3, l3)

print(opposites)


#Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info = list(zip(species, population))

endangered = [name for (name, pop) in pop_info if pop < 2500]
print(endangered)


"""
FINAL PROJECT

This project will take you through the process of mashing up data from two different APIs to make movie 
recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, 
and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get 
back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).
You will put those two together. You will use TasteDive to get related movies for a whole list of titles. 
You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes 
scores (which will require making API calls to the OMDB API.)

To avoid problems with rate limits and site accessibility, we have provided a cache file with results for 
all the queries you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather 
than requests.get(). If you’re having trouble, you may not be formatting your queries properly, or you may 
not be asking for data that exists in our cache. We will try to provide as much information as we can to 
help guide you to form queries for which data exists in the cache.

Your first task will be to fetch data from TasteDive. The documentation for the API is at 
https://tastedive.com/read/api.

Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is 
the name of a movie or music artist. The function should return the 5 TasteDive results that are associated 
with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with 
just one key, ‘Similar’.

Try invoking your function with the input “Black Panther”.

HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. 
If any other parameters are included, then the function will not be able to recognize the data that you’re 
attempting to pull from the cache. Remember, you will not need an api key in order to complete the project, 
because all data will be found in the cache.
"""

import requests_with_caching
import json

def get_movies_from_tastedive(movie_name):
    base_url = "https://tastedive.com/api/similar"
    parameters = {}
    parameters["q"] = movie_name
    parameters["type"] = "movies"
    parameters["limit"] = 5
    
    resp = requests_with_caching.get(base_url, params=parameters)
    print(resp.url)
    
    return resp.json()


# Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
import requests_with_caching
import json
    
def extract_movie_titles(resp):
    # Go into dictionary, go into Similar, go into Results, then use "Name" as the key
    list_of_titles = [item["Name"] for item in resp["Similar"]["Results"]]
    return list_of_titles



# Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
def get_related_titles(movie_list):
    related_titles = []
    
    for movie in movie_list:
        similar_title_list = extract_movie_titles(get_movies_from_tastedive(movie))
        related_titles = related_titles + similar_title_list
    
    return list(set(related_titles))


"""
Your next task will be to fetch data from OMDB. The documentation for the API is at 
https://www.omdbapi.com/

Define a function called get_movie_data. It takes in one parameter which is a string that should 
represent the title of a movie you want to search. The function should return a dictionary with 
information about that movie.

Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you 
won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, 
be sure to only include those two parameters in order to extract existing data from the cache.
"""


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")
import json
import requests_with_caching

def get_movie_data(movie_name):
    base_url = "http://www.omdbapi.com/"
    parameters = {}
    parameters["t"] = movie_name
    parameters["r"] = "json"
    
    resp = requests_with_caching.get(base_url, params = parameters)
    print(resp.url)
    return resp.json()


# Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
def get_movie_rating(resp):
    # Go into the dictionary for on Ratings key
    ratings_dict = resp["Ratings"]
    rating = 0
    for item in ratings_dict:
        if item["Source"] == "Rotten Tomatoes":
            rating = int(item["Value"][:-1])
    return rating


#Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
import requests_with_caching
import json

## Taste Dive Functions
def get_movies_from_tastedive(movie_name):
    base_url = "https://tastedive.com/api/similar"
    parameters = {}
    parameters["q"] = movie_name
    parameters["type"] = "movies"
    parameters["limit"] = 5
    
    resp = requests_with_caching.get(base_url, params=parameters)

    # Returns a dictionary of results
    return resp.json()    

def extract_movie_titles(resp):
    # Go into dictionary, go into Similar, go into Results, then use "Name" as the key
    list_of_titles = [item["Name"] for item in resp["Similar"]["Results"]]
    return list_of_titles

def get_related_titles(movie_list):
    related_titles = []
    
    for movie in movie_list:
        similar_title_list = extract_movie_titles(get_movies_from_tastedive(movie))
        related_titles = related_titles + similar_title_list
    
    return list(set(related_titles))


## OMDB Functions
def get_movie_data(movie_name):
    base_url = "http://www.omdbapi.com/"
    parameters = {}
    parameters["t"] = movie_name
    parameters["r"] = "json"
    
    resp = requests_with_caching.get(base_url, params = parameters)

    return resp.json()

def get_movie_rating(resp):
    # Go into the dictionary for on Ratings key
    ratings_dict = resp["Ratings"]
    rating = 0
    for item in ratings_dict:
        if item["Source"] == "Rotten Tomatoes":
            rating = int(item["Value"][:-1])
    return rating


## Combine all together
def get_sorted_recommendations(movie_list):
    related_movies = get_related_titles(movie_list)
    
    movie_dict = {}
    for movie in related_movies:
        resp = get_movie_data(movie)
        movie_rating = get_movie_rating(resp)
        movie_dict[movie] = movie_rating
    
    # Sort by rating in descending order
    # Then alphabetical, also descending order
    movie_dict = sorted(movie_dict.items(), 
                        key = lambda x: (x[1], x[0]), reverse = True)
    
    movie_list = [x1 for (x1, x2) in movie_dict]
    return movie_list

result = get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
print(result)   
print(type(result))
