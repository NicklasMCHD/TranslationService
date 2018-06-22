# -*- encoding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

from TranslationService import *
import BaseHTTPServer, threading, urlparse

# The type of messages.
EMPTY_REQUEST = '["status":"error", "message":"No parameters supplied", "code":1001]'
TARGET_LANGUAGE_NOT_SPECIFIED = '["status":"error","message":"Target language not specified.", "code":1002]'
NO_TEXT_SENT = '["status":"error","message":"No text sent for translation.","code":1003]'
INVALID_PROVIDER = '["status":"error","message":"Invalid translation provider","code":1004]'

valid_providers = {'yandex'}

class TranslationRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(s):
		s.send_response(200)
		s.send_header("Content-type", "text/json")
		s.end_headers()
		raw_request = line = s.path.translate(None, '?/')
		if raw_request == "":
			s.wfile.write(EMPTY_REQUEST)
			return
		request_dict = urlparse.parse_qsl(raw_request)
		request = dict(request_dict)
		if "target" not in request:
			s.wfile.write(TARGET_LANGUAGE_NOT_SPECIFIED)
			return
		target_language = request["target"]
		if "text" not in request:
			s.wfile.write(NO_TEXT_SENT)
			return
		text = request["text"]
		from_language = "auto"
		if "from" in request:
			from_language = request["from"]
		provider = "yandex"
		if "provider" in request:
			if request["provider"] in valid_providers:
				provider = request["provider"]
		translate_now(s, unicode(text[0:500], "utf-8"), from_language, target_language, provider)
		return


class WebService(threading.Thread):
	def __init__(self, host, port):
		threading.Thread.__init__(self)
		self.host = host
		self.port = port
		self.web = BaseHTTPServer.HTTPServer
		self.httpd = self.web((self.host, self.port), TranslationRequestHandler)

	def run(self):
		try:
			self.httpd.serve_forever()
		except KeyboardInterrupt:
			pass
			self.httpd.server_close()
			# close everything here
			sys.exit()
