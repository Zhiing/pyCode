from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(10)

def test_function(num1, num2):
    print(num1, num2)
    return num1 + num2

future = executor.submit(test_function, 1, 2)
print(future.result())