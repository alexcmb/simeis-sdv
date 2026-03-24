import requests
from collections import Counter

OWNER = "alexcmb"
REPO = "simeis-sdv"

URL = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"


def get_issues():
    response = requests.get(URL)

    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")

    return response.json()

def count_labels(issues):
    counter = Counter()

    for issue in issues:
        labels = issue.get("labels", [])

        if not labels:
            counter["no-label"] += 1
            continue

        for label in labels:
            counter[label["name"]] += 1

    return counter

def main():
    issues=get_issues()
    # print(issues[:2])
    counter=count_labels(issues)
    print(counter)

if __name__ == "__main__":
    main()