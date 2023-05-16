from github import Github


GIT_ACCESS_TOKEN = ""
USERNAME = "prathikasundar@gmail.com"
PASSWORD = ""
BRANCH_TO_MERGE = "master"
REPO_NAME = "Prathika/Python_Utils"

# LOGIN
git_obj = Github(GIT_ACCESS_TOKEN)

# GET REPO
repo_obj = git_obj.get_repo(REPO_NAME)

# GET ALL PR
pr_list = repo_obj.get_pulls()
pr_obj = pr_list.get_page(0)
final_pr = pr_obj.pop()
branch = final_pr._rawData['head']['label']
BRANCH_TO_BE_MERGED = branch.split(":")[1]

# MERGE
base = repo_obj.get_branch(BRANCH_TO_MERGE)
head = repo_obj.get_branch(BRANCH_TO_BE_MERGED)
merge_to_master = repo_obj.merge(BRANCH_TO_MERGE, head.commit.sha, head.name)
