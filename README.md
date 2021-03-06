# Tweeter
This is a mini-version of Twitter based on client-server TCP socket programming with relational MySQL database. The entire project is based on python with command line interface.

### Requirements and Dependencies
- MySQL Workbench
- Mininet (for testing)
- Python Libraries - MySQL connector, threading, regex, socket, getpass, mininet

### How to Run?
- Add your MySQL username and password in database_init.py and server.py. 
- Initialize the database using the command `python database_init.py`.
- Run `python server.py` in terminal.
- Run `python client.py` in terminal and follow the CLI. You can create multiple clients at one time as well.
- In order to test, run `python run_concurrent_clients.py`.
- If all the dependencies are satisfied and a successful database connection is made, the application should run smoothly.

### Features
- Login/ Register a user
- Obscure Password
- Search a user from registered users list
- Follow/ unfollow users
- Delete followers
- Display list of online followers and following
- Post tweets with hashtags
- Retweet a tweet
- Display trending hashtags
- Search tweets by hashtags
- 1v1 chat session
- News Feed home page
- Pin tweets for the user's home page

### Contributors
- <a href = "https://github.com/kavita-v"> Kavita Vaishnaw </a>
- <a href = "https://github.com/kanishkkalra11"> Kanishk Kalra </a>
- <a href = "https://github.com/mohitmina"> Mohit Mina </a>
