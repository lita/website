"""Usage: publish.py -pc -m <comment>
          publish.py 

Process FILE and optionally apply correction to either left-hand side or
right-hand side.

Options:
  -h --help
  -p                push to litacho.github.io
  -c                commit and push to website git
  -m <comment>      comment
"""

import subprocess
import os

from path import path
from docopt import docopt

def gitCommitPush(workingDir, comment):
    os.chdir(workingDir)
    cmd = 'git add --all *'
    subprocess.call(cmd, shell=True)
    if comment:
        subprocess.call('git commit  -m ' + comment, shell=True)
    else:
        subprocess.call('git commit ', shell=True)

    try:
        subprocess.call('git push origin master')
    except:
        print "push failed"



def main(args):
    pushToDevGit = False
    pushToWebsite = False
    workingDir = path('/Users/litacho/Development/website')
    webDir = path('/Users/litacho/Development/litacho.github.io/')
    comment = None

    if args['-c']:
        pushToWebsite = True

    if args['-p']:
        pushToDevGit = True

    if args['-m']:
        comment = args['-m']

    # Set the environment
    subprocess.call(('source ' + 
                    workingDir + 
                    path('/blog_env/bin/activate')), shell=True)

    # Make the published htmls files
    subprocess.call('make publish', shell=True)

    #copy the publish files to litacho.github.io
    src = workingDir + path('/output/* ')
    cmd = 'cp -r ' + src + " " + webDir
    subprocess.call(cmd, shell=True)

    #Push to Github
    if pushToWebsite:
        gitCommitPush(webDir, comment)

    if pushToDevGit:
        gitCommitPush(workingDir, comment)



if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0rc2')
    main(arguments)