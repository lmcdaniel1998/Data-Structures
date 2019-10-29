import random
import time


def selection_sort(list):
    comparisons = 0
    for idx_sort in range(len(list) - 1, 0, -1):
        current_max = 0
        for idx_comp in range(1, idx_sort + 1):
            comparisons += 1
            if list[idx_comp] > list[current_max]:
                current_max = idx_comp
        temp = list[idx_sort]
        list[idx_sort] = list[current_max]
        list[current_max] = temp
    return comparisons


def insertion_sort(list):
    comparisons = 0
    for idx in range(1, len(list)):
        current = list[idx]
        pos = idx
        while pos > 0:
            if current < list[pos - 1]:
                comparisons += 1
                list[pos] = list[pos - 1]
                list[pos - 1] = current
                pos = pos - 1
            else:
                comparisons += 1
                break
    return comparisons


def main():
    # Give the random number generator a seed, so the same sequence of
    # random numbers is generated at each run
    random.seed(1234)
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)
    '''
    # ---------------------------------------------------#
    # Selection Sort 1000 items
    random.seed(7541)
    ss_random_1000 = random.sample(range(10000), 1000)
    ss_start_time_1000 = time.time()
    ss_comp_1000 = selection_sort(ss_random_1000)
    ss_end_time_1000 = time.time()
    ss_time_1000 = ss_end_time_1000 - ss_start_time_1000
    print("selection sort 1000 items, comparisons : " + str(ss_comp_1000) + " ,run time : " + str(ss_time_1000))

    # ---------------------------------------------------#
    # Selection Sort 2000 items
    random.seed(2345)
    ss_random_2000 = random.sample(range(10000), 2000)
    ss_start_time_2000 = time.time()
    ss_comp_2000 = selection_sort(ss_random_2000)
    ss_end_time_2000 = time.time()
    ss_time_2000 = ss_end_time_2000 - ss_start_time_2000
    print("selection sort 2000 items, comparisons : " + str(ss_comp_2000) + " ,run time : " + str(ss_time_2000))

    # ---------------------------------------------------#
    # Selection Sort 4000 items
    random.seed(76556)
    ss_random_4000 = random.sample(range(10000), 4000)
    ss_start_time_4000 = time.time()
    ss_comp_4000 = selection_sort(ss_random_4000)
    ss_end_time_4000 = time.time()
    ss_time_4000 = ss_end_time_4000 - ss_start_time_4000
    print("selection sort 4000 items, comparisons : " + str(ss_comp_4000) + " ,run time : " + str(ss_time_4000))

    # ---------------------------------------------------#
    # Selection Sort 8000 items
    random.seed(1917)
    ss_random_8000 = random.sample(range(10000), 8000)
    ss_start_time_8000 = time.time()
    ss_comp_8000 = selection_sort(ss_random_8000)
    ss_end_time_8000 = time.time()
    ss_time_8000 = ss_end_time_8000 - ss_start_time_8000
    print("selection sort 8000 items, comparisons : " + str(ss_comp_8000) + " ,run time : " + str(ss_time_8000))

    # ---------------------------------------------------#
    # Selection Sort 16000 items
    random.seed(1111111)
    ss_random_16000 = random.sample(range(100000), 16000)
    ss_start_time_16000 = time.time()
    ss_comp_16000 = selection_sort(ss_random_16000)
    ss_end_time_16000 = time.time()
    ss_time_16000 = ss_end_time_16000 - ss_start_time_16000
    print("selection sort 16000 items, comparisons : " + str(ss_comp_16000) + " ,run time : " + str(ss_time_16000))

    # ---------------------------------------------------#
    # Selection Sort 32000 items
    random.seed(48392)
    ss_random_32000 = random.sample(range(100000), 32000)
    ss_start_time_32000 = time.time()
    ss_comp_32000 = selection_sort(ss_random_32000)
    ss_end_time_32000 = time.time()
    ss_time_32000 = ss_end_time_32000 - ss_start_time_32000
    print("selection sort 32000 items, comparisons : " + str(ss_comp_32000) + " ,run time : " + str(ss_time_32000))
    '''






    # ---------------------------------------------------#
    # Insertion Sort 1000 items
    random.seed(7541)
    is_random_1000 = random.sample(range(10000), 1000)
    is_start_time_1000 = time.time()
    is_comp_1000 = insertion_sort(is_random_1000)
    is_end_time_1000 = time.time()
    is_time_1000 = is_end_time_1000 - is_start_time_1000
    print("insertion sort 1000 items, comparisons : " + str(is_comp_1000) + " ,run time : " + str(is_time_1000))

    # ---------------------------------------------------#
    # Insertion Sort 2000 items
    random.seed(2345)
    is_random_2000 = random.sample(range(10000), 2000)
    is_start_time_2000 = time.time()
    is_comp_2000 = insertion_sort(is_random_2000)
    is_end_time_2000 = time.time()
    is_time_2000 = is_end_time_2000 - is_start_time_2000
    print("insertion sort 2000 items, comparisons : " + str(is_comp_2000) + " ,run time : " + str(is_time_2000))

    # ---------------------------------------------------#
    # Insertion Sort 4000 items
    random.seed(76556)
    is_random_4000 = random.sample(range(10000), 4000)
    is_start_time_4000 = time.time()
    is_comp_4000 = insertion_sort(is_random_4000)
    is_end_time_4000 = time.time()
    is_time_4000 = is_end_time_4000 - is_start_time_4000
    print("insertion sort 4000 items, comparisons : " + str(is_comp_4000) + " ,run time : " + str(is_time_4000))

    # ---------------------------------------------------#
    # Insertion Sort 8000 items
    random.seed(1917)
    is_random_8000 = random.sample(range(10000), 8000)
    is_start_time_8000 = time.time()
    is_comp_8000 = insertion_sort(is_random_8000)
    is_end_time_8000 = time.time()
    is_time_8000 = is_end_time_8000 - is_start_time_8000
    print("insertion sort 8000 items, comparisons : " + str(is_comp_8000) + " ,run time : " + str(is_time_8000))

    # ---------------------------------------------------#
    # Insertion Sort 16000 items
    random.seed(1111111)
    is_random_16000 = random.sample(range(100000), 16000)
    is_start_time_16000 = time.time()
    is_comp_16000 = insertion_sort(is_random_16000)
    is_end_time_16000 = time.time()
    is_time_16000 = is_end_time_16000 - is_start_time_16000
    print("insertion sort 16000 items, comparisons : " + str(is_comp_16000) + " ,run time : " + str(is_time_16000))

    # ---------------------------------------------------#
    # Insertion Sort 32000 items
    random.seed(48392)
    is_random_32000 = random.sample(range(100000), 32000)
    is_start_time_32000 = time.time()
    is_comp_32000 = insertion_sort(is_random_32000)
    is_end_time_32000 = time.time()
    is_time_32000 = is_end_time_32000 - is_start_time_32000
    print("insertion sort 32000 items, comparisons : " + str(is_comp_32000) + " ,run time : " + str(is_time_32000))


if __name__ == '__main__': 
    main()
