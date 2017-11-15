FROM python:3.5-slim

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG PACKAGE_NAME
ARG CONFIGURATION_DIRECTORY_NAME
ARG CONFIGURATION_FILE_NAME

ARG aws_lambda_directory="/var/task"

# unzip is needed to extract the package.
ENV BUILDTIME_DEPENDENCIES="unzip"

# This is needed by child images.
ENV PACKAGE_DIRECTORY="${aws_lambda_directory}/${PACKAGE_NAME}"
# This is needed by the application to find the configuration file.
ENV CONFIGURATION_FILE_PATH="${PACKAGE_DIRECTORY}/${CONFIGURATION_DIRECTORY_NAME}/${CONFIGURATION_FILE_NAME}"

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ${BUILDTIME_DEPENDENCIES}

RUN useradd ${PACKAGE_NAME}

RUN mkdir --parents ${PACKAGE_DIRECTORY}

WORKDIR ${PACKAGE_DIRECTORY}

RUN rm -fr /var/lib/apt/lists/*
