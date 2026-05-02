''' 
    Sort the Summary
    You are given an array of integers. Your task is to construct a 2D array where:

    - The first element of each row is a distinct value from the array.
    - The second element is the frequency of that value in the array.

    After constructing this 2D array, sort it using the following rules:

    - Sort by frequency in descending order.
    - If two values have the same frequency, sort by the value in ascending order.

    Return the sorted 2D array.

    Example
    Input: arr = [3, 3, 1, 2, 1]
    Output: [[1, 2], [3, 2], [2, 1]]
'''
def groupSort(arr):
    freq_list = []

    # go through each item in the input array
    for item in arr:
        # flag to check if the item is already in the frequency list
        found = False

        # go through the frequency list to find the item
        for pair in freq_list:
            # check the first element of the pais
            if pair[0] == item:
                pair[1] += 1
                found = True
                break

        if not found:
            freq_list.append([item, 1])


    # Sort by frequency (descending) and then by value (ascending)
    freq_list.sort(key=lambda x : x[0])

    freq_list.sort(key=lambda x : x[1], reverse=True)

    return freq_list;

# Teste com input de exemplo
if __name__ == "__main__":
    arr = [3, 3, 1, 2, 1]
    result = groupSort(arr)
    print("Input:", arr)
    print("Output:", result)
    