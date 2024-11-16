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

grep -ri "your_search_string" /path/to/directory
find /path/to/directory -type f -name "*.txt" -exec grep -H "your_search_string" {} \;
find /path/to/directory -type f | xargs grep -H "your_search_string"
  The -H option tells grep to print the filename alongside the matching line of text, even if only one file is being searched.
  The {} is a placeholder used in the find command when combined with -exec to represent the current file that find is processing.
  \;: The semicolon ends the -exec command. It’s escaped (\;) because the semicolon has special meaning in the shell.
