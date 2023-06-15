'''import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time} секунд.")
        return result
    return wrapper'''

'''@measure_time'''
def reverse(input_file, output_file) -> None:
    with open(input_file, 'r') as inp, open(output_file, 'w') as out:
        out.writelines(reversed(inp.readlines()))

'''@measure_time
def reverse1(input_file, output_file) -> None:
    with open(input_file, 'r') as inp, open(output_file, 'w') as out:
        out.writelines(inp.readlines()[::-1])'''

reverse('2_4_1/dataset_24465_4.txt','2_4_1/result.txt')
'''reverse1('2_4_1/dataset_24465_4.txt','2_4_1/result1.txt')'''
