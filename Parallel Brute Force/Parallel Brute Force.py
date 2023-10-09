import itertools
import multiprocessing

def brute_force(charset, length):
    for attempt in itertools.product(charset, repeat=length):
        yield ''.join(attempt)

def check_password(password, guess):
    return password == guess

def parallel_brute_force(password, charset, length, num_processes):
    manager = multiprocessing.Manager()
    result_queue = manager.Queue()

    def worker(password, charset, length, result_queue):
        for guess in brute_force(charset, length):
            if check_password(password, guess):
                result_queue.put(guess)
                break

    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=worker, args=(password, charset, length, result_queue))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    if not result_queue.empty():
        return result_queue.get()
    else:
        return None

if __name__ == '__main__':
    password = 'password123'
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(password)
    num_processes = multiprocessing.cpu_count()

    cracked_password = parallel_brute_force(password, charset, length, num_processes)
    if cracked_password:
        print(f'Password cracked: {cracked_password}')
    else:
        print('Password not cracked')
