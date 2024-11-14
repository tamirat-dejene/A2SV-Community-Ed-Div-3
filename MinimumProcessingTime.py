class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        sorted_tasks = sorted(tasks)
        sorted_processor_time = sorted(processorTime, reverse=True)

        # the idea is assining the shorter tasks to processors that becomes available later

        i = 0
        minim = None
        for processor_time in sorted_processor_time:
            maxim = max([task + processor_time for task in sorted_tasks[i:i+4]])
            minim = maxim if minim == None else max(minim, maxim)
            i += 4
        
        return minim


            



        
