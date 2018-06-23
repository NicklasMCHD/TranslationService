# -*- encoding: utf-8 -*-
import requests, requests_cache, json, sys, os
sys.dont_write_bytecode = True

class TranslationService(object):
	def __init__(self, cache_path):
		self.cache_path = cache_path
		requests_cache.install_cache(os.path.join(self.cache_path, "translation.cache"), backend='sqlite')

	def translate(self, text, target_language):
		return self.translate_specified(text, "auto", target_language)

	def translate_specified(self, text, from_language, target_language):
		r = requests.get('http://localhost:8081/?text=' + text + '&from=' + from_language + '&target=' + target_language)
		print r.content
		return r.content
