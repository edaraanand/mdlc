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

docker pull jenkins/jenkins:lts

docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v downloads_jenkins_home:/var/jenkins_home jenkins/jenkins:lts

docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v downloads_jenkins_home:/var/jenkins_home jenkins_custom_lts:v1

:Didn't work:
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v downloads_jenkins_home_1:/var/jenkins_home jenkins_custom_lts:v1

#build
curl -v -u anand:anand http://localhost:8080/job/smodel1-pipeline/build?token=rngbaObFGOR69S0ISquftn0uz31uFzfk

#buildWithParameters
curl -v -u anand:anand "http://localhost:8080/job/smodel1-pipeline/buildWithParameters?token=rngbaObFGOR69S0ISquftn0uz31uFzfk&target_env=anand"

CSRF Protection
curl -v -u anand:anand "http://localhost:8080/crumbIssuer/api/json"

Jenkins has built-in protection against CSRF attacks, and it requires a Jenkins-Crumb token to be included in the request when triggering jobs remotely via the API.

curl -v -u anand:anand -H "Jenkins-Crumb: 0713398a4383b8fcbf7ff4729a2c4743d09b56500c27b631629d50fce6a68ce3" "http://localhost:8080/job/smodel1-pipeline/buildWithParameters?token=rngbaObFGOR69S0ISquftn0uz31uFzfk&target_env=anand"

