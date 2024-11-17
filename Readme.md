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


Remote Docker API:
systemctl status docker
systemctl start docker
systemctl restart docker
systemctl stop docker

/usr/lib/systemd/system/docker.service
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:4243 -H unix:///var/run/docker.sock

rm -rf  /etc/docker/daemon.json
{
    "hosts": ["unix:///var/run/docker.sock", "tcp://0.0.0.0:4243"]
}

sudo systemctl restart docker
sudo journalctl -u docker.service
sudo netstat -lntp | grep dockerd
sudo netstat -tuln | grep 4243
ps aux | grep dockerd

sestatus
sudo setenforce 0

curl -v http://localhost:4243/version
curl -v http://127.0.0.1:4243/version
curl -v http://192.168.1.190:4243/version

sudo ufw allow 4243/tcp
sudo iptables -A INPUT -p tcp --dport 4243 -j ACCEPT
sudo iptables -I INPUT -p udp --dport 4243 -j ACCEPT
sudo service iptables save
sudo netfilter-persistent save
sudo iptables -L -n
sudo iptables -L -n | grep 4243

systemctl daemon-reload
sudo firewall-cmd --permanent --add-port=4243/tcp
sudo firewall-cmd --permanent --add-port=4243/udp
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports
sudo systemctl enable firewalld
sudo systemctl stop firewalld
sudo systemctl status firewalld
sudo systemctl start firewalld
sudo systemctl mask firewalld

tcp://192.168.1.190:4243
demo-docker-slave
bibinwilson/jenkins-slave:latest

sudo yum install -y java-11-openjdk-devel
java -version
sudo alternatives --config java
  select the java version

OR
wget https://download.java.net/openjdk/jdk11/ri/openjdk-11+28_linux-x64_bin.tar.gz
tar xvf openjdk-11+28_linux-x64_bin.tar.gz
export JAVA_HOME=/path/to/jdk-11
export PATH=$JAVA_HOME/bin:$PATH

yum install epel-release -y
sudo yum install python3 -y
python3 --version
sudo alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo yum install python3-pip -y
pip3 install --upgrade pip
pip3 --version
pip install flask==2.1.0
pip show flask

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh

eval "$(/root/anaconda3/bin/conda shell.bash hook)"
conda init
source ~/.bashrc
conda --version

usermod -aG root jenkins
su jenkins
eval "$(/root/anaconda3/bin/conda shell.bash hook)"
chmod +x /root/anaconda3/bin/conda
chown -R jenkins:jenkins /root/anaconda3

conda create --name myenv python=3.9
conda activate myenv
python --version
conda install flask

source /root/anaconda3/bin/activate

visudo
jenkins ALL=(ALL) NOPASSWD: /root/anaconda3/bin/conda



