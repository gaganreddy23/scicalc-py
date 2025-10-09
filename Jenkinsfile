pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
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
                // Run automated tests only
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
    }

    post {
        always {
            echo "Cleaning up Docker images..."
            sh 'docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || true'
        }
        success {
            echo "Pipeline succeeded!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
