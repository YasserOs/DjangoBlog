## Django Blog Project
Blog Created With Python Django
For Python Programming Course - ITI (Information Technology Institute) - Nasr City


## Supervised By:
 Eng. Mohamed Ramadan @mohamed-ramdan


## Contributers

# 1. Yasser Ossama 

# 2. Amr Ahmed

# 3. Mohamed Sambo

# 4. Mohamed Elgarhy

# 5  Mahmoud Shaaban

### what can users do

- Anyone can visit the blog without logging in and see the posts but can't like or comment on any of them.

* logged in normal user can view posts , comment on them , like or dislike

- logged in admin user can do crud operations on normal users , post and the other project parts except controlling other admins

* logged in super user can control anything in the blog even admins but can't control other super users

#### Users app handles all the following:

1. provide an easy and secure way to register new users.

2. handles users login , logout and authentication and check if user is registered but blocked and redirects him to another page tells him he is blocked and shall contact one of the admins listed for him and provide admins names and emails.

3. a blocked user cannot login but he is registered and still exist in users table for to be unblocked by admins any time they need.
