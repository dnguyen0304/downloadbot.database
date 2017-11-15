# Download Bot Cache
An event handler that writes to cache.

NOTE: Remember to replace the <tag> placeholder where applicable.

## Getting Started
### Building
```
sudo ./build.sh
```

### Configuring
Update the configuration files in the `configuration` directory.

## Advanced
### Testing the application
1. Build the image.
```
sudo ./build.sh test
```
2. Update the configuration files in the `configuration` directory.
3. Run the test suite.
```
sudo docker run \
    --rm \
    --volume $(pwd)/configuration:/etc/opt/downloadbot_cache \
    dnguyen0304/downloadbot_cache-runtime:<tag>
```

### Managing the base buildtime image
1. Change the working directory to the package root directory.
2. Build the image.
```
sudo ./scripts/build-buildtime-base.sh
```
3. Push the image.
```
sudo docker push dnguyen0304/downloadbot_cache-buildtime-base:<tag>
```

### Managing the base runtime image
1. Change the working directory to the package root directory.
2. Build the image.
```
sudo ./scripts/build-runtime-base.sh
```
3. Push the image.
```
sudo docker push dnguyen0304/downloadbot_cache-runtime-base:<tag>
```
