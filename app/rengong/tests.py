from django.test import TestCase
import os

from kefu.settings import BASE_DIR

# Create your tests here.

print( os.path.join(BASE_DIR, "static"),)