from github import Github


GIT_ACCESS_TOKEN = "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"
USERNAME = "prathikasundar@gmail.com"
PASSWORD = "Keerthu@2021"
BRANCH_TO_MERGE = "master"
REPO_NAME = "Prathika/Python_Utils"

import pdb;pdb.set_trace()
# LOGIN
git_obj = Github(GIT_ACCESS_TOKEN)

# GET REPO
repo_obj = git_obj.get_repo(REPO_NAME)

# GET ALL PR
# pr_list = repo_obj.get_pulls()
# pr_obj = pr_list.get_page(0)

# MERGE
base = repo_obj.get_branch(BRANCH_TO_MERGE)
head = repo_obj.get_branch(BRANCH_TO_BE_MERGED)
merge_to_master = repo_obj.merge(BRANCH_TO_MERGE, head.commit.sha, head.name))
