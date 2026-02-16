## Data Platform LAB 1

### Step by step
1. Create and clone repo:
    - ### CREATE
      1. Create repo in GitHub 
      2. In git: 
        - git init
        - git add README.md
        - git commit -m "first commit"
        - git branch -M main
        - git remote add origin git@github.com:LisaYllander92/Data_Platform_LAB1.git
        - git push -u origin main
    - ### CLONE 
      1. Clone repo in GitHub
      2. In git:
         - git clone git@github.com:LisaYllander92/Data_Platform_LAB1.git
         - git pull origin main 
      
NOTE: Add collaborators to repo in GitHub to work together 
   
### Create new branch 
- In terminal git checkout -b <branchname>
- git checkout <branchname> --> to switch branch

### Ingest data from csv-file
1. df = pd.read_csv("products.csv")
