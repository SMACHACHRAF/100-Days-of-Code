import random
import my_module

'''
random_instance = Random() # instance de Random
random_integer = random_instance.randint(1, 10)
print(random_integer)
'''
'''
random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.my_favorite_number)
'''
'''
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)
#which generates a random float uniformly in the half-open range 0.0 <= X < 1.0
'''
'''
random_float = random.uniform(1,10)
print(random_float)
'''

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else :
    print("Tails")

