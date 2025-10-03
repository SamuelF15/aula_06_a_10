from functools import wraps

from loguru import logger
from tenacity import retry, stop_after_attempt, wait_fixed

logger.remove()

logger.add(
    "src/aula_08/logger_info.log",
    format="{time} | {level} | {module}:{function}:{line} - {message}",
    level="INFO",
)

logger.add(
    "src/aula_08/logger_critical.log",
    format="{time} | {level} | {module}:{function}:{line} - {message}",
    level="CRITICAL",
)


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}"
        )
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Exception(f"Erro na função '{func.__name__}': {e}")

    return wrapper


def time_measure_decorator(func):
    import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.info(
            f"Função '{func.__name__}' executada em {elapsed_time:.4f} segundos"
        )
        print(f"Função '{func.__name__}' executada em {elapsed_time:.4f} segundos")
        return result

    return wrapper


def retry_decorator(func):
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1.5))
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = input(
            f"Digite 'ok' para continuar com a execução de '{func.__name__}': "
        )

        try:
            result = func(*args, **kwargs)
            print(f"'{func.__name__}' sucesso.")
            return result
        except Exception as e:
            print(f"'{func.__name__}' falhou. Tentando novamente...")
            raise e

    return wrapper
