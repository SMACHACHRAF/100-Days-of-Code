import time

# Définition du décorateur
def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()  # Capture du temps de début
        function()  # Exécution de la fonction
        end_time = time.time()  # Capture du temps de fin
        run_time = end_time - start_time  # Calcul du temps écoulé
        print(f"{function.__name__} run speed: {run_time}s")
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

# Exécution des fonctions décorées
fast_function()
slow_function()
