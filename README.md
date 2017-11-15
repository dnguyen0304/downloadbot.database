# Download Bot Cache
An event handler that writes to cache.

NOTE: Remember to replace the <tag> placeholder where applicable.

## Getting Started

## Advanced
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
