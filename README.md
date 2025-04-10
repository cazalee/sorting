# rafzy

Sorting Algorithms: 

A sorting algorithm is an algorithm that puts elements of a list in a certain order. The most frequently used orders are numerical order and lexicographical/alphabetical order. Efficient sorting is important for optimizing the use of other algorithms such as searching and merging, which require input data to be in sorted lists.

Efficiency of Sorting Algorithms
There are many different sorting algorithms and each has its own advantages and limitations. As I said, sorting is a basic building block that many other algorithms are built on. Therefore, it is important to know how sorting algorithms work and their relative efficiency.

Efficiency in an algorithm is defined in terms of the time complexity and space complexity, which we've already talked about. As a reminder, time complexity is a measure of the amount of time it takes for the algorithm to run. Space complexity is a measure of the amount of memory space it takes for the algorithm to run.

Sorting algorithm performance can be classified by:

1.Best case complexity: the minimum possible number of operations required to sort the data.
2.Average case complexity: the average number of operations required to sort the data.
3.Worst case complexity: the maximum number of operations required to sort the data.
4.Memory usage: the amount of memory space required to sort the data.

These are expressed using Big O notation. Most commone sorting Algorithms:

1.Insertion sort

2.Quick sort

3.Merge sort

4.Bubble sort

Strategies for sorting:

1.Recursion - Recursion can be used in sorting algorithms. We know that recursion is when a function calls itself with a smaller version of the input. We'll see how this can be used in sorting algorithms.

2.Divide and conquer - A divide and conquer algorithm works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem. This is very similar to recursion. We'll see how this can be used in sorting algorithms.

3. In-place sorting - An in-place sorting algorithm uses constant extra space for producing the output (modifies the given array only to produce the sorted array). It sorts the list only by modifying the order of the elements within the list. 


 # INSERTION SORT: 
Insertion sort is similar to how you would sort playing cards. You start with an empty left hand and the cards face down on the table. Then you remove one card at a time from the table and insert it into the correct position in the left hand. To find the correct position for a card, you compare it with each of the cards already in the hand. At all times, the cards held in the left hand are sorted.

An array is split into two parts: sorted and unsorted. Initially, the sorted part just has one element (the first element). Then, we pick an element from the unsorted part and insert it into the sorted part at the correct position. We do this until the unsorted part becomes empty.

![Image](https://github.com/user-attachments/assets/54abd2d0-3f46-466a-aba8-33524547827c)


[4, 3, 2, 10, 12, 1, 5, 6]

The first element is already sorted. So, we pick the second element (3) and compare it with the first element (4). Since 3 is smaller than 4, we swap them. Now, the first two elements are sorted.

[3, 4, 2, 10, 12, 1, 5, 6]

Next, we pick the third element (2) and compare it with the first element (3). Since 2 is smaller than 3, we swap them. Then, we compare 2 with 4 and swap them. Now, the first three elements are sorted.

[2, 3, 4, 10, 12, 1, 5, 6]

We continue this process until the unsorted part becomes empty.

a.Complexity & Efficiency
b.Worst-case time complexity: O(n^2)
c.Best-case time complexity: O(n^2)
d.Average-case time complexity: O(n^2)
e. Space complexity: O(1)
Online Sorting: Insertion sort is well-suited for "online" sorting, where new elements are continuously added to a sorted list. It efficiently adds new elements to the sorted portion, while something like selection sort, which we'll look at next, requires a full traversal of the unsorted portion for each new element.
For e.g. compared to a bubble sort, insertion sort requires less number of swaps, so it is slightly more efficient, especially when the array is partially sorted. However, it still has a time complexity of O(n2) because we still have to compare each element with all the other elements in the sorted part.



 
 # QUICK SORT: 

 Quick Sort Algorithm
The Quick Sort algorithm is a highly efficient divide-and-conquer sorting algorithm. It works by selecting a "pivot" element from the array and partitioning the other elements into two subarrays according to whether they are less than or greater than the pivot. The subarrays are then sorted recursively.

Quick Sort offers an average time complexity of O(n log n), making it one of the fastest sorting algorithms available. It's especially efficient for larger datasets. Quick sort has a better space complexity than a merge sort because merge Sort requires additional memory space to create temporary arrays during the merging process. When merging two subarrays, a temporary array is needed to hold the merged elements before they are placed back into the original array. This additional memory usage can be a drawback for Merge Sort, especially when dealing with very large arrays.

Example
Let's walk through an example using the array [20, 13, 3, 2, 10, 1, 5, 6] and choosing the pivot as 6: 

![quicksort1](https://github.com/user-attachments/assets/274c0597-0fa8-47d3-a373-d1ea4b2abd76)


 Choose the pivot element (6) and partition the array:

Pivot: 6
[20, 13, 3, 2, 10, 12, 1, 5, | 6]

Partition the array into two subarrays:

[3, 2, 1, 5] | [6, 20, 13, 10]
         
Left: Choose (3) pivot

  [2, 1] [3 5] 
           
Right: Choose (10) pivot
  [6] [10, 20, 13] 
           
At this point, 6 is done as there is only one element. This is our recursive case.

Left: Choose (2) pivot and (5) pivot
  [1] [2] [3] [5]
           
These are all done.

Right: choose (13) pivot
  [10] [13, 20]
           
10 is done. Now, (20) as pivot

 [13] [20]
          
Now there is no more than 1 value per array element and we can combine into one array: [1,2,3,5,6,10,13,20]



 # MERGE SORT
 The merge sort algorithm is a very efficient divide and conquer algorithm. It works by continuously splitting the array in half until it can no longer be divided. Then, it merges each subarray while sorting them in the process. This process continues until the whole array is sorted.

This is the most efficient solution that we've looked at so far. It has a time complexity of O(n log n), which signifies that its performance grows in a linearithmic fashion with the input size. This is different from O(log n), where the growth is purely logarithmic. So it isn't as fast as O(log n) but it's faster than O(n), especially for large data sets. It's definitely faster than the other algorithms we've looked at, which had complexities of O(n^2).

Let's look at an example:

![merge-sort](https://github.com/user-attachments/assets/62825fff-b556-4fbe-b1c8-0b6cea76f6aa)

[5, 3, 7, 1];
The first step is to split the array in half. We get two subarrays:

[5, 3][(7, 1)];
We split each subarray in half again:

[5][3][7][1];
Now that we can not go any further, we start merging each subarray while sorting them in the process:

[3, 5][(1, 7)];
We merge the two subarrays again:

[1, 3, 5, 7];
And we are done!



 # BUBBLE SORT: 

This is one of the simplest sorting algorithms. It's also one of the least efficient. But it's a good place to start because it's easy to understand. It is also a very common interview question.

What is Bubble Sort?
The Bubble sort sorting algorithm is comparison-based. Each pair of adjacent elements are compared with eachother and the elements are swapped if they are not in order. This is repeated until the list is sorted.

The algorithm gets its name from the way that smaller or larger elements "bubble" to the top of the list. Because it only uses comparisons to operate on elements, it is a comparison sort. Although the algorithm is simple, it is too slow and impractical for most problems even when compared to other sorting algorithms such as insertion sort. It can be practical if the input is usually in sort order but may occasionally have some out-of-order elements nearly in position.

How Does Bubble Sort Work?

Let`s look at an example. We have the following array of numbers:

[5, 4, 2, 1]

![bubble-sort](https://github.com/user-attachments/assets/f382d91e-b047-4351-9dcb-53c694227b14)

We start by comparing the first two elements in the array. If the first element is larger than the second element, we swap them. Otherwise, we leave them as is. In this case, 5 is larger than 4, so we swap them:

[4, 5, 2, 1]
Next, we compare the second and third elements in the array. If the second element is larger than the third element, we swap them. Otherwise, we leave them as is. In this case, 5 is larger than 2, so we swap them:

[4, 2, 5, 1]
Next, we compare the third and fourth elements in the array. If the third element is larger than the fourth element, we swap them. Otherwise, we leave them as is. In this case, 5 is larger than 1, so we swap them:

[4, 2, 1, 5]
We have now completed one pass through the array. We repeat this process until the array is sorted. In this case, we need to repeat the process three more times:

[2, 4, 1, 5]
[2, 1, 4, 5]
[1, 2, 4, 5]
Complexity & Efficiency
Worst-case time complexity: O(n^2)
Best-case time complexity: O(n)
Average-case time complexity: O(n^2)
Space complexity: O(1)

The worst-case time complexity is O(n^2) because we have to iterate through the array n times and for each iteration, we have to iterate through the array n times. This is because we have to compare each element with all the other elements in the array. What really makes bubble sorts inefficient is that it swaps elements multiple times per iteration. For example, in the first iteration, it swaps 5 and 4. Then, it swaps 5 and 2. Then, it swaps 5 and 1. It does this for each iteration. This is why the best-case time complexity is O(n). If the array is already sorted, we don't need to swap any elements.








