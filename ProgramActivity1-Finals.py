import heapq

class PrintJob:
    def __init__(self, job_id, arrival_time, num_pages):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.num_pages = num_pages
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def fcfs_printing(jobs):
    jobs.sort(key=lambda x: x.arrival_time)  # Sort jobs by arrival time
    current_time = 0
    for job in jobs:
        if current_time < job.arrival_time:
            current_time = job.arrival_time
        current_time += job.num_pages  # Printing takes time equal to the number of pages
        job.completion_time = current_time
        job.turnaround_time = job.completion_time - job.arrival_time
        job.waiting_time = job.turnaround_time - job.num_pages

def sjf_printing(jobs):
    current_time = 0
    completed_jobs = []
    ready_queue = []
    jobs = sorted(jobs, key=lambda x: x.arrival_time)  # Sort by arrival time
    index = 0
    
    while len(completed_jobs) < len(jobs):
        # Add jobs that have arrived by the current time
        while index < len(jobs) and jobs[index].arrival_time <= current_time:
            heapq.heappush(ready_queue, (jobs[index].num_pages, jobs[index]))
            index += 1
        
        if ready_queue:
            num_pages, current_job = heapq.heappop(ready_queue)
            current_time += num_pages
            current_job.completion_time = current_time
            current_job.turnaround_time = current_job.completion_time - current_job.arrival_time
            current_job.waiting_time = current_job.turnaround_time - current_job.num_pages
            completed_jobs.append(current_job)
        else:
            current_time += 1  # If no job is ready to be printed, increment time

def print_job_stats(jobs):
    print(f"{'Job ID':<10}{'Arrival Time':<15}{'Num Pages':<15}{'Completion Time':<20}{'Turnaround Time':<20}{'Waiting Time':<20}")
    for job in jobs:
        print(f"{job.job_id:<10}{job.arrival_time:<15}{job.num_pages:<15}{job.completion_time:<20}{job.turnaround_time:<20}{job.waiting_time:<20}")

def main():
    # Simulate print job submissions
    jobs = [
        PrintJob("Job 1", 0, 10),  # Job ID, Arrival Time, Pages
        PrintJob("Job 2", 2, 4),
        PrintJob("Job 3", 3, 7),
        PrintJob("Job 4", 5, 2)
    ]
    
    # Choose scheduling algorithm
    print("Choose scheduling algorithm:")
    print("1. FCFS (Non-preemptive)")
    print("2. SJF (Preemptive)")
    choice = int(input())
    
    if choice == 1:
        print("\nRunning FCFS Scheduling Algorithm for Print Jobs...\n")
        fcfs_printing(jobs)
        print_job_stats(jobs)
    elif choice == 2:
        print("\nRunning SJF Scheduling Algorithm for Print Jobs...\n")
        sjf_printing(jobs)
        print_job_stats(jobs)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()