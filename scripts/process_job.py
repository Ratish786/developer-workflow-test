import json
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


def get_latest_job():

    jobs = sorted(Path("jobs").glob("*.json"))

    if not jobs:
        print("No workflow jobs found.")
        return None

    return jobs[-1]


def connect_sheet():

    credentials = Credentials.from_service_account_file(
        "service-account.json",
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)

    # We'll replace this with your real Sheet ID
    sheet = client.open_by_key("1AU-8yR3yicF-JrAXwh4BaWUGaAQazrNzEEE3Is-HfqI").sheet1

    return sheet


def main():

    job = get_latest_job()

    if job is None:
        return

    print(f"Processing {job.name}")

    with open(job, "r", encoding="utf-8") as file:
        data = json.load(file)

    sheet = connect_sheet()

    for task in data["tasks"]:

        row = [
            task.get("Module"),
            task.get("Task / Bug"),
            task.get("Description")
        ]

        sheet.append_row(row)

        print(f"Inserted : {task.get('Task / Bug')}")

    print("Workflow Finished Successfully")


if __name__ == "__main__":
    main()