pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub' // Jenkins credentials ID for Docker Hub
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
                    // Build the Docker image
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Run Calculator & Tests') {
            steps {
                script {
                    // Run calculator.py and pytest inside the Docker container
                    docker.image("${IMAGE_NAME}:${IMAGE_TAG}").inside {
                        sh 'python app/calculator.py'  // run your calculator script
                        sh 'pytest --maxfail=1 --disable-warnings -q'  // run tests
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }
    }
}
