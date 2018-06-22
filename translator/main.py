# -*- encoding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

from WebService import *
from TranslationService import *

web = WebService("localhost", 8081)
web.start()

