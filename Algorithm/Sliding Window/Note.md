### Pattern: Sliding window 滑动窗口类型

Generally speaking, a sliding window is a sub-list that runs over an underlying collection. Sliding window algorithm is used to perform required operation on specific window size of given large buffer or array. Window starts from the 1st element and keeps shifting right by one element. The objective is to find the minimum k numbers present in each window. This is commonly known as sliding window problem or algorithm. 

For example, to find the maximum or minimum element from every n element in given array, sliding window algorithm is used. 

Method 1:

First way is to use quick sort, when pivot is at Kth position, all elements on the right side are greater than pivot, hence, all elements on the left side automatically become K smallest elements of given array.

Method 2:

Keep an array of K elements, Fill it with first K elements of given input array. Now from K+1 element, check if the current element is less than the maximum element in the auxiliary array, if yes, add this element into array. Only problem with above solution is that we need to keep track of maximum element. Still workable. How can we keep track of maximum element in set of integer? Think heap. Think Max heap.

Method 3:

In O(1) we would get the max element among K elements already chose as smallest K elements . If max in current set is greater than newly considered element, we need to remove max and introduce new element in set of K smallest element. Heapify again to maintain the heap property. Now we can easily get K minimum elements in array of N.
