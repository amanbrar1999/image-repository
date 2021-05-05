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

## Endpoints

`GET /` healthcheck endpoint to ensure the application is running with a simple get request

`POST /add` adding an image path to the database. data must be of the form `{"path": "path/to/image"}`

`POST /delete` removing an image path from the database. data must be of the form `{"path": "path/to/image"}`

`GET /view` view all image paths in the database

`GET /view/images` view html page of all images in the database

## Testing

Unit and integration tests have been included in the `/tests` directory

## Future Improvements for Productionizing

As of now, file paths are stored in the database and the actual images are stored locally. A possible solution to make this better for a production environment is to store images in a cloud storage system such as AWS S3, and store the S3 file paths within the database instead of the current local filepaths.