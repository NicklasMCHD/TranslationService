# Translation Service API spec
Here you'll find the api spec for the Translation Service.
This is the page you need to look at, if you want to create a binding for another language.

### Requirements
To be accepted as a binding, the binding needs the following features.
* A local cache, to keep responses from the api in, to look in before sending a request to the Translation Service API.
* Be able to handle all the api responses in a language native way.

### The flow of a binding
A binding should have the following flow:
* Something needs translated
* Binding gets the request from somewhere else in the application.
* Binding checks in the cache for a request looking like the one it just got (checking with text to translate, targeted language).
* If a result in the local cache is found with the translated text and targeted text, it should return that and go no further.
* If no result is found in the local cache it should make a request to the api.
* On success, it should store the result in the local cache for future use.
* On error it should check the 4 digit error code and raise an exception or what ever else is normally done in that language.

### Requirements for the local cache
The cache need to save the successful responses from the api. From the response it should save the following (at least):
* Original text.
* Targeted language.
* Translated text.

### Possible API Responses
Note: All responses are returned in the json format.
The api responses can be divided into 2 groups. The errors and the success.
All the api responses has some fields in common:
* status: Wich can be either "success" or "error".
The error responses have the following fields.
* message. A string describing what went wrong.
* Code: (int) a 4 digit code from the api (wich should be used in the binding to determine the cause of the error).
On success the response have the following fields:
* status: "success"
* original: a field holding the text sent to translation.
* translation: A field holding the translated text.

### Error Codes
Following error codes are returned from the api.
* 1001: No parameters supplied.
* 1002: No target language sent.
* 1003: No text sent.
* 1004: Sent text exceeded the character limit
* 1005: Invalid translation provider