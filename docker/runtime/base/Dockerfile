FROM python:3.5-slim

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG PACKAGE_NAME
ARG CONFIGURATION_DIRECTORY_NAME
ARG CONFIGURATION_FILE_NAME

# unzip is needed to extract the package.
ENV BUILDTIME_DEPENDENCIES="unzip"

ARG PACKAGE_DIRECTORY="/opt/${PACKAGE_NAME}"

# PWD is an environment variable available in the AWS Lambda runtime.
ENV CONFIGURATION_FILE_PATH="${PWD}/${PACKAGE_NAME}/${CONFIGURATION_DIRECTORY_NAME}/${CONFIGURATION_FILE_NAME}"

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ${BUILDTIME_DEPENDENCIES}

RUN useradd ${PACKAGE_NAME}

RUN mkdir ${PACKAGE_DIRECTORY}

WORKDIR ${PACKAGE_DIRECTORY}

RUN rm -fr /var/lib/apt/lists/*
