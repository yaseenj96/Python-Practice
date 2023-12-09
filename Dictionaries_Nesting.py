programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

dictionary = {"Key": "Value", 3: "Value2"}

#Retrieving items
print(dictionary["Key"])
print(dictionary[3])

#Adding new items to dictionary:
dictionary["Key3"] = "Here is the last value of the dictionary"

#Create empty dictionary
empty_dictionary = {}

#Wipe existing dictionary
# programming_dictionary = {}

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

#Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#NEsting
capitals = {"France": "Paris",
           "Germany": "Berlin",
           }

#Nesting a Dictionary in a Dictionary
travel_log = {
  "France" : {"cities_visited": ["Paris", "Dijon", "Lille"], "total_visits": 12},
  "Germany": {"cities_visited": ["Hamurg", "Berlin"], "total_visits": 12},
}

#Nesting Dictionary in a List
travel_log = [
  {
   "country": "France",
   "cities_visited": ["Paris", "Lille"], 
   "total_visits": 12
  },
  {
   "country": "Spain",
   "cities_visited": ["Seville", "Madrid", "Barthelona"], 
   "total_visits": 69
  },
]


## Blind Bidding code
from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bids = {}
print("Welcome to the secret auction program.\n")
other_bidders = 'yes'

while other_bidders == 'yes':
  name = input("What is your name?: \n")
  bid = input("What is your bid?: \n")
  bids[name] = int(bid)
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()

#Calculate highest bidder
max_bid = 0
for name in bids:
  if bids[name] > max_bid:
    max_bid = bids[name]
    max_name = name
    
print(f"The winner is {max_name} with a bid of ${max_bid}.")
