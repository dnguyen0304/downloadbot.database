ARG DOMAIN
ARG PACKAGE_NAME
ARG BASE_IMAGE_VERSION
FROM ${DOMAIN}/${PACKAGE_NAME}-buildtime-base:${BASE_IMAGE_VERSION}

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG PACKAGE_NAME
ARG CONFIGURATION_DIRECTORY_NAME

ARG build_executable="build.sh"

# Include the build executable.
COPY docker/buildtime/${build_executable} .

# Include the source code.
COPY ${PACKAGE_NAME} ./${PACKAGE_NAME}

# Include the dependencies.
# The destination directory must end with a forward slash ("/") when copying
# more than one source files.
COPY requirements*.txt ./

# Include the configuration.
COPY ${CONFIGURATION_DIRECTORY_NAME} ./${CONFIGURATION_DIRECTORY_NAME}

# Include the entry point.
COPY main.py .
