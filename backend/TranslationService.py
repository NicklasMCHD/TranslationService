# -*- encoding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

# translation services.
from yandex_translate import YandexTranslate
import googletrans

yandex = YandexTranslate("trnsl.1.1.20180130T151809Z.8c280d79de9f5411.9b57bc3a583bc2894bc5de61b0a653c6fee98a1c")
google = googletrans.Translator()

# translation function
def translate_now(s, raw_text, from_language, target_language, provider):
	if provider == "google":
		if from_language == "auto":
			result = google.translate(raw_text, dest=target_language)
			write_result(s, raw_text, result.text, provider)
			return
		else:
			result = google.translate(raw_text, src=from_language, dest=target_language)
			write_result(s, raw_text, result.text, provider)
			return
	if provider == "yandex":
		if from_language == "auto":
			result = yandex.translate(raw_text, target_language)['text']
			translation = result[0]
			write_result(s, raw_text, translation, provider)
			return
		else:
			result = yandex.translate(raw_text, from_language+"-"+target_language)['text']
			translation = result[0]
			write_result(s, raw_text, translation, provider)
			return

def write_result(s, raw_text, translated_text, provider):
	s.wfile.write('{"status":"success", "original":"'+raw_text+'", "translation":"'+translated_text+'", "provider":"'+provider+'"}')
