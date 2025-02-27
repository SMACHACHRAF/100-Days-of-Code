#dictionary with a liste
capitals ={
    "France":"Paris",
    "Germany":"Berlin"
}
#nested list in a dictionary
"""
travel_log={
    "France":["paris","lille","lyon"],
    "germany":["berlin","dortmund"]
}"""

#print lille
#print(travel_log["France"][1])

nasted_list=["A","B",["c","d"]]
#affiche d
print(nasted_list[2][1])
travel_log ={
    "France":{
        "num_times_visited":8,
        "cities_visited":["Paris","Lille","Dijon"]
    },
    "Germany":{
        "num_times_visited":12,
        "cities_visited":["berlin","dortmund","stuttgard"]
    }
}
print(travel_log["Germany"]["cities_visited"][2])