
#!/data/data/com.termux/files/usr/bin/bash

# =========================================
#       CONFIGURATION SECTION
# =========================================

GITHUB_USERNAME="priyanshu8586"
REPO_DIR="$HOME/Python"
BRANCH="main"
COMMIT_MESSAGE="Added python"

# =========================================
#       END CONFIGURATION
# =========================================

cd "$REPO_DIR" || {
    echo "ERROR: Python directory not found!"
    exit 1
}

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "ERROR: Git repository not found!"
    exit 1
fi

if [ "$(git branch --show-current)" != "$BRANCH" ]; then
    echo "ERROR: Switch to main branch first!"
    exit 1
fi

if [ -d "$(git rev-parse --git-path rebase-merge)" ] || \
   [ -d "$(git rev-parse --git-path rebase-apply)" ]; then
    echo "ERROR: Existing rebase detected!"
    exit 1
fi

echo "================================"
echo " PYTHON AUTO GITHUB UPLOADER"
echo "================================"
echo "Username: $GITHUB_USERNAME"
echo "Repository: $REPO_DIR"
echo "Branch: $BRANCH"
echo "Authentication: SSH"
echo "Press CTRL+C to stop."

inotifywait -m -r \
-e close_write,create,delete,moved_to,moved_from \
--exclude '(^|/)\.git(/|$)|(^|/)(__pycache__|\.venv|venv)(/|$)|\.pyc$' \
--format '%w%f' . |

while IFS= read -r file
do

    echo ""
    echo "Change detected: $file"

    sleep 3

    git add -A

    if git diff --cached --quiet; then
        echo "No changes to commit."
        continue
    fi

    if ! git commit -m "$COMMIT_MESSAGE"; then
        echo "ERROR: Commit failed!"
        continue
    fi

    if ! git fetch origin "$BRANCH"; then
        echo "ERROR: Fetch failed!"
        continue
    fi

    if ! git rebase "origin/$BRANCH"; then
        echo "ERROR: Rebase failed!"
        git rebase --abort
        continue
    fi

    if git push origin "$BRANCH"; then
        echo "================================"
        echo "SUCCESS: GitHub updated!"
        echo "================================"
    else
        echo "ERROR: Push failed!"
    fi

done


