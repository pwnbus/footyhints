#!/bin/sh

set -e

# Get the highest tag number
VERSION=`git tag -l --sort=v:refname | tail -n1 | head -n1`

# Get number parts
MAJOR="${VERSION%%.*}"; VERSION="${VERSION#*.}"
MINOR="${VERSION%%.*}"; VERSION="${VERSION#*.}"
PATCH="${VERSION%%.*}"; VERSION="${VERSION#*.}"

# Increase version
PATCH=$((PATCH+1))

NEW_TAG="$MAJOR.$MINOR.$PATCH"

# Check to see if:
# 1. There are any local modifications
# 2. Local is not up to date with remote master
if [ -z "$(git diff origin/master)" ]; then
  continue
else
  echo "There are files either local or local is missing commits from remote...you need to manually fix"
  exit 1
fi

# Prompt user to create new tag
while true; do
    read -p "Tag to create: $NEW_TAG (y/n)? " answer
    case $answer in
        [Yy]* ) echo "Updating to $NEW_TAG"; git tag $NEW_TAG; git push origin $NEW_TAG; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
