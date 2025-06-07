#!/bin/bash

# Output directories
mkdir -p ./en-US/LC_MESSAGES
mkdir -p ./ru-RU/LC_MESSAGES 
mkdir -p ./sr-Cyrl-RS/LC_MESSAGES 
mkdir -p ./sr-Latn-RS/LC_MESSAGES

# Initialize .po files
# msginit --locale=en-US --input=./about.pot --output=./en-US/LC_MESSAGES/about.po --no-translator
# msginit --locale=ru-RU --input=./about.pot --output=./ru-RU/LC_MESSAGES/about.po --no-translator
# msginit --locale=sr-Cyrl-RS --input=./about.pot --output=./sr-Cyrl-RS/LC_MESSAGES/about.po --no-translator
# msginit --locale=sr-Latn-RS --input=./about.pot --output=./sr-Latn-RS/LC_MESSAGES/about.po --no-translator

# msginit --locale=en-US --input=./app.pot --output=./en-US/LC_MESSAGES/app.po --no-translator
# msginit --locale=ru-RU --input=./app.pot --output=./ru-RU/LC_MESSAGES/app.po --no-translator
# msginit --locale=sr-Cyrl-RS --input=./app.pot --output=./sr-Cyrl-RS/LC_MESSAGES/app.po --no-translator
# msginit --locale=sr-Latn-RS --input=./app.pot --output=./sr-Latn-RS/LC_MESSAGES/app.po --no-translator

# msginit --locale=en-US --input=./main.pot --output=./en-US/LC_MESSAGES/main.po --no-translator
# msginit --locale=ru-RU --input=./main.pot --output=./ru-RU/LC_MESSAGES/main.po --no-translator
# msginit --locale=sr-Cyrl-RS --input=./main.pot --output=./sr-Cyrl-RS/LC_MESSAGES/main.po --no-translator
# msginit --locale=sr-Latn-eRS --input=./main.pot --output=./sr-Latn-RS/LC_MESSAGES/main.po --no-translator

# msginit --locale=en-US --input=./help.pot --output=./en-US/LC_MESSAGES/help.po --no-translator
# msginit --locale=ru-RU --input=./help.pot --output=./ru-RU/LC_MESSAGES/help.po --no-translator
# msginit --locale=sr-Cyrl-RS --input=./help.pot --output=./sr-Cyrl-RS/LC_MESSAGES/help.po --no-translator
# msginit --locale=sr-Latn-RS --input=./help.pot --output=./sr-Latn-RS/LC_MESSAGES/help.po --no-translator

# msginit --locale=en-US --input=./districts.pot --output=./en-US/LC_MESSAGES/districts.po --no-translator
# msginit --locale=ru-RU --input=./districts.pot --output=./ru-RU/LC_MESSAGES/districts.po --no-translator
# msginit --locale=sr-Cyrl-RS --input=./districts.pot --output=./sr-Cyrl-RS/LC_MESSAGES/districts.po --no-translator
# msginit --locale=sr-Latn-RS --input=./districts.pot --output=./sr-Latn-RS/LC_MESSAGES/districts.po --no-translator

# msginit --locale=en-US --input=./rooms.pot --output=./en-US/LC_MESSAGES/rooms.po --no-translator
# msginit --locale=ru-RU --input=./rooms.pot --output=./ru-RU/LC_MESSAGES/rooms.po --no-translator
# msginit --locale=sr-Cyrl-RS --input=./rooms.pot --output=./sr-Cyrl-RS/LC_MESSAGES/rooms.po --no-translator
# msginit --locale=sr-Latn-RS --input=./rooms.pot --output=./sr-Latn-RS/LC_MESSAGES/rooms.po --no-translator

msginit --locale=en-US --input=./trends.pot --output=./en-US/LC_MESSAGES/trends.po --no-translator
msginit --locale=ru-RU --input=./trends.pot --output=./ru-RU/LC_MESSAGES/trends.po --no-translator
msginit --locale=sr-Cyrl-RS --input=./trends.pot --output=./sr-Cyrl-RS/LC_MESSAGES/trends.po --no-translator
msginit --locale=sr-Latn-RS --input=./trends.pot --output=./sr-Latn-RS/LC_MESSAGES/trends.po --no-translator
