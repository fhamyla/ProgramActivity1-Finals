import time
import heapq

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time

    def __repr__(self):
        return f"Process {self.pid} (Arrival: {self.arrival_time}, Burst: {self.burst_time})"


def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    schedule = []
    
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        current_time += process.burst_time
        schedule.append((process.pid, current_time))
    
    return schedule


def sjf_preemptive(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    schedule = []
    ready_queue = []
    idx = 0

    while idx < len(processes) or ready_queue:
        while idx < len(processes) and processes[idx].arrival_time <= current_time:
            heapq.heappush(ready_queue, (processes[idx].burst_time, processes[idx]))
            idx += 1

        if ready_queue:
            burst_time, process = heapq.heappop(ready_queue)
            schedule.append((process.pid, current_time))
            current_time += process.burst_time
            process.remaining_time = 0
        else:
            current_time += 1

    return schedule


def display_schedule(schedule):
    print("Process Execution Order:")
    for pid, time in schedule:
        print(f"Process {pid} finished at time {time}")


def loading_screen():
    print("************************************")
    print("* CPU scheduler by Fhamyla De Vera *")
    print("************************************")
    input("Click Enter to proceed.")
    print("\nLoading...")
    time.sleep(3)


def main():
    loading_screen()

    processes = [
        Process(pid=1, arrival_time=0, burst_time=8, priority=1),
        Process(pid=2, arrival_time=1, burst_time=4, priority=2),
        Process(pid=3, arrival_time=2, burst_time=9, priority=3),
        Process(pid=4, arrival_time=3, burst_time=5, priority=4)
    ]
    
    print("Choose the scheduling algorithm:")
    print("1: First Come First Serve (Non-Preemptive)")
    print("2: Shortest Job First (Preemptive)")
    choice = int(input("Enter choice (1 or 2): "))
    print("\nLoading...")
    time.sleep(3)
    
    if choice == 1:
        print("Running First Come First Serve Scheduling (Non-Preemptive)...")
        schedule = fcfs_scheduling(processes)
    elif choice == 2:
        print("Running Shortest Job First Scheduling (Preemptive)...")
        schedule = sjf_preemptive(processes)
    else:
        print("Invalid choice. Exiting.")
        return

    display_schedule(schedule)


if __name__ == "__main__":
    main()