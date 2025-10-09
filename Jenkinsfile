pipeline {
    agent any

    environment {
        IMAGE_NAME = 'gaganreddy508/scientific-calculator'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/gaganreddy23/scicalc-py.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} pytest /app/test_calculator.py'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([string(credentialsId: 'SUDO_PASS', variable: 'SUDO_PASS')]) {
                    sh 'echo $SUDO_PASS | sudo -S ansible-playbook -i inventory.ini deploy.yml'
                }
            }
        }
    }
}
