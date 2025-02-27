programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing somethnig over and over again. "
    }

print(programming_dictionary["Bug"])
print(programming_dictionary["Loop"])

programming_dictionary["Ash"]="bonjour ash"
print(programming_dictionary)

#empty_dictionary={}
#programming_dictionary={}#clear the dictionary
#print(programming_dictionary)

programming_dictionary["Bug"] = "achraf smach"
print(programming_dictionary)

#loop
"""
for i in programming_dictionary:
    print(i)"""

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


