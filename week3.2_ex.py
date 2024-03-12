parties = {
    "Person_A":{
        "apple":5,
        "orange":2
    },
    "Person_B":{
        "cherry":3,
        "orange":1,
        "apple":3
    },
    "Person_C":{
        "grape":10,
        "mango":6
    }
    
}
total = {
    # "apple":5,
    # "orange":2     
}
for person,fruits in parties.items():
     # person = Person_A
     # fruits = {"apple":5,"orange":2}
     for fruit,amount in fruits.items():
          #fruit = apple
          #amount = 5
          #if exist ? increase
          current = total.get(fruit, 0)
          #print(current)
          total[fruit] = current + amount
print(total)
