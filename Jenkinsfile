pipeline {
    agent any

    environment {
        // Define your environment variables here
        DOCKER_IMAGE = 'edaraanand/smodel1'
        DOCKER_TAG = "${env.BRANCH_NAME}-${env.GIT_COMMIT.take(7)}"
        HELM_RELEASE_NAME = 'model-release'
        K8S_NAMESPACE = 'model-namespace'
        MODEL_PATH = 'src/model'  // Path to your model code
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the model repository
                    checkout scm
                }
            }
        }
        stage('Install Dependencies | Setup Environment') {
            steps {
                script {
                    // Install Python and pip in the Docker container (for Ubuntu-based images)
                    // TODO
                    // python3 -m venv venv
                    // source venv/bin/activate
                    sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip
                    pip3 install -r requirements.txt
                    '''
                }
            }
        }
        stage('Train Model') {
            steps {
                script {
                    // Train the model (adjust for your model's training script)
                    sh '''
                    python ${MODEL_PATH}/train.py --epochs 10 --batch_size 32
                    '''
                }
            }
        }

        stage('Test Model') {
            steps {
                script {
                    // Test the trained model (adjust as necessary)
                    sh '''
                    python ${MODEL_PATH}/test.py
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh '''
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    '''
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    // Push Docker image to your container registry
                    sh '''
                    docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD} ${DOCKER_REGISTRY}
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes via Helm') {
            steps {
                script {
                    // Deploy the model using Helm
                    // You might need to modify the Helm chart's values (like the image tag)
                    sh '''
                    helm upgrade --install ${HELM_RELEASE_NAME} ./helm/model-chart \
                      --set image.repository=${DOCKER_IMAGE} \
                      --set image.tag=${DOCKER_TAG} \
                      --namespace ${K8S_NAMESPACE}
                    '''
                }
            }
        }

        stage('Monitor Deployment') {
            steps {
                script {
                    // Monitor the deployment or check status
                    sh '''
                    kubectl rollout status deployment/${HELM_RELEASE_NAME} --namespace ${K8S_NAMESPACE}
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    // Clean up resources (optional, for example, removing old Docker images)
                    sh '''
                    docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG}
                    '''
                }
            }
        }
    }

    post {
        always {
            // Always execute clean up actions
            cleanWs()
        }
        success {
            // Notify if build is successful
            echo "Model deployment to Kubernetes was successful!"
        }
        failure {
            // Notify if build failed
            echo "Model deployment to Kubernetes failed!"
        }
    }
}
