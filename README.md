# Swamp Services: Students Helping Students
Students are faced with all sorts of challenges these days that impede their ability to learn. Some of these challenges include needing help with food, pets, finances, and mental health. We are building a community service website that allows students to volunteer some of their time to help other students who may be facing some of these challenges. The volunteer students would provide quick services like developing meal plans, learning to cook, walking pets, talking when troubled, and helping with resumes and job searches.

**FOR** (target customer) - This product is for students on the UF campus who need help.<br />
**WHO** (statement of the need or opportunity) - It fulfills the needs of students for a safe, reliable, free service on the UF campus. <br />
The (*PRODUCT NAME*) is a (*PRODUCT CATEGORY*) - Swamp Services which provides free student help. <br />
**THAT** (key benefit, compelling reason to buy) - The University of Florida would be interested in licensing this product and giving students access to use this app to strengthen their community. The appeal to students would be the ability to earn Gator Points, which are redeemable in campus stores, while gaining community service hours and building a sociable community through outreach and response facilitated by the website. <br />
**UNLIKE** (primary competitive alternative) - Unlike craigslist, Swamp Services provides a free, safe alternative to existing service marketplaces. <br />
**OUR PRODUCT** (statement of primary differentiation) - Our product differs from competitors because it is solely based on the UF campus and is made for the students who are verified. Our site provides volunteer/social opportunities to UF students.<br />

Because Swamp Services needs UFID to access, if any crime or harassment occurs, the culprit will be easy to identify. The UFID access also excludes non-students from accessing the services and should provide a measure of safety.

### Added Branch Protection Rules

<ins>Applies to 1 branch</ins>:  **main**

- Require a pull request before merging
    - Require approvals: 1
    - Dismiss stale pull request approvals when new commits are pushed

- Require status checks to pass before merging
    - Require branches to be up to date before merging

- Require conversation resolution before merging


### Project setup and running

1. Install postgresSQL:
    - On Windows: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
    -  On Mac, run this command in the terminal to install postgres: `brew install postgres`
2. Run following commands in the Windows:
- `pip install virtualenv`
- `python -m virtualenv <your_env_name>`
- `.\<your_env_name>\Scripts\activate`
- `pip install -r requirements.txt`
- `python manage.py runserver`
- Copy the *http://...* link in your browser and run.
- When done running. Close the environment: `deactivate`

3. Run following commands in the Windows:
- `python3 -m venv <your_env_name>`
- `source ./<your_env_name>/Scripts/activate`
- `pip install -r requirements.txt`
- `python manage.py runserver`
- Copy the *http://...* link in your browser and run.
- When done running. Close the environment: `deactivate`
