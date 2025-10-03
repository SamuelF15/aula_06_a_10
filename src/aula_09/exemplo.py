import time

from utils_log import log_decorator, time_measure_decorator


@log_decorator
@time_measure_decorator
def soma(x, y):
    time.sleep(2)
    return x + y


soma(2, 3)
# soma(10, '15')  # Isso vai gerar um erro de tipo
