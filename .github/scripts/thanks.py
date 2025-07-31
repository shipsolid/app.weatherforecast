import os
import requests
import sys

# --- Read and validate environment variables ---
token = os.getenv("GITHUB_TOKEN")
issue_number = os.getenv("ISSUE_NUMBER")
repo = os.getenv("REPO")  # Expected format: owner/repo

if not token or not issue_number or not repo:
    print("❌ Missing required environment variables: GITHUB_TOKEN, ISSUE_NUMBER, or REPO")
    sys.exit(1)

# --- Parse repo into owner and name ---
try:
    owner, repo_name = repo.split("/")
except ValueError:
    print("❌ REPO environment variable must be in 'owner/repo' format.")
    sys.exit(1)

# --- Set headers for GitHub API ---
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

# --- Create comment on the issue ---
comment_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues/{issue_number}/comments"
comment_body = {"body": "Thanks for your contribution!"}
comment_res = requests.post(comment_url, headers=headers, json=comment_body)

if comment_res.status_code != 201:
    print(f"❌ Failed to comment on issue: {comment_res.status_code}")
    print(comment_res.text)
    sys.exit(1)

comment_data = comment_res.json()
comment_id = comment_data.get("id")
print(f"✅ Comment posted with ID: {comment_id}")

# --- Add label to the issue ---
label_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues/{issue_number}/labels"
label_body = {"labels": ["todo-review"]}
label_res = requests.post(label_url, headers=headers, json=label_body)

if label_res.status_code not in [200, 201]:
    print(f"❌ Failed to add label: {label_res.status_code}")
    print(label_res.text)
    sys.exit(1)

print(f"✅ Label 'todo-review' added to issue #{issue_number}")

# --- Output comment ID to GitHub Actions ---
github_output = os.getenv("GITHUB_OUTPUT")
if github_output:
    with open(github_output, "a") as f:
        f.write(f"comment_id={comment_id}\n")
else:
    print("⚠️ GITHUB_OUTPUT not set, cannot export comment ID")
