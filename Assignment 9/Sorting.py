#  File: Sorting.py
#  Description: This program performs tests on performance of 6 different sorting algorithms
#  Student's Name: Marcos Ortiz
#  Student's UT EID: mjo579
#  Course Name: CS 313E
#  Unique Number: 51320
#
#  Date Created: 11/12/2016
#  Date Last Modified: 11/18/2016

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def createList(t, n):

    if t == "Random":
        l = [i for i in range(n)]
        random.shuffle(l)
        return l

    elif t == "Sorted":
        l = [i for i in range(n)]
        return l

    elif t == "Reverse":
        l = [i for i in range(n-1, 0, -1)]
        return l

    else:
        l = [i for i in range(n)]
        numSwaps = int(len(l) * 0.1)

        for i in range(numSwaps):
            num1 = random.randint(0, len(l)-1)
            num2 = random.randint(0, len(l)-1)
            while num2 == num1:
                num2 = random.randint(0, len(l)-1)
            swap(l, num1, num2)
        return l

def main():

    #Declare list that will be used to perform tests accoring to specifications
    listLengths = [10,100,1000]
    listFunctions = ["bubbleSort", "selectionSort", "insertionSort", "shellSort", "mergeSort", "quickSort"]
    listType = ["Random", "Sorted", "Reverse", "Almost Sorted"]

    # 1. Begin tests for lists that are arranged in a specified matter
    for typeSort in listType:

        # 2. Print Header
        print("Input type = ", typeSort)
        print("                    avg time   avg time   avg time")
        print("   Sort function     (n=10)    (n=100)    (n=1000)")
        print("-----------------------------------------------------")

        # 3. Perform test for each type of function
        for function in listFunctions:
            resultString = "{:>16s}     ".format(function)

            # 4. Perform test for lists on specified lengths
            for listLength in listLengths:
                testTimes = 0

                # 5. Perform each test 5 times and average
                for j in range(5):
                    startTime = time.perf_counter()
                    eval(function+"(createList(typeSort, listLength))")
                    endTime = time.perf_counter()
                    elapsedTime = endTime - startTime
                    testTimes += elapsedTime

                # 6. Compute average and add them to current line print
                avgTime = testTimes / 5
                resultString += "{:6f}   ".format(avgTime)
            print(resultString)
        print()
main()
