import statistics
import numpy
class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def swap(distances, x, y):  
            temp = distances[x]  
            distances[x] = distances[y]  
            distances[y] = temp 
        
        #partition function
        def partition(distances, left, right, x): 
            for i in range(left, right): 
                if distances[i] == x: 
                    swap(distances, right, i) 
                    break
            x = distances[right]  
            i = left  
            for j in range(left, right):  
                if (distances[j] <= x):  
                    swap(distances, i, j)  
                    i += 1
            swap(distances, i, right)  
            return i
        
        #just insertion sort
        def getMed(distances, left, n): 
            hold = [] 
            for i in range(left, left+n):
                print(distances[i])
                hold.append(distances[i]) 
            for i in range(1, len(hold)):
                key = hold[i] 
                j = i-1
                while j >=0 and key < hold[j] : 
                        hold[j+1] = hold[j] 
                        j -= 1
                hold[j+1] = key 
            return hold[n//2]

        def kthSmallest(distances, left, right, kth, recursiontracker):     
            elementsInArray = right-left+1 
            print(right-left+1, recursiontracker)
            median = [] 
            i = 0
            #step1+2: divide into groups of 5
            while (i < elementsInArray // 5): 
                median.append(getMed(distances, left+i*5, 5)) 
                i += 1
                
            #groups less than 5 = n modulo 5
            if (i*5 < elementsInArray): 
                median.append(getMed(distances, left+i*5, elementsInArray %5))
                i += 1
            
            
            print(median)
            
            #base case:num elements = 1 | other: we recurse
            if i == 1: 
                MOM = median[i-1] 
                print(MOM) 
            #step 3
            else:
                MOM = kthSmallest(median, 0, i-1, i//2, recursiontracker-1) 
                print(MOM) 
                
            # Partition about MOM  
            # currentposition  = numpy.partition(distances, MOM)
            #step 4 
            currentposition = partition(distances, left, right, MOM) 

            #we are happy if currentposition = kth 
            #because this means we have found a solution  
            if (currentposition-left == kth-1):  
                print(distances)
                return distances[currentposition] 
            
            #step 5
            #left array 
            if (currentposition-left > kth-1):  
                return kthSmallest(distances, left, currentposition-1, kth,recursiontracker -1) 
                print(distances)
            #right array
            return kthSmallest(distances, currentposition+1, right, kth-currentposition + left-                                                                         1, recursiontracker -1) 
        distances = [i[0]**2+i[1]**2 for i in points]
        returnarr = []
        k = kthSmallest(distances, 0, len(distances)-1, K,len(distances))
        print(k)
        for i in range(len(points)):
            temp = points[i]
            
            if temp[0]**2 + temp[1]**2 <= k:
                returnarr.append(points[i]) 
        print(returnarr)
        return returnarr
