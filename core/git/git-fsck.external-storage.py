import subprocess
from typing import Any, List, Optional, TypedDict
from concurrent.futures import Future, ThreadPoolExecutor
import os
import json

class ImportantRepo(TypedDict):
  name: str
  private: Optional[bool]


 
with open('{home}/Documents/repositories/my-notes/core/git/important-repos.json'.format(home=os.environ['HOME'])) as f:
  important_repos: List[ImportantRepo] = json.load(f)

def git_fsck(important_repo: ImportantRepo):
  important_repo_name=important_repo['name']

  username=os.environ['USERNAME']

  result: subprocess.CompletedProcess[bytes]  = subprocess.run(
    executable="/bin/bash",
    cwd='/media/{username}/backups/{important_repo_name}'.format(
      username=username,
      important_repo_name=important_repo_name
    ), 
    args='git fsck --no-dangling 2>&1',
    shell=True,
    capture_output=True
    )

  print(f'''-- {important_repo_name} --
{result.stdout.decode("utf-8")}''')
  
  if(result.returncode != 0):
    raise Exception();


with ThreadPoolExecutor(max_workers=2) as executor:
  futures: List[Future[Any]] = []

  for important_repo in important_repos:
    futures.append(executor.submit(git_fsck, important_repo))
  
  for future in futures:
    future.result()
  
