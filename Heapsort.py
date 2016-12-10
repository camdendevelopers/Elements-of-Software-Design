import random
import numpy

def heapify(alist):
    start = (len(alist) - 2) // 2     # the last internal node

    while start >= 0:
        #print("Sifting: start =",start," end =",len(alist)-1)
        siftDown(alist,start,len(alist)-1)
        start -= 1

def siftDown(alist,start,end):
    root = start
    #print("   siftDown: start =",start,"  end =",end)
    while root * 2 + 1 <= end:

        # initially, "child" is left child, "child+1" is right child
        child = root * 2 + 1

        # if there is a right child and it's bigger, use that
        if child + 1 <= end and alist[child] < alist[child + 1]:
            #print("      using right child")
            child += 1
        else:
            pass
            #print("      using left child")

        # if the bigger child is greater than parent, swap them
        if child <= end and alist[root] < alist[child]:
            #print("      swapping",alist[root],"and",alist[child])
            temp = alist[root]
            alist[root] = alist[child]
            alist[child] = temp
            root = child
        else:
            #print("      No need to swap",alist[root],"and",alist[child])
            #dummy = input()
            return

    #dummy = input()

def heapSort(alist):

    #print("Phase 1:  calling heapify to make the list a heap")
    heapify(alist)
    #print("alist",alist,"is now a heap.")
    #dummy = input()
    #print("\n\nPhase 2:")
    end = len(alist) - 1
    while end > 0:
        #print("moving root (largest element) to last position")
        #print("   swapping",alist[0],"and",alist[end])
        temp = alist[0]
        alist[0] = alist[end]
        alist[end] = temp
        #print("   end of list is now",end-1,". Resift to fix heap")
        siftDown(alist,0,end-1)
        end -= 1

def main():

    #myList = [13, 14, 94, 33, 82, 21, 59, 65, 23, 45, 27, 73, 25, 10]
    #myList = [3,1,7,5,2,8,4]
    myList = [x for x in range(100000)]

    random.shuffle(myList)



    heapSort(myList)
    print(myList)

main()
