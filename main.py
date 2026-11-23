import os
import requests

# Personal access token with the "read_api" scope, e.g.
#   export GITLAB_TOKEN="glpat-xxxxxxxxxxxxxxxxxxxx"
token = os.environ.get("GITLAB_TOKEN")
if not token:
    raise SystemExit("GITLAB_TOKEN is not set. Create a personal access token in GitLab "
                     "(Settings > Access Tokens, scope 'read_api') and export it.")

response = requests.get(
    "https://gitlab.com/api/v4/projects",
    headers={"PRIVATE-TOKEN": token},
    params={"membership": True, "per_page": 100},
)
response.raise_for_status()
my_projects = response.json()

# print the whole objects list
print(my_projects)
print(type(my_projects))

# print just the names and urls
for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['http_url_to_repo']}\n")
