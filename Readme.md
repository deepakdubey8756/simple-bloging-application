# roketrakoon a simple tech blog
A simple bloging website made using `django`, and other stacks..

# Features
It contains features like: 
1. Blogs sorted based on how recent it is publised.
2. Anonymous commenting feature so that anyone can comment on articles.

# Demo

To get a demo of it's woking check this  link...

![alt text](https://github.com/deepakdubey8756/simple-to-do/blob/main/asset/todo.png)

# Design
This document provides a high-level overview of this application.
## Overall working
It will display the lists of blogs when user will vist the blog. And it will show more details about the article when user will click on it.

## Models:
The following models will be created in the application:
1. `Post`: 
To store content details
2. `Comments`: 
To store  comments of a particular blog.

## Views
It contains following views
    1. `index`: to list all of the blog.
    2. `details`: To print all of the neccessary details of blog.
    3. `Store`: To store newly created blogs
    4. `addComment`: To add new comment to the blog.

## URLs:
The following URLs will be defined for each view:

### /
 The URL for the index page to display Notes.


### /edit/<note_id>
The URL for the Edit Note view, where <note_id> is the ID of the note to be edited.

### deleteNote/<id>
 The URL for the Delete Note view, where <id> is the ID of the note to be deleted.


### accounts/signup
This url will signup user

### accounts/login
This url will login user

### accounts/logout
to logout user

## Conclusion:
This design document outlines the basic structure of the note taking application that i have developed using Django. The application will allow users to create, view, edit, and delete notes. The models, views, templates, and URLs have been defined to provide a clear understanding of the functionalities that will be implemented in the application.
