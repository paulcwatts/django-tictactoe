=====================
Tic-Tac-Toe in Django
=====================

.. image:: https://travis-ci.org/paulcwatts/django-tictactoe.png?branch=master
   :target: https://travis-ci.org/paulcwatts/django-tictactoe

For people new to Django (or to programming in general) I tend to give people a challenge
to write a tic-tac-toe game. This is my solution.

It's not only a working tic-tac-toe game, but it also includes many standard patterns
used by Django apps such as unit testing models and views, importing modules, and testing
with tox_ and Travis_.

Building
--------

The easiest way to get this set up is to use virtualenv_. Usually it's easy as::

    sudo pip install virtualenv
    
Once you have virtualenv and the code, you can create a virtualenv and install the dependencies::

    cd <path_to_code>
    mkvirtualenv tictactoe
    pip install -r requirements.txt
    
Then run the server::

    python manage.py runserver
    
Design
------

The game state is stored in the Game model. The board is stored as a 9 character string, 
with the option of having multiple player types::

    class Game(models.Model):
        board = models.CharField(max_length=9, default=" " * 9)

        player_x = models.CharField(max_length=64)
        player_o = models.CharField(max_length=64)

You can see the rest of the logic of the same by checking out the models file: https://github.com/paulcwatts/django-tictactoe/blob/master/game/models.py

Each player is stored as a string which can either be "human" or the name of a class that 
implements the player logic. Player logic is separated out into classes of their own to 
maintain a good separation of roles. Right now there's only a player that plays randomly, 
but the intent is to create a new player that plays perfectly.

The UI for the game is fairly simplistic, and relies entirely on Django templates and views. 
It's not actually the way I would write it -- I'd create a front-end Javascript solution and 
use a JSON API to send and receive moves.

Testing
-------

All of the code is tested, which is a good primer if you're new to testing Django applications: https://github.com/paulcwatts/django-tictactoe/tree/master/game/tests
If you're unfamiliar with many of the testing tools available to Django apps, I have 
slides and code from a talk I did on `testing Django <https://github.com/paulcwatts/codefellows-django-testing>`_). 

Future
------

Eventually I'd like to create a real Javascript front-end and API. But for now this was specifically about
Django development.


.. _Travis: https://travis-ci.org/
.. _tox: http://tox.readthedocs.org/en/latest/
.. _virtualenv: http://www.virtualenv.org/en/latest/
