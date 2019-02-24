#!/bin/bash

MERGE_BRANCH="dev"
REPOSITORIES="home-assistant"

for repository in $REPOSITORIES
do
    cd $repository
    branches=$(git branch -r --no-merged)
    for branch in $branches
    do
        first_commit=$(git log --no-merges --reverse --date=iso --format="%ad" $branch ^$MERGE_BRANCH | head -1)
        last_author=$(git log --no-merges --format="%ae" $branch ^$MERGE_BRANCH | head -1)
        echo $repository,$branch,$last_author,$first_commit
    done
    cd ..
done