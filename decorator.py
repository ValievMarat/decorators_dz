import datetime

# задание 1, оставил функцию отдельно
def logger_1(some_function):
    filename = 'log.txt'

    def new_function(*args, **kwargs):
        time_calling = datetime.datetime.now()
        result = some_function(*args, **kwargs)

        with open(filename, 'a', encoding='utf-8') as f:
            f.write('-----------------\n')
            f.write(f'datetime: {time_calling}\n')
            f.write(f'function: {some_function.__name__}\n')
            f.write(f'args: {args}\n')
            f.write(f'kwargs: {kwargs}\n')
            f.write(f'result: {result}\n')

        return result

    return new_function


#задание 2, основной логгер
def logger(filename):

    def _logger(some_function):

        def new_function(*args, **kwargs):
            time_calling = datetime.datetime.now()
            result = some_function(*args, **kwargs)

            with open(filename, 'a', encoding='utf-8') as f:
                f.write('-----------------\n')
                f.write(f'datetime: {time_calling}\n')
                f.write(f'function: {some_function.__name__}\n')
                f.write(f'args: {args}\n')
                f.write(f'kwargs: {kwargs}\n')
                f.write(f'result: {result}\n')

            return result

        return new_function

    return _logger