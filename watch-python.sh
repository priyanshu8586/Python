#!/data/data/com.termux/files/usr/bin/bash

cd "$HOME/python" || exit 1

# Check Git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "ERROR: Git repository not found!"
    exit 1
fi

# Check branch
if [ "$(git branch --show-current)" != "main" ]; then
    echo "ERROR: Please switch to main branch first."
    exit 1
fi

# Prevent running during an existing rebase
if [ -d "$(git rev-parse --git-path rebase-merge)" ] || \
   [ -d "$(git rev-parse --git-path rebase-apply)" ]; then
    echo "ERROR: An existing rebase needs attention."
    exit 1
fi

echo "================================"
echo "  PYTHON AUTO GITHUB UPLOADER"
echo "================================"
echo "Watching: $HOME/python"
echo "Branch: main"
echo "Press CTRL+C to stop."

inotifywait -m -r \
-e close_write,create,delete,moved_to,moved_from \
--exclude '(^|/)\.git(/|$)|(^|/)(__pycache__|\.venv|venv)(/|$)|\.pyc$' \
--format '%w%f' . |
while IFS= read -r file
do
    # Ignore Git internal files
    case "$file" in
        ./.git/*|./.git)
            continue
            ;;
    esac

    echo ""
    echo "Change detected: $file"

    # Allow multiple quick edits to settle
    sleep 3

    # Stage project changes
    git add -A

    if git diff --cached --quiet; then
        echo "No changes to commit."
        continue
    fi

    # Commit changes
    if ! git commit -m "Added python "; then
        echo "ERROR: Commit failed!"
        continue
    fi

    # Fetch latest GitHub changes
    if ! git fetch origin main; then
        echo "ERROR: GitHub fetch failed!"
        continue
    fi

    # Integrate remote changes
    if ! git rebase origin/main; then
        echo "ERROR: Rebase failed. Manual conflict check required."
        git rebase --abort
        continue
    fi

    # Push to GitHub
    if git push origin main; then
        echo "================================"
        echo "SUCCESS: GitHub updated!"
        echo "================================"
    else
        echo "ERROR: Push failed!"
    fi
done
