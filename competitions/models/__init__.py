# https://docs.djangoproject.com/en/3.2/topics/db/models/#organizing-models-in-a-package
# the order of import matters, import the foreign key classes first

from .Level import Level
from .Group import Group
from .Type import Type
from .Interclub import *
from .Game import Game
