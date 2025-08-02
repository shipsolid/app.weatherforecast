#!/bin/bash
set -euo pipefail

# ---------------------
# Configurable Variables
# ---------------------
SERVICE_NAME="my-app"                        # Must match the service name in docker-compose.yml
REGISTRY="ghcr.io"
OWNER="${GITHUB_REPOSITORY_OWNER:-$(git config user.name)}"  # Default fallback to Git user
OWNER_LC=$(echo "$OWNER" | tr '[:upper:]' '[:lower:]')       # GHCR requires lowercase
IMAGE_NAME="${REGISTRY}/${OWNER_LC}/${SERVICE_NAME}"

# ---------------------
# Derive App Version
# ---------------------
if git describe --tags --abbrev=0 &>/dev/null; then
  APP_VERSION=$(git describe --tags --always)
else
  APP_VERSION="dev-$(git rev-parse --short HEAD)"
fi

echo "🔧 Building ${SERVICE_NAME} version: $APP_VERSION"
echo "📦 Target image: ${IMAGE_NAME}:${APP_VERSION}"

# ---------------------
# Docker Login (optional if done in workflow)
# ---------------------
if ! docker info | grep -q "$REGISTRY"; then
  echo "🔐 Logging in to $REGISTRY"
  echo "$GHCR_TOKEN" | docker login "$REGISTRY" -u "$OWNER" --password-stdin
fi

# ---------------------
# Build and Tag Docker Image
# ---------------------
docker compose build \
  --pull \
  --build-arg "MY_APP_VERSION=${APP_VERSION}"

# Tag explicitly for version + latest
docker tag "$SERVICE_NAME" "${IMAGE_NAME}:${APP_VERSION}"
docker tag "$SERVICE_NAME" "${IMAGE_NAME}:latest"

# ---------------------
# Push Tags to GHCR
# ---------------------
# echo "🚀 Pushing tags to GHCR..."
# docker push "${IMAGE_NAME}:${APP_VERSION}"
# docker push "${IMAGE_NAME}:latest"

echo "✅ Done. Image pushed:"
echo " - ${IMAGE_NAME}:${APP_VERSION}"
echo " - ${IMAGE_NAME}:latest"
