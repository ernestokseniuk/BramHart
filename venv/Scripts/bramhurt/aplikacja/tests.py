from django.test import TestCase
import pyperclip
text = ""
for i in range(9000):
    text += str(i+1) +". PLAYBOY \n"

pyperclip.copy(text)
# Create your tests here.
