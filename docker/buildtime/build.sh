#!/usr/bin/env bash

set -eu

PACKAGE_NAME=$1
SHARED_VOLUME=$2
VERSION=$3
CONFIGURATION_DIRECTORY_NAME=$4
FOR_TESTING=$5

# Set the build root to the working directory. Now relative references
# may be used.
BUILD_ROOT=$(pwd)

PACKAGE="${PACKAGE_NAME}-${VERSION}"
mkdir ${PACKAGE}

# Include the source code.
cp -r ${PACKAGE_NAME} ${PACKAGE}

# Include the dependencies.
if [ ${FOR_TESTING} = "true" ] && [ -s requirements-testing.txt ]; then
    pip install --requirement requirements-testing.txt --target ${PACKAGE}
elif [ -s requirements.txt ]; then
    pip install --requirement requirements.txt --target ${PACKAGE}
fi

# Include the configuration.
cp -r ${CONFIGURATION_DIRECTORY_NAME} ${PACKAGE}

# Include the entry point.
cp main.py ${PACKAGE}

# Archive the package.
cd ${PACKAGE}
zip -9qr ${PACKAGE}.zip .
cp ${PACKAGE}.zip ${PACKAGE_NAME}-latest.zip
mv ${PACKAGE_NAME}-*.zip ${SHARED_VOLUME}
