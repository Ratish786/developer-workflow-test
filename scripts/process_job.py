import json
from pathlib import Path


def get_latest_job():
    jobs = sorted(Path("jobs").glob("*.json"))

    if not jobs:
        print("No workflow jobs found.")
        return None

    return jobs[-1]


def process_task(index, task):

    print("=" * 60)
    print(f"Processing Task {index}")
    print("=" * 60)

    for key, value in task.items():
        print(f"{key:<20}: {value}")

    print("\nTask processed successfully.\n")


def main():

    job = get_latest_job()

    if job is None:
        return

    print("=" * 60)
    print("DEVELOPER WORKFLOW ENGINE")
    print("=" * 60)

    print(f"\nJob File : {job.name}")

    with open(job, "r", encoding="utf-8") as file:
        data = json.load(file)

    print(f"Status     : {data['status']}")
    print(f"Created At : {data['created_at']}")
    print(f"Total Tasks: {len(data['tasks'])}\n")

    for index, task in enumerate(data["tasks"], start=1):
        process_task(index, task)

    print("=" * 60)
    print("WORKFLOW FINISHED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()