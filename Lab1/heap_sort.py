import time



def heapify_max(array, size, i): 
    max_node = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    swaps_counter = 0
    comparisons_counter = 0

    if left_child < size:
        if array[left_child] > array[max_node]:
            max_node = left_child
        comparisons_counter += 1
    comparisons_counter += 1

    if right_child < size:
        if array[right_child] > array[max_node]:
            max_node = right_child
        comparisons_counter += 1
    comparisons_counter += 1

    if max_node != i:
        array[max_node], array[i] = array[i], array[max_node]
        swaps_counter += 1
        swaps_counter_increment, comparisons_counter_increment = heapify_max(array, size, max_node)
        swaps_counter += swaps_counter_increment
        comparisons_counter += comparisons_counter_increment

    return swaps_counter, comparisons_counter

def heapify_min(array, size, i): 
    min_node = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    swaps_counter = 0
    comparisons_counter = 0

    if left_child < size:
        if array[left_child] < array[min_node]:
            min_node = left_child
        comparisons_counter += 1
    comparisons_counter += 1

    if right_child < size:
        if array[right_child] < array[min_node]:
            min_node = right_child
        comparisons_counter += 1
    comparisons_counter += 1

    if min_node != i:
        array[min_node], array[i] = array[i], array[min_node]
        swaps_counter += 1
        swaps_counter_increment, comparisons_counter_increment = heapify_min(array, size, min_node)
        swaps_counter += swaps_counter_increment
        comparisons_counter += comparisons_counter_increment


    return swaps_counter, comparisons_counter

def heap_sort(array, sort_order = "asc"):
    start_time = time.perf_counter_ns()
    swaps_counter = 0
    comparisons_counter = 0

    size = len(array)
    last_parent_node = size // 2 -1

    if sort_order == "asc":
        for node in range(last_parent_node, -1, -1):
            heapify_max(array, size, node)
        
        for node in range(size - 1, 0, -1):
            array[node], array[0] = array[0], array[node]
            swaps_counter += 1
            swaps_counter_increment, comparisons_counter_increment = heapify_max(array, node, 0)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment

    elif sort_order == "desc":
        for node in range(last_parent_node, -1, -1):
            swaps_counter_increment, comparisons_counter_increment = heapify_min(array, size, node)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment

        for node in range(size - 1, 0, -1):
            array[node], array[0] = array[0], array[node]
            swaps_counter += 1
            swaps_counter_increment, comparisons_counter_increment = heapify_min(array, node, 0)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment

    else:
        print("Second arg must be one of these: asc, desc")
        return
    
    execution_time = time.perf_counter_ns() - start_time

    print("Heap sort:")
    print("Execution time:", execution_time, "ns")
    print("Comparisons:", comparisons_counter)
    print("Swaps:", swaps_counter)
    print(array)

    return array




