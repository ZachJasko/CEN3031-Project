# Swamp Services: Students Helping Students
Students are faced with all sorts of challenges these days that impede their ability to learn. Some of these challenges include needing help with food, pets, finances, and mental health. We are building a community service website that allows students to volunteer some of their time to help other students who may be facing some of these challenges. The volunteer students would provide quick services like developing meal plans, learning to cook, walking pets, talking when troubled, and helping with resumes and job searches.

###Project Description
Group 11's project was to create a student volunteer web application for the students of the University of Florida. Specifically, this project titled "Swamp Services" helps address the myriad of struggles that college students face during their college journey. The service was intended to be hosted by the University of Florida student government or other administrative organization as a way to provide a central place for students to earn service hours, engage in social activities, and help their community while earning gator points. By restricting account registration to only those who have a UF email, this service ensures safety and accountability for those who make use of it. This product differs from other service board websites like Craigslist by providing free help and a safer volunteer base.

###Challenge Statement and Solution
####Challenge
One common problem for college students, especially first year and first generation, is managing new challenges and environments. This can be stressful for many and harm their ability to learn and get the most out of their time at college. Some common challenges that college students might face include food insecurity, financial troubles, loneliness, time management, and dealing with illness/disability. 

####Solution
To help mitigate this problem, group 11 has created a student volunteer community website centered around helping their peers. College students are best able to help because they may have gone through similar problems and be able to emphasize and lend their experience. To create a realistic scope for our project, group 11 focused on the University of Florida community and tailored our website accordingly. Students will be able to earn volunteer hours and help their community by providing quick services such as creating meal plans, looking over resumes, taking students to the campus food bank, and teaching time management skills.


*NOTE* Please view the complete report in the main Github Repository (Project Report.pdf).

### Added Branch Protection Rules

<ins>Applies to 1 branch</ins>:  **main**

- Require a pull request before merging
    - Require approvals: 1
    - Dismiss stale pull request approvals when new commits are pushed

- Require status checks to pass before merging
    - Require branches to be up to date before merging

- Require conversation resolution before merging


### Project setup and running

0. python version: Python 3.12.1

1. Install postgresSQL:
    - On Windows: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
    -  On Mac, run this command in the terminal to install postgres: `brew install postgres`

2. Run following commands in the Windows:
- `pip install virtualenv`
- `python -m virtualenv <your_env_name>`
- `.\<your_env_name>\Scripts\activate`
- `pip install -r requirements.txt`
- `python manage.py makemigrations` 
- `python manage.py migrate`     
- `python manage.py runserver`
- Copy the *http://...* link in your browser and run.
- When done running. Close the environment: `deactivate`

3. Run following commands in the Mac:
- `pip3 install virtualenv`
- `python3 -m venv <your_env_name>`
- `source <your_env_name>/bin/activate`
- `pip3 install -r requirements.txt`
- `python3 manage.py makemigrations` 
- `python3 manage.py migrate`     
- `python3 manage.py runserver`
- Copy the *http://...* link in your browser and run.
- When done running. Close the environment: `deactivate`
