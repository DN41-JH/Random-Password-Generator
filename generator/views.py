from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.
def HomePage(request):
    HomePage_dict = {}
    return render(request, 'generator/homepage.html', HomePage_dict)

def pwSettings(request):
    pwSettings_dict = {}
    return render(request, 'generator/pw_settings.html', context = pwSettings_dict)

def getRandomPW(length, doUppercase, doNumber, doSpecial):
    characters_lower = []
    characters_upper = []
    numbers = []
    special_character = ['~','!','@','#','$','%','^','&','*','(',')','-','+','=']
    for i in range(26):
        characters_lower.append(chr(ord('a') + i))
        characters_upper.append(chr(ord('A') + i))
    for i in range(10):
        numbers.append(chr(ord('0') + i))

    characters = characters_lower
    if doUppercase:
        characters += characters_upper
    if doNumber:
        characters += numbers
    if doSpecial:
        characters += special_character

    randomPW = ""
    for i in range(length):
        randomPW += random.choice(characters)

    return randomPW

def Password(request):
    length = int(request.GET.get('pw_length'))  ### 'length' is from homepage.html, the name of the select input
    doUppercase = True if request.GET.get('doUppercase') is not None else False  ### 'Uppercase' is from homepage.html, the name of the Uppercase checkbox
    doNumber = True if request.GET.get('doNumbers') is not None else False  ### 'Numbers' is from homepage.html, the name of the Numbers checkbox
    doSpecial = True if request.GET.get('doSpecials') is not None else False  ### 'Special' is from homepage.html, the name of the Specials checkbox
    randomPW = getRandomPW(length, doUppercase, doNumber, doSpecial)

    Password_dict = {'password':randomPW}
    return render(request, 'generator/password.html', context = Password_dict)
