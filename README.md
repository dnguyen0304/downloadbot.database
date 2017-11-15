# Download Bot Cache
An event handler that writes to cache.

NOTE: Remember to replace the <tag> placeholder where applicable.

## Getting Started
### Configuring
Update the configuration files in the `configuration` directory.

### Building
```
sudo ./build.sh
```

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

### Deploying the application.
1. Install `docker`.
2. Install `git`.
3. Clone the repository.
```
git clone https://github.com/dnguyen0304/downloadbot_cache.git
```
4. Change the working directory.
```
cd downloadbot_cache
```
5. Build and configure the application. See the notes in the _Getting Started_ section.
6. Upload the build artifacts to S3.
7. Create the Lambda Function.

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
