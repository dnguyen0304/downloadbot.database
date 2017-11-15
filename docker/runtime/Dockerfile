ARG DOMAIN
ARG PACKAGE_NAME
ARG BASE_IMAGE_VERSION
FROM ${DOMAIN}/${PACKAGE_NAME}-runtime-base:${BASE_IMAGE_VERSION}

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG PACKAGE_NAME

ARG PACKAGE="${PACKAGE_NAME}-latest.zip"

COPY ${PACKAGE} .

RUN unzip -q ${PACKAGE} && \
    chown --recursive ${PACKAGE_NAME}:${PACKAGE_NAME} . && \
    rm ${PACKAGE}

RUN apt-get purge -y --auto-remove ${BUILDTIME_DEPENDENCIES}
