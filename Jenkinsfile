pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-creds' // Jenkins credentials ID
        IMAGE_NAME = 'gaganreddy508/scientific-calculator'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/gaganreddy23/scicalc-py.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}:${IMAGE_TAG}").inside {
                        sh 'pytest --maxfail=1 --disable-warnings -q'
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment step: run container on your server if needed'
            }
        }
    }
}
