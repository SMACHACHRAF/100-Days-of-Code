"""
Advanced Decorators
Create a logging_decorator() which is going to print the name of the function that was called, the arguments it was given and finally the returned output:

You called a_function(1,2,3)
It returned: 6
The value 6 is the return value of the function.
Don't change the body of a_function.
IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise.
"""
# Création du décorateur
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")  # Affichage du nom de la fonction et des arguments
        result = function(*args)  # Exécution de la fonction
        print(f"It returned: {result}")  # Affichage du résultat retourné
        return result  # Retourner la valeur de la fonction
    return wrapper

# Utilisation du décorateur
@logging_decorator
def a_function(*args):
    return sum(args)

# Appel de la fonction test
a_function(1, 2, 3)
