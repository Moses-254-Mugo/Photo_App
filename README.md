# M-Instagram
## Contributors
Feel free to comment, critique or even submit a pull request.

## Author
Mugo Moses

## Description
M-Instagram is a web app that allows users to sign in the application, upload images, see profile pictures, follow others and also see their pictures and like picutes and leave comment on it.

## Screenshots
<img src="" alt="">
<img src="" alt="">
<img src="" alt="">

## Setup and Installation
### Requirements
1. Clone the repository by running

        ghttps://github.com/Moses-254-Mugo/Photo_App
    Navigate to the project

        cd Photo_App
 2. Create a virtual enviroment

         pip install virtualenv 

    To activate the created virtual environment, run

        source virtual/bin/activate
3. Create database
    You will need to create a new postgress database by typing the following command to access postgress

        $ psql

    Then run below query to create a new database named 

        # create databases instaphotos;
5. Create Database migrations
    make migrations on postgres using django

        python3.8 manage.py makemigrations garage instaphotos
    then run the below command.

        python3.8 manage.py migrate

6. Run the app
    To run the application on your development machine,

        pythong3.8 manage.py runserver
### Running Tests
To run tests;

        python3.8 manage.py test


## Technologies Used
* Python3.8
* Django
* HTML
* Bootstrap
* CSS

## User Stories
1. Sign in to the application to start using.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline
5. Like a picture and leave a comment on it. 

## Support and contact details
If you have any questions, want to contribute to the code? Please email at
moseskinyua12@gmail.com

## License
The project is under[MIT License](LICENSE).