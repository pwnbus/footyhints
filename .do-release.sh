#!/bin/sh

# Get the highest tag number
VERSION=`git tag -l --sort=v:refname | tail -n1 | head -n1`

# Get number parts
MAJOR="${VERSION%%.*}"; VERSION="${VERSION#*.}"
MINOR="${VERSION%%.*}"; VERSION="${VERSION#*.}"
PATCH="${VERSION%%.*}"; VERSION="${VERSION#*.}"

# Increase version
PATCH=$((PATCH+1))

# Create new tag
NEW_TAG="$MAJOR.$MINOR.$PATCH"
echo "Updating to $NEW_TAG"
git tag $NEW_TAG
git push origin $NEW_TAG
