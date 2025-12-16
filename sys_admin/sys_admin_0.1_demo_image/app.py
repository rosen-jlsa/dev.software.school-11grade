import datatime 
import sys 
import os

TASKS_FILE = os.environ.get('TASKS_FILE', 'tasks.txt')
NOTIFICATION_ENABLED = os.environ.get('NOTIFICATION_ENABLED', 'true').lower() == 'true'

def get_current_day_week_and_number():
    now = datetime.now()
    #Monday is the 0, sunday is the 6
    day_of_week = now.weekday()
    # iso week number 
    week_number = now.isocalendar()[1]
    return day_of_week, week_number

    def load_task():
        task = {i: [] for i in range (7)}
        try:
            with open(TASK_FILE, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
        
       parts = line.split(':', 1)
       if len(parts) != 2:
        print(f"Warning: Skipping malformed task line: {line}", file=sys.stderr)
        continue
        day_specifier = parts[0].strip().lower()
        task_description = parts[1].strip()

        if day_specifier == 'dayly':
            for i in range (7):
                tasks[i].append(task_description)
                elif day_specifier.startswith('weekly-'):
                    try:
                        week_parity = day_specifier.split('-')[1]
                        if week_parity not in ['even', 'odd', 'all']:
                              print(f"Warning: Invalid weekly specifier '{week_parity}' in '{line}'. Use 'even', 'odd', or 'all'.", file=sys.stderr)
                             continue
                        tasks['weekly'].append((week_parity, task_description)) # Store weekly tasks separately for now
                    except IndexError:
                        print(f"Warning: Malformed weekly task specifier: {line}", file=sys.stderr)
                        continue
                else:
                    days_map = {
                        'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
                        'friday': 4, 'saturday': 5, 'sunday': 6
                    }
                    day_index = days_map.get(day_specifier)
                    if day_index is not None:
                        tasks[day_index].append(task_description)
                    else:
                        print(f"Warning: Unknown day specifier '{day_specifier}' in '{line}'", file=sys.stderr)
        return tasks
    except FileNotFoundError:
        print(f"Error: Tasks file '{TASKS_FILE}' not found. Please create it.", file=sys.stderr)
        return {i: [] for i in range(7)}

        def get_daily_tasks(tasks_data, current_day_of_week, current_week_number):
    daily_tasks_for_today = []

    # Add general daily tasks and specific day tasks
    daily_tasks_for_today.extend(tasks_data.get(current_day_of_week, []))

    # Add weekly tasks based on week number
    is_even_week = (current_week_number % 2 == 0)
    for parity, task_desc in tasks_data.get('weekly', []):
        if parity == 'all':
            daily_tasks_for_today.append(task_desc)
        elif parity == 'even' and is_even_week:
            daily_tasks_for_today.append(task_desc)
        elif parity == 'odd' and not is_even_week:
            daily_tasks_for_today.append(task_desc)

    return daily_tasks_for_today

def display_tasks_for_today():
    day_of_week, week_number = get_current_week_day_and_week_number()
    tasks_data = load_tasks()
    today_tasks = get_daily_tasks(tasks_data, day_of_week, week_number)

    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(f"\n--- Daily Task Notification for {day_names[day_of_week]} (Week {week_number}) ---")
    if today_tasks:
        for i, task in enumerate(today_tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No specific tasks scheduled for today.")
    print("-------------------------------------------------------------------\n")

if __name__ == "__main__":
    if NOTIFICATION_ENABLED:
        display_tasks_for_today()
    else:
        print("Notification feature is disabled. Set NOTIFICATION_ENABLED=true to enable.")