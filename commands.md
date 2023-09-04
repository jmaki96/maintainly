# Commands needed to do common operations

## Running compose locally
docker compose build

docker compose up

## Building

### AMD Target
docker buildx build --platform linux/amd64 --tag us-central1-docker.pkg.dev/maintainly-prod/maintainly/maintainly_amd:version .

### ARM Target


docker push us-east1-docker.pkg.dev/maintainly-prod/maintainly-dockerhub/maintainly:version

docker push us-east1-docker.pkg.dev/maintainly-prod/maintainly-dockerhub/maintainly_amd:version


gcloud artifacts repositories add-iam-policy-binding maintainly \
    --location=us-central1 \
    --member=serviceAccount:349075390319-compute@developer.gserviceaccount.com \
    --role="roles/artifactregistry.reader"