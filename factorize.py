from multiprocessing import Pool, cpu_count, freeze_support
import time


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize_sync(*numbers):
    results = []
    for number in numbers:
        result = factorize(number)
        results.append(result)
    return results


def factorize_parallel(*numbers):
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    return results


def test_factorize():
    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print("All wright")


if __name__ == '__main__':
    freeze_support()
    start_time = time.time()
    results_sync = factorize_sync(128, 255, 99999, 10651060)
    end_time = time.time()
    print("Synchroning time:", end_time - start_time)

    start_time = time.time()
    results_parallel = factorize_parallel(128, 255, 99999, 10651060)
    end_time = time.time()
    print("Parallel time:", end_time - start_time)

    test_factorize()
