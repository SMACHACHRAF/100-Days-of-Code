bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))#decimal kahaw
print(round(bmi))#arroundi
print(round(3.738492)) # Becomes 4

print(round(3.14159)) # Becomes 3

print(round(3.14159, 2)) # Becomes 3.14

score = 0
score += 1
print(score)
score -= 2
print(score)

#F-strings
print("your scoree is "+str(score))

score =0
height = 1.8
is_winnig = True
print(f"your score is ={score}, your height is {height}. you are winnig is {is_winnig}")
