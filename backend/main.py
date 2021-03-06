# -*- encoding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

from WebService import *
from TranslationService import *
import requests_cache

print("Setting up cache")
requests_cache.install_cache('translation.cache', backend='sqlite')
web = WebService("0.0.0.0", 11000)
web.start()
