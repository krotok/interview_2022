#Используется для добавления функционала к шагам теста без изменения их кода
#Успользуется в :
#pytest-rerunfailures
#pytest-timeout
#pytest-allure (декораторы @allure.step)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def say_hello(name):
    print(f"Hello {name}")

say_hello("Alice")
