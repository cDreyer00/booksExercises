def quicksort(array):
    if (len(array) < 2):
        return array

    else:
        firstId = array[0]
        lesser = [i for i in array[1:] if i <= firstId]
        higher = [i for i in array[1:] if i > firstId]
        print([firstId])
        return quicksort((lesser)) + [firstId] + quicksort(higher)

print(quicksort([5 , 4]))