import requests, pymysql.cursors, string, re, pickle
from bs4 import BeautifulSoup
from nltk import word_tokenize

class Scraper:

	def __init__(self):
		indonesian_words_unique_token = []
		PIK = "indonesian_words_unique_token.pickle"
		with open(PIK, "rb") as f:
			indonesian_words_unique_token = pickle.load(f)

		print(indonesian_words_unique_token)
		
	