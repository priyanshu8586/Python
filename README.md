# Git aur GitHub: Repository banakar Code Upload karne ka Guide

Ye guide Termux (Android) ke liye hai. Step by step follow kijiye.

## Step 1: GitHub par Repository banao

1. GitHub kholo aur login karo.
2. **New repository** (+ icon) par click karo.
3. Repository ka naam daalo.
4. **Create repository** par click karo.
5. Apni repository ka link copy kar lo.

## Step 2: Terminal mein Git install karo

Termux kholo aur ye command chalao:

```bash
pkg install git -y
```

## Step 3: Project ko GitHub par push karo

Neeche ke commands ek-ek karke terminal mein paste karo:

```bash
# 1. Apne project folder mein jao
cd folder_name

# 2. Git shuru karo
git init

# 3. Saari files add karo
git add .

# 4. Apna naam aur email set karo
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# 5. Commit karo
git commit -m "Python"

# 6. Branch ka naam main karo
git branch -M main

# 7. Apni repository se connect karo
git remote add origin 'YOUR_REPOSITORY_LINK'

```

> `folder_name`, `Your Name`, `your@email.com` aur `YOUR_REPOSITORY_LINK` ko apni details se badal dena.

## Step 4: GitHub Token banao

Push karte waqt GitHub password nahi leta, token leta hai. Token ऐसे banao:

1. GitHub par **Generate new token** par click karo.
2. **Token name** daalo.
3. **Repository access** mein **Only select repositories** chuno, phir apni repo select karo.
4. **Permissions** mein jao: **Contents** chuno aur **Read and write** set karo.
5. Token generate karke **copy** kar lo.

## Step 5: Push karte waqt Login karo

```bash
git push -u origin main
```

- **Username:** apna GitHub username daalo.
- **Password:** copy kiya hua **Token** paste karo.

## Agar Error aaye

Agar push karte waqt error aaye, to use ignore karo aur ye command chalao:

```bash
git push -u origin main --force
```

> Dhyan rakho: `--force` GitHub par pehle se maujood data ko overwrite kar deta hai.

## Zaroori Baatein

- Apna token kisi ke saath share mat karo aur README mein mat likhna.
- Token kho jaye to naya token bana lo.
