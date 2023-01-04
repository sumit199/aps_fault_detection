# neurolab-mongo-python

![image](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### Step 3 - git

```bash
git --version
```

### To download dataset
```
wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
```

### Git commands

If you are starting a project and you want to use git in your project

```
git init
```
Note: This is going to initalize git in your source code.

OR

You can clone exiting github repo
```bash
git clone <github_url>
```
Note: Clone/ Downlaod github repo in your system

Add your changes made in file to git stagging are
```bash
git add file_name
```
Note: You can given file_name to add specific file or use "." to add everything to staging are

### Create commits
```bash
git commit -m "message"
git push origin main
```
Note: origin--> contains url to your github repo main--> is your branch name

To push your changes forcefully.
```bash
git push origin main -f
```
To pull changes from github repo

```bash
git pull origin main
```
Note: origin--> contains url to your github repo main--> is your branch name

.env file has


```bash
MONGO_DB_URL="mongodb://localhost:27017"
AWS_ACCESS_KEY_ID="aagswdiquyawvdiu"
AWS_SECRET_ACCESS_KEY="sadoiuabnswodihabosdbn"
```

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

```
AWS_ACCESS_KEY_ID =
AWS_SECRET_ACCESS_KEY =
AWS_REGION =
AWS_ECR_LOGIN_URI =
ECR_REPOSITORY_NAME =
BUCKET_NAME =
MONGO_DB_URL =
```
