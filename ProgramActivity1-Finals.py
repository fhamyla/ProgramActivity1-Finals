import heapq

class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time  # Used for preemptive scheduling
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    time = 0
    for process in processes:
        if time < process.arrival_time:
            time = process.arrival_time
        time += process.burst_time
        process.completion_time = time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

def sjf_preemptive(processes):
    time = 0
    completed_processes = []
    ready_queue = []
    processes = sorted(processes, key=lambda x: x.arrival_time)
    index = 0
    
    while len(completed_processes) < len(processes):
        # Add processes that have arrived by the current time
        while index < len(processes) and processes[index].arrival_time <= time:
            heapq.heappush(ready_queue, (processes[index].burst_time, processes[index]))
            index += 1
        
        if ready_queue:
            burst_time, current_process = heapq.heappop(ready_queue)
            time += burst_time
            current_process.remaining_time -= burst_time
            
            if current_process.remaining_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes.append(current_process)
            else:
                heapq.heappush(ready_queue, (current_process.remaining_time, current_process))
        else:
            time += 1  # If no process is ready to run, increment time

def print_stats(processes):
    print(f"{'Process ID':<12}{'Arrival Time':<15}{'Burst Time':<15}{'Completion Time':<15}{'Turnaround Time':<20}{'Waiting Time':<15}")
    for process in processes:
        print(f"{process.process_id:<12}{process.arrival_time:<15}{process.burst_time:<15}{process.completion_time:<15}{process.turnaround_time:<20}{process.waiting_time:<15}")

def main():
    # Input processes
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    for i in range(num_processes):
        process_id = input(f"Enter Process {i + 1} ID: ")
        arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
        burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
        processes.append(Process(process_id, arrival_time, burst_time))

    # Choose the algorithm
    print("\nChoose scheduling algorithm:")
    print("1. First Come First Serve (Non-preemptive)")
    print("2. Shortest Job First (Preemptive)")
    choice = int(input())

    if choice == 1:
        print("\nRunning FCFS Scheduling Algorithm...\n")
        fcfs(processes)
        print_stats(processes)
    elif choice == 2:
        print("\nRunning SJF Preemptive Scheduling Algorithm...\n")
        sjf_preemptive(processes)
        print_stats(processes)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()