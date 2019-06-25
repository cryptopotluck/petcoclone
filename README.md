#Petco Project
This project was built as a example project in two days to show off my programing capabilities as a backend developer.

##What is this project?

This is a full stack pet funding social media app that would be hosted on the cloud. You can upload your pets & let other people get to know them. Donate to posts based on different criteria ranging from birthday to medical needs & any other reason you can think of.

Structure of Project
-
- Account
    1. Login
    2. Logout
    3. Register Page
    4. Profile Page
        1. Rich Text Editor About Page Form
        2. Add Facebook link Form
        3. Add Twitter Link Form
        4. Add Instagram Link Form
        5. Filter Database for all your pets
        6. Paginator
- Home
    1. Presentation Page
    2. About Page
- Create Pet
    1. Add a New Pet
        1. Pet Name Form
        2. Pet Type Form
        3. Pet Bread Form
        4. Birthdat Form
        5. Pet Profile Pic Form
        6. Rich Text Editor Pet About Page
    2. Update Pet
        1. Pet Name Form
        2. Pet Type Form
        3. Pet Bread Form
        4. Birthdat Form
        5. Pet Profile Pic Form
        6. Rich Text Editor Pet About Page
    3. Pet Detail View
        1. Filters Database & Shows All Pet's Posts
        2. Filters Database & Shows All Pet's Info
    4. Pet Delete View
        1. Gives a warning before deleting a pet
        2. Deletes the Pet from the database
        3. Deletes all of Pets posts
- Pets Post's
    1. Create Post
        1. Lets you select a pet you own
        2. Name the title of Post Form
        3. Monetization Form
        4. Type of Post
        5. Rich Text Editor Body Form
        6. Funding Goal
    2. Update Post
        1. Lets you select a pet you own
        2. Name the title of Post Form
        3. Monetization Form
        4. Type of Post
        5. Rich Text Editor Body Form
        6. Funding Goal
    3. Post Detail
        1. Creates a Detail page of the post for viewing
        2. Filters Database for Post Information
        3. Filters Database for Account Information
        4. Filters Database for Pets Information
        5. Donate Form
        7. Displays all comments on post
        6. Comment Post Form
    4. Post Delete
        1. Deletes Post
    5. Pet Social
        1. Filters database for all Posts and displays them
        2. Filter Based on Birthday
        3. Filter Based on Medical
        4. Filter Based on In memory of
        5. Filter Based on Fun
- Account Goal Graph
    1. Work in progress haven't started will Build rich interactive graphs with plotly & Dash
        
       
        
-
#How to Run Project
This project is built with python 3.7 once you download the project on your local machine create and setup a virtual env. Open terminal of project & run ``pip3 install -r requirements.txt`` Create a postgres database & set it up in the settings.py file. Run migrations & you should be good to go.

#Pictures of Project
![Image description](link-to-image)