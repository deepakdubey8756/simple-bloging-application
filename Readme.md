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
 The URL for the index page to list all of the blogs.

### /details/<slug:slug>
The URL to display blog details.

## Conclusion:
This design document outlines the basic structure of the bloging application that i have developed using Django. I am using it personly to write blogs. Your can read it here: `url`