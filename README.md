## Flask blog app

This is a flask blog app based on [this wonderful playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) by [Corey Shafer](https://www.youtube.com/user/schafer5).

I plan to watch the vidoes, create user stories and then try to code it on my own. 

### User Stories
- [x] I have a homepage which displays the posts, authors, date of when it was posted.
- [x] I have an access bar which has shortcuts.
- [x] I can create my account using my email id.
- [x] I can login using my email id with my password.
- [x] Once I login, I get a success (or failure message) before redirecting to homepage (or staying on the same page)
- [x] While logging in, if I fail to login, I see which field I entered wrong.
- [x] I can upload my display picture.
- [x] I can re-login and persist the data.
- [x] If I try accessing a webpage that requires me to login first, logging in will redirect me to the page I was trying to access.
- [x] I can create a new post.
- [x] I can update the posts that I had previously created (others should not be able to update my posts).
- [x] I can delete the post if I want to. 
- [ ] I see visually appealing error pages (like 404 and 403).
- [ ] The blog is secure with an SSL/TLS certificate

### System Features
- [x] Redirect the user back to his/her homepage once the post is deleted.
- [x] The profile picture is compressed to save memory.
- [x] If the user wants to edit his information (username, email or password), the previous information is pre-filled for the user.
- [x] Responsive layout that adapts to the size of the screen.
- [x] All users have a default profile picture which they can use (if they choose not to upload their picture).
- [x] User has to login to be able to access the accounts and page.

### How to run
- Open terminal with the home directory
- Install the dependencies from requirements.txt with:
```
pipenv install -r requirements.txt
```
- Run the flask server using
<!--
```
flask run
```
-->
```
python run.py
```

- Go to your browser and see the project on http://localhost:5000

#### Notes
- Using wtforms for making forms -> You can make forms from classes
