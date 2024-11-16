# Install the Helm chart
helm install model-release ./model-chart \
  --namespace model-namespace \
  --set image.repository=your-docker-repo/model-image \
  --set image.tag=latest

# OR upgrade an existing release
helm upgrade --install model-release ./model-chart \
  --namespace model-namespace \
  --set image.repository=your-docker-repo/model-image \
  --set image.tag=latest
