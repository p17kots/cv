#!/bin/sh

setup_git() {
  git config --global user.email "p17kots@ionio.gr"
  git config --global user.name "p17kots"
}

commit_website_files() {
  git checkout -b main
  git add . cv.pdf
  git commit --message "Updating pdf format: $TRAVIS_BUILD_NUMBER "
}

upload_files() {
  git remote add origin-pages https://${GH_TOKEN}@github.com/p17kots/cv.git > /dev/null 2>&1
  git push --quiet --set-upstream origin main 
}

setup_git
commit_website_files
upload_files
