pipeline {
    agent any

    environment {
        IMAGE_NAME = "scientific-calculator"
        DOCKERHUB_USER = "your_dockerhub_username"   // 👈 replace with yours
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm $IMAGE_NAME'
            }
        }

        stage('Push to Docker Hub') {
            when {
                expression { env.BRANCH_NAME == 'main' }
            }
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKERHUB_TOKEN')]) {
                    sh '''
                    echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USER" --password-stdin
                    docker tag $IMAGE_NAME $DOCKERHUB_USER/$IMAGE_NAME:latest
                    docker push $DOCKERHUB_USER/$IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose -f deploy.yml up -d'
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
    }
}
