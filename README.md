# Image Repository

## Setup
In order to run this project, clone this repo

```
$ git clone git@github.com:amanbrar1999/image-repository.git
$ cd image-repository
```

Requirements can be installed using the requirements.txt file. You may want to set up a virtual environment to do so

```
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```

Now, you can initialize the database and run the app with:

```
$ export FLASK_APP=image_repo
$ export FLASK_ENV=development
$ flask init-db
$ flask run
```

## Functionality

This application currently supports the following functionality:

- Adding image to database
- Removing image from database
- Viewing images in database