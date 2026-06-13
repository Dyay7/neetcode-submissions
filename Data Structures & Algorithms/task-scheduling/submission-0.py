class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count how many times each task appears
        count = Counter(tasks)

        # We want to always run the task with the highest remaining count.
        # Python only has a MIN-heap, so we store NEGATIVE counts to simulate a MAX-heap.
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0

        # Queue to store tasks that are cooling down.
        # Each entry is: [remaining_count, time_when_task_can_run_again]
        q = deque()

        # Continue until all tasks are processed:
        # - heap has tasks ready to run
        # - queue has tasks cooling down
        while maxHeap or q:
            time += 1  # simulate one CPU cycle

            if not maxHeap:
                # No task is available to run right now.
                # Jump time forward to when the next cooling task becomes available.
                time = q[0][1]

            else:
                # Pop the task with the highest remaining count (most negative number)
                cnt = 1 + heapq.heappop(maxHeap)  
                # cnt is still negative; adding 1 reduces its magnitude (one task executed)

                if cnt:  
                    # If the task still has remaining executions,
                    # put it into cooldown until time + n
                    q.append([cnt, time + n])

            # If the earliest cooling task is now available, push it back into the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
