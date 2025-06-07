#!/bin/bash

# Compile .po to .mo
msgfmt ./en-US/LC_MESSAGES/about.po -o ./en-US/LC_MESSAGES/about.mo
msgfmt ./ru-RU/LC_MESSAGES/about.po -o ./ru-RU/LC_MESSAGES/about.mo
msgfmt ./sr-Cyrl-RS/LC_MESSAGES/about.po -o ./sr-Cyrl-RS/LC_MESSAGES/about.mo
msgfmt ./sr-Latn-RS/LC_MESSAGES/about.po -o ./sr-Latn-RS/LC_MESSAGES/about.mo

msgfmt ./en-US/LC_MESSAGES/app.po -o ./en-US/LC_MESSAGES/app.mo
msgfmt ./ru-RU/LC_MESSAGES/app.po -o ./ru-RU/LC_MESSAGES/app.mo
msgfmt ./sr-Cyrl-RS/LC_MESSAGES/app.po -o ./sr-Cyrl-RS/LC_MESSAGES/app.mo
msgfmt ./sr-Latn-RS/LC_MESSAGES/app.po -o ./sr-Latn-RS/LC_MESSAGES/app.mo

msgfmt ./en-US/LC_MESSAGES/main.po -o ./en-US/LC_MESSAGES/main.mo
msgfmt ./ru-RU/LC_MESSAGES/main.po -o ./ru-RU/LC_MESSAGES/main.mo
msgfmt ./sr-Cyrl-RS/LC_MESSAGES/main.po -o ./sr-Cyrl-RS/LC_MESSAGES/main.mo
msgfmt ./sr-Latn-RS/LC_MESSAGES/main.po -o ./sr-Latn-RS/LC_MESSAGES/main.mo

msgfmt ./en-US/LC_MESSAGES/help.po -o ./en-US/LC_MESSAGES/help.mo
msgfmt ./ru-RU/LC_MESSAGES/help.po -o ./ru-RU/LC_MESSAGES/help.mo
msgfmt ./sr-Cyrl-RS/LC_MESSAGES/help.po -o ./sr-Cyrl-RS/LC_MESSAGES/help.mo
msgfmt ./sr-Latn-RS/LC_MESSAGES/help.po -o ./sr-Latn-RS/LC_MESSAGES/help.mo

msgfmt ./en-US/LC_MESSAGES/districts.po -o ./en-US/LC_MESSAGES/districts.mo
msgfmt ./ru-RU/LC_MESSAGES/districts.po -o ./ru-RU/LC_MESSAGES/districts.mo
msgfmt ./sr-Cyrl-RS/LC_MESSAGES/districts.po -o ./sr-Cyrl-RS/LC_MESSAGES/districts.mo
msgfmt ./sr-Latn-RS/LC_MESSAGES/districts.po -o ./sr-Latn-RS/LC_MESSAGES/districts.mo

msgfmt ./en-US/LC_MESSAGES/rooms.po -o ./en-US/LC_MESSAGES/rooms.mo
msgfmt ./ru-RU/LC_MESSAGES/rooms.po -o ./ru-RU/LC_MESSAGES/rooms.mo
msgfmt ./sr-Cyrl-RS/LC_MESSAGES/rooms.po -o ./sr-Cyrl-RS/LC_MESSAGES/rooms.mo
msgfmt ./sr-Latn-RS/LC_MESSAGES/rooms.po -o ./sr-Latn-RS/LC_MESSAGES/rooms.mo

msgfmt ./en-US/LC_MESSAGES/trends.po -o ./en-US/LC_MESSAGES/trends.mo
msgfmt ./ru-RU/LC_MESSAGES/trends.po -o ./ru-RU/LC_MESSAGES/trends.mo
msgfmt ./sr-Cyrl-RS/LC_MESSAGES/trends.po -o ./sr-Cyrl-RS/LC_MESSAGES/trends.mo
msgfmt ./sr-Latn-RS/LC_MESSAGES/trends.po -o ./sr-Latn-RS/LC_MESSAGES/trends.mo
