import requests, pymysql.cursors, string
from bs4 import BeautifulSoup
from nltk import word_tokenize

class Scraper:

	def __init__(self):
		indonesian_words_unique_token = []
		indonesian_words_token = word_tokenize(self.__get_indonesian_words())
		for word in indonesian_words_token:
			if word not in indonesian_words_unique_token:
				indonesian_words_unique_token.append(word)
		
		print(len(indonesian_words_token))
		print(len(indonesian_words_unique_token))
		print(indonesian_words_unique_token)

	def __get_indonesian_words(self):
		conn_kamus = pymysql.connect(
			host='localhost',
			user='root',
			password='',
			db='kamus',
			charset='utf8mb4',
			cursorclass=pymysql.cursors.DictCursor)


		indonesian_words = ""	

		try:
			with conn_kamus.cursor() as cursor:
				# Read a single record
				sql = """
					SELECT s.song_lyric
					FROM musiklib.song s 
					INNER JOIN musiklib.artist t
					ON s.song_artist_id = t.artist_id
					WHERE t.artist_country_id = 1
					AND s.song_lyric NOT LIKE %s
					LIMIT 1000
				"""
				cursor.execute(sql, ('%you%',))
				result = cursor.fetchall()
				for lyric in result:
					indonesian_words += lyric['song_lyric']
					indonesian_words += " "
				
		finally:
			conn_kamus.close()

		indonesian_words = indonesian_words.replace('<br>', ' ').lower()
		indonesian_words = indonesian_words.replace('.', ' ').lower()
		
		return indonesian_words