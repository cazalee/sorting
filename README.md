# rafzy
 skills-foundry-dsa,sd,note.js.python

 # INSERTION SORT: 
 A simple algorithm 
 sorts an array by inserting each element into its correct position/place 
 In a sorted sub list 
 Features: 
 In pace sorting. No additional memory requirements 
 Adaptive
 efficient for smaller data sets 
 Quadratic Runtime efficiency = 0(n**2)
 
 # workings: 
 1. Split an array into two parts 
 2. One is sorted and the other unsorted
 3. Take element from unsorted part 
 4. compare it with those in the sorted sublist array 
 5. Shift any larger elemeents to the right 
 6. Thereby inserting elements in to their correction positions in sorted list 
 7. Repeat till all elements are sorted 

 # QUICK SORT: 
 Algorithm 
 Highly efficient divide and conquer technique 
 In place sorting - Adl memnory to sotre sorted array is not required 
 Widely used 
 Time complexity 0(nlogn) - Making it very fast for larger datasets 
 worst case scenario. For e.g. in reverse sort case time complexity degrrades to O(n^2)
 Not stable. Relative order of elements with same value might not be preserved

 # workings: 
 Quick sort -apply to a sequence of numbers we pass and followed by sub sequences we may create
 But only if the length is equal or greater than 1. lest, a return or in some cases - a base case
 so 
 selecting  a pivot element 
 partition array into 2 sub arrays: To be solved recrussively. 
 > elements smaller in value than pivot are placed before it 
 > lest after pivot 
 Recrussively sort : Apply same process 1. pivot and 2. partition on either sides of pivot 
 finally recursion stops when one element is left to sort in sub arrays 
 recrusion: process of calling same function (quicksort) on smaller subarrays for base case

 # MERGE SORT

 recrusion based alogrithm
 divide and conquer technique 
 Time complexity O(nlogn)
 Efficient, suitable and stable for large data sets 
 Needs additional space to store sorted sub arrays 

 # workings: 
 Recursion based - divivde and conquer technique 
 be used on linear structure like arrays or vectors
 When to be sorteed in increaing or decreasing order
 Uses first divide technique and then conquer 
 Base rule: ascertain the length be greater than 1.
 Part I: 
 Input array divided into 2 halves 
 until each sub array contains only one element(sorted)
 Part II: 
call merge sort function on each half to sort them recrusively 
 Part III: 
Merge: compare elements from 2 sorted arrays and place into a new sorted arrray: 
> compare leftmost element of one subarray with leftmost element of other subarray with indexing 
>> for e.g. i for tracking left most element of left sub array 
>> for e.g. j for tracking right most element of right sub array
>>> while assigning k as index for elements passed in the new sorted array 
>>> using inner while loops 
>>> and any left over elements in either sub arrays be passed eventually in the new sorted array


# BUBBLE SORT: 
simple algorithm 
sorts a list of items-repeatedly comparing & swapping adjacent elements if they are out of order
Useful when memory constraints are significant
Not suitable for large data sets because its average and worst case complexity are O(n^2)

# workings: 
Start at the beginning of the list
The Bubble Sort alg loops through every value in the array, comparing it to the value next to it.
If the first value is bigger, swap the positions of the two values
Keep going until there are no more items to compare
Go back to the start of the list








