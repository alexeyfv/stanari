#!/bin/bash

# Metadata
PACKAGE_NAME="stanari"
PACKAGE_VERSION="1.0"

# Extract .pot files
# xgettext \
#   --language=Python \
#   --from-code=UTF-8 \
#   --package-name="$PACKAGE_NAME" \
#   --package-version="$PACKAGE_VERSION" \
#   -o about.pot ./../pages/about.py

# xgettext \
#   --language=Python \
#   --from-code=UTF-8 \
#   --package-name="$PACKAGE_NAME" \
#   --package-version="$PACKAGE_VERSION" \
#   -o app.pot ./../app.py

# xgettext \
#   --language=Python \
#   --from-code=UTF-8 \
#   --package-name="$PACKAGE_NAME" \
#   --package-version="$PACKAGE_VERSION" \
#   -o main.pot ./../pages/main.py

# xgettext \
#   --language=Python \
#   --from-code=UTF-8 \
#   --package-name="$PACKAGE_NAME" \
#   --package-version="$PACKAGE_VERSION" \
#   -o help.pot ./../pages/help.py

# xgettext \
#   --language=Python \
#   --from-code=UTF-8 \
#   --package-name="$PACKAGE_NAME" \
#   --package-version="$PACKAGE_VERSION" \
#   -o districts.pot ./../pages/districts.py

# xgettext \
#   --language=Python \
#   --from-code=UTF-8 \
#   --package-name="$PACKAGE_NAME" \
#   --package-version="$PACKAGE_VERSION" \
#   -o rooms.pot ./../pages/rooms.py

xgettext \
  --language=Python \
  --from-code=UTF-8 \
  --package-name="$PACKAGE_NAME" \
  --package-version="$PACKAGE_VERSION" \
  -o trends.pot ./../pages/trends.py
