# Commands needed to do common operations

## Building

### AMD Target
docker buildx build --platform linux/amd64 --tag us-east1-docker.pkg.dev/maintainly-prod/maintainly-dockerhub/maintainly_amd:version .

### ARM Target


docker push us-east1-docker.pkg.dev/maintainly-prod/maintainly-dockerhub/maintainly:version

docker push us-east1-docker.pkg.dev/maintainly-prod/maintainly-dockerhub/maintainly_amd:version