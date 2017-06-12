class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # sort the list by height in ascending order
        # in-place sorting
       	people.sort(key=lambda x: x[0])

        queue = self._reconstruct_queue_helper(0, len(people)-1, people)
        print(queue)



       	def _reconstruct_queue_helper(self, left, right, people):
       		if left>=right:
       			return 
       		pivot = people[left]
     		print(pivot)

          	# people[0][1] - number of positions to swap to the right
          	# add code here to count the number of people with the same height as pivot to the left of pivot 
         	# and subtract that from the number of positions to swap.
       		for j in range(pivot[1]):
        		people[j], people[j+1] = people[j+1], people[j]

        	self._reconstruct_queue_helper(left, people.index(pivot)-1, people)
        	self._reconstruct_queue_helper(people.index(pivot)+1, right, people)

        	return people



if __name__=='__main__':
  s = Solution()
  s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])


