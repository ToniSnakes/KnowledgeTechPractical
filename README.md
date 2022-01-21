# Test Chooser: A Knowledge System for the Recommendation of Statistical Tests
Late-night, a statistical task, but it’s been several years since the statistics
course; students and professionals with brittle statistical knowledge needed a
system that supports their choice of statistical tests. Therefore, we developed
TestChooser in the course Knowledge Technology Practical at the RuG, which suggests
statistical tests and models given a
type of data and a hypothesis. The need for such a system was experienced
first-hand but also by Megan Payne, the statistics expert that supported us in
this task.

By Amir Abdul Aziz , Antonio-Ionut Boar , and Joris Peters

Link: https://ktp-frontend.tonisworkshop.com

## Important files ##

The code for the backend is in `backend`

The relevant code for the frontend is in `frontend/components` and `frontend/pages`

## How to run ##

To run the backend on Ubuntu (you need python3):
```
cd backend/
sudo apt-get install python3.8-venv
python3 -m venv venv
. venv/bin/activate
pip3 install Flask
pip3 install flask-cors
export FLASK_APP=prototype
export FLASK_ENV=development
flask run
```

To run the backend on Windows Powershell (you need python3):
```
cd backend
python3 -m venv venv
.\venv\Scripts\activate
pip3 install Flask
pip3 install flask-cors
$env:FLASK_APP="prototype.py"
$env:FLASK_ENV="development"
flask run
```

This will install a package that you need to use the virtual environment, it activates it, and starts the backend on localhost:5000, with self-update whenever you save the script


To run the frontend (you need npm) on Ubuntu and Windows:

```
cd frontend/
npm install
npm run dev
```

This will install any missing dependencies and start the frontend on localhost:3000, with self-update when you update any of the files (I recommend VSCode to work with the code)


## How to access ##

Go to localhost:3000. The frontend will self-reload with changes made, and it will communicate with the backend to update its state