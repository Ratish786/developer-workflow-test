import json
from pathlib import Path


def main():

    jobs = sorted(Path("jobs").glob("*.json"))

    if not jobs:
        print("No workflow jobs found.")
        return

    latest_job = jobs[-1]

    print("=" * 60)
    print("DEVELOPER WORKFLOW ENGINE")
    print("=" * 60)

    print(f"\nProcessing Job : {latest_job.name}\n")

    with open(latest_job, "r", encoding="utf-8") as file:
        data = json.load(file)

    print(f"Status : {data['status']}")
    print(f"Created: {data['created_at']}\n")

    for index, task in enumerate(data["tasks"], start=1):

        print("-" * 60)
        print(f"Task {index}")
        print("-" * 60)

        for key, value in task.items():
            print(f"{key:<20}: {value}")

        print()


if __name__ == "__main__":
    main()