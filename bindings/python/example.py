import TranslationService, json

service = TranslationService.TranslationService("")
print json.loads(service.translate("", "da"))
