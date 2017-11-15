ARG DOMAIN
ARG PACKAGE_NAME
ARG BASE_IMAGE_VERSION
FROM ${DOMAIN}/${PACKAGE_NAME}-buildtime-base:${BASE_IMAGE_VERSION}

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG PACKAGE_NAME

ARG BUILD_EXECUTABLE="build.sh"

COPY docker/buildtime/${BUILD_EXECUTABLE} .
COPY ${PACKAGE_NAME} ./${PACKAGE_NAME}
# The destination directory must end with a forward slash ("/") when copying
# more than one source files.
COPY requirements*.txt ./
COPY main.py .
