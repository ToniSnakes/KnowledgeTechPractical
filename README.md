# KnowledgeTechPractical

To run the backend (you need python3):

```
cd backend/
sudo apt-get install python3.8-venv
. venv/bin/activate
export FLASK_APP=hello
export FLASK_EVN=development
flask run
```

This will install a package that you need to use the virtual environment, it activates it (which should have all of the python packages you need to run the script, if it doesn't let me know) and then it starts the backend on localhost:5000, with self-update whenever you save the script


To run the frontend (you need npm):

```
cd frontend/hello/
npm install
npm run dev
```

This will install any missing dependencies and start the frontend on localhost:3000, with self-update when you update any of the files (I recommend VSCode to work with the code)


## How to access ##

Go to localhost:3000. The frontend will self-reload with changes made, and it will communicate with the backend to update its state
