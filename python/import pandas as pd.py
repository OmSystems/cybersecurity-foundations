import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

FILE_NAME = "task_progress.csv"


def prompt_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")


# Create file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=[
        "Date",
        "Total Tasks",
        "Completed Tasks",
        "Completion %",
        "Streak Earned"
    ])
    df.to_csv(FILE_NAME, index=False)


def add_day_progress():

    date = datetime.now().strftime("%Y-%m-%d")

    total_tasks = prompt_positive_int("Enter total tasks today: ")
    completed_tasks = prompt_positive_int("Enter completed tasks today: ")

    if total_tasks == 0:
        print("Total tasks cannot be zero. Please enter at least 1.")
        return

    if completed_tasks > total_tasks:
        print("Completed tasks cannot exceed total tasks.")
        return

    completion = round((completed_tasks / total_tasks) * 100, 2)

    streak = 1 if completed_tasks == total_tasks else 0

    new_data = pd.DataFrame({
        "Date": [date],
        "Total Tasks": [total_tasks],
        "Completed Tasks": [completed_tasks],
        "Completion %": [completion],
        "Streak Earned": [streak]
    })

    existing = pd.read_csv(FILE_NAME)

    existing = pd.concat([existing, new_data], ignore_index=True)

    existing.to_csv(FILE_NAME, index=False)

    print("\nProgress Saved!")

    if streak:
        print("🔥 Perfect Day! +1 Streak Earned")
    else:
        print("❌ No Streak Today")


def show_statistics():

    df = pd.read_csv(FILE_NAME)

    if len(df) == 0:
        print("No data available.")
        return

    total_days = len(df)
    avg_completion = df["Completion %"].mean()
    total_streaks = df["Streak Earned"].sum()

    print("\n===== STATISTICS =====")
    print(f"Days Tracked: {total_days}")
    print(f"Average Completion: {avg_completion:.2f}%")
    print(f"Total Streaks: {total_streaks}")
    print("======================")


def show_graphs():

    df = pd.read_csv(FILE_NAME)

    if len(df) == 0:
        print("No data available.")
        return

    plt.figure(figsize=(12,6))

    df_plot = df.copy()
    df_plot["Date"] = pd.to_datetime(df_plot["Date"], errors="coerce")
    df_plot = df_plot.sort_values("Date")

    plt.plot(
        df_plot["Date"],
        df_plot["Completion %"],
        marker="o"
    )

    plt.title("Daily Productivity")
    plt.xlabel("Date")
    plt.ylabel("Completion %")
    plt.xticks(rotation=45)

    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # Streak Graph
    plt.figure(figsize=(10,5))

    cumulative_streak = df_plot["Streak Earned"].cumsum()

    plt.plot(
        df_plot["Date"],
        cumulative_streak,
        marker="o"
    )

    plt.title("Total Streak Growth")
    plt.xlabel("Date")
    plt.ylabel("Streak Count")

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.tight_layout()
    plt.show()


def main():

    while True:

        print("\n===== TASK TRACKER =====")
        print("1. Add Today's Progress")
        print("2. Show Statistics")
        print("3. Show Graphs")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_day_progress()

        elif choice == "2":
            show_statistics()

        elif choice == "3":
            show_graphs()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()