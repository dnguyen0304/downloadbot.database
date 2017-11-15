ARG DOMAIN
ARG NAMESPACE
ARG BASE_IMAGE_VERSION
FROM ${DOMAIN}/${NAMESPACE}-runtime:${BASE_IMAGE_VERSION}

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ENTRYPOINT python -c "import nose; nose.main()"
