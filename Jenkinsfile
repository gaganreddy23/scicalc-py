pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t gaganreddy508/scientific-calculator:latest .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm gaganreddy508/scientific-calculator:latest pytest /app/test_calculator.py'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                    sh 'docker push gaganreddy508/scientific-calculator:latest'
                }
            }
        }

        stage('Deploy') {
            steps {
                // sudo no longer requires password
                sh 'sudo ansible-playbook -i inventory.ini deploy.yml'
            }
        }
    }
}
