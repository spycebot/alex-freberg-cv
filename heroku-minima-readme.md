F:\01 - Python\flash\heroku-minima> heroku login

F:\01 - Python\flash\heroku-minima> git init 

F:\01 - Python\flash\heroku-minima> git add .

F:\01 - Python\flash\heroku-minima> git commit -am "Initialise app"

F:\01 - Python\flash\free-code-camp> heroku apps:create heroku-minima

Creating heroku-minima... done
https://heroku-minima-506369e31bc7.herokuapp.com | https://git.heroku.com/heroku-minima.git

F:\01 - Python\flash\free-code-camp> heroku help

----------

PS F:\01 - Python\heroku\heroku-minima> git push heroku main
error: src refspec main does not match any
error: failed to push some refs to 'https://git.heroku.com/heroku-minima.git'
PS F:\01 - Python\heroku\heroku-minima> git remote -v
heroku  https://git.heroku.com/heroku-minima.git (fetch)
heroku  https://git.heroku.com/heroku-minima.git (push)
PS F:\01 - Python\heroku\heroku-minima> git push heroku mai 
error: src refspec mai does not match any
error: failed to push some refs to 'https://git.heroku.com/heroku-minima.git'
PS F:\01 - Python\heroku\heroku-minima> git push heroku master
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.

https://help.heroku.com/O0EXQZTA/how-do-i-switch-branches-from-master-to-main

==========

# 11 MAY 2024

The template site courtesy of Dan Bevens has been successfully launched on www.terzotechnical.com
using Heroku and of course Flask. 

What this site, at this point in time, does not have, that dan-blevens-flask does have

1. app.py / main.py
2. index.html that is populated
3. index.html as template for app.py

## Steps

1. Create app.py file at top level / and populate script contents.

2. Activate development environment

PS F:\01 - Python\heroku\heroku-minima> .venv\Scripts\activate

3. Upgrade pip

(.venv) PS F:\01 - Python\heroku\heroku-minima> python -m pip install --upgrade pip

4. Install Flask

(.venv) PS F:\01 - Python\heroku\heroku-minima> python -m install Flask

NB: There is a project folder heroku-minima as well as a project folder flask-minima

==========

### MON 20 JAN 2025

Heroku-minima > alex-freberg-cv

1. Heroku Endpoint
2. Git Endpoint
3. Virtual Environment

(.venv) PS C:\Projects\alex-freberg-cv\heroku-minima> git add .
(.venv) PS C:\Projects\alex-freberg-cv\heroku-minima> git commit -m "Repurpose heroku-minima for alex-freberg-cv"
[master 716d72e] Repurpose heroku-minima for alex-freberg-cv
 4 files changed, 28 insertions(+), 15 deletions(-)
 rewrite templates/index.html (90%)
(.venv) PS C:\Projects\alex-freberg-cv\heroku-minima> heroku create alex-freberg-cv
>> 
Creating ⬢ alex-freberg-cv... done
https://alex-freberg-cv-204da870b90b.herokuapp.com/ | https://git.heroku.com/alex-freberg-cv.git
(.venv) PS C:\Projects\alex-freberg-cv\heroku-minima> 

## GIT BASH

photi@TERZO-SECUNDUS MINGW64 /c/Projects/alex-freberg-cv/heroku-minima (master)
$ git remote add spycebot https://github.com/spycebot/alex-freberg-cv.git

photi@TERZO-SECUNDUS MINGW64 /c/Projects/alex-freberg-cv/heroku-minima (master)
$

## VSCode extension: GitHub Pull Requests Extension

(.venv) PS C:\Projects\alex-freberg-cv\heroku-minima> git push spycebot master