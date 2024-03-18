#Question
'''
Implement the naive string matching and print the starting indices of the pattern (P) in the text (T). In case of more than one occurrence, print the starting indices comma-separated. If the pattern is not present, print -1. Count the indices from 0. 

Input format
Read the T in the first line

Read P in the next line

Output Format
Print the starting locations of the pattern in the text comma-separated. If not found, print -1. 
'''
def naive(text, pattern):
    textlen = len(text)
    patlen = len(pattern)

    difference = textlen-patlen

    array = []

    for i in range(difference+1):
        for j in range(patlen):
            if (text[i+j] != pattern[j]):
                break
        
        if j == patlen-1:
            array.append(i)
        
    if (len(array)>0):
        for i in array:  print("pattern found at index value: ", i)
    else:
        print(-1)

text = input("Enter the Text string: ")
pattern = input("Enter the Pattern string: ")

naive(text, pattern)