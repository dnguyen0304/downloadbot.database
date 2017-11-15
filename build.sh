#!/usr/bin/env bash

set -eu

if [ "${1:-}" = test ]; then
    for_testing="true"
else
    for_testing="false"
fi

DOMAIN="dnguyen0304"
PACKAGE_NAME=$(./scripts/get-package-name.sh)
VERSION=$(./scripts/get-package-version.sh)
CONFIGURATION_DIRECTORY_NAME=$(./scripts/get-configuration-directory-name.sh)
REMOTE_SHARED_VOLUME="/tmp/build"

# Clean up existing packages created by previous builds.
rm --force ${PACKAGE_NAME}*.zip

# Create the buildtime image.
BUILDTIME_BASE_IMAGE_VERSION="0.1.0"
tag=${DOMAIN}/${PACKAGE_NAME}-buildtime:${VERSION}

if [ ! -z $(sudo docker images --quiet ${tag}) ]; then
    docker rmi --force ${tag}
fi
# This must pass the PACKAGE_NAME build argument twice. See the documentation
# for more details [1].
#
# Links
# [1] https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact
docker build \
    --file docker/buildtime/Dockerfile \
    --tag ${tag} \
    --build-arg DOMAIN=${DOMAIN} \
    --build-arg PACKAGE_NAME=${PACKAGE_NAME} \
    --build-arg BASE_IMAGE_VERSION=${BUILDTIME_BASE_IMAGE_VERSION} \
    --build-arg PACKAGE_NAME=${PACKAGE_NAME} \
    --build-arg CONFIGURATION_DIRECTORY_NAME=${CONFIGURATION_DIRECTORY_NAME} \
    .

# Create the package.
docker run \
    --rm \
    --volume $(pwd):${REMOTE_SHARED_VOLUME} \
    ${tag} \
    ${PACKAGE_NAME} ${REMOTE_SHARED_VOLUME} ${VERSION} ${CONFIGURATION_DIRECTORY_NAME} ${for_testing}

# Create the runtime image.
RUNTIME_BASE_IMAGE_VERSION="0.1.0"
tag=${DOMAIN}/${PACKAGE_NAME}-runtime:${VERSION}

if [ ! -z $(sudo docker images --quiet ${tag}) ]; then
    docker rmi --force ${tag}
fi
docker build \
    --file docker/runtime/Dockerfile \
    --tag ${tag} \
    --build-arg DOMAIN=${DOMAIN} \
    --build-arg PACKAGE_NAME=${PACKAGE_NAME} \
    --build-arg BASE_IMAGE_VERSION=${RUNTIME_BASE_IMAGE_VERSION} \
    --build-arg PACKAGE_NAME=${PACKAGE_NAME} \
    .

if [ "${for_testing}" = true ]; then
    docker build \
        --file docker/runtime/testing/Dockerfile \
        --tag ${tag} \
        --build-arg DOMAIN=${DOMAIN} \
        --build-arg PACKAGE_NAME=${PACKAGE_NAME} \
        --build-arg BASE_IMAGE_VERSION=${RUNTIME_BASE_IMAGE_VERSION} \
        .
fi
