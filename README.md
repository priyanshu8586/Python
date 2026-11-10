# Python


cd ~/Python1

git config --global user.name "priyanshu8586"

git remote set-url origin https://github.com/priyanshu8586/Python.git

git branch -M main

git add .

if ! git diff --cached --quiet; then
    git commit -m "Upload Python project"
fi

git pull --no-rebase --allow-unrelated-histories --no-edit origin main

git push -u origin main
