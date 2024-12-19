#!/usr/bin/env python3

task = input("Input task description: ")
task_priority = input("Is the task priority high, medium or low? ")
time_bound = input("Is the task time-bound? (yes/no): ").lower()

match task_priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task.Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a medium priority task.Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a low priority task.Consider completing it when you have free time.")
