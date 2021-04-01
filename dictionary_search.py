"""
Assignment 2:
Write a python class that is able to return the meaning of an English language word provided to it
in the terminal. (Use https://dictionaryapi.dev/)
Expected output:
$ python -m dictionary_search.py
> Word? <user inputs a word>(Ex – “House”)
> House. Noun. A building for human habitation, especially one that is lived in by a family or
small group of people.
"""
import requests

def dictionary_search(word):
	response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/'+word)
	data = response.json()
	for i in range(len(data[0]['meanings'])):
		print(data[0]['meanings'][i]['partOfSpeech'].capitalize(),end=". ")
		print(data[0]['meanings'][i]['definitions'][0]['definition'])

word = input('Word? ')
print(word.capitalize())
dictionary_search(word)