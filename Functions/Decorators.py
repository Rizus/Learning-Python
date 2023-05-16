def logger(func):
    def wrapped(num_list):
        result = func(num_list)
        with open('/home/pozdniakov/Desktop/all_my_project/Learning-Python/Functions/test.txt','w') as log_file:
            log_file.write(str(result))

        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


summator([1, 2, 3, 4, 5])
# with open('/home/pozdniakov/Desktop/all_my_project/Learning-Python/Functions/test.txt') as log_file:
#     print(log_file.read())


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#


import functools

def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('/home/pozdniakov/Desktop/all_my_project/Learning-Python/Functions/test.txt','w') as log_file:
            log_file.write(str(result))

        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


summator([1, 2, 3, 4, 5])
print(summator.__name__)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#


def logger2(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as log_file2:
                log_file2.write(str(result))
            return result
        return wrapped
    return decorator


@logger2('/home/pozdniakov/Desktop/all_my_project/Learning-Python/Functions/test.txt')
def summator(num_list):
    return sum(num_list)


summator([10, 20, 30, 400, 50])
