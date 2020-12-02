results = [] 
number = 2000 

while number <= 3200: 
    if number % 7 == 0: 
        if number % 5 != 0: 
            results.append(number) 
    number +=1 

print(results) 