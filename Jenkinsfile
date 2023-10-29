pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    
                    def frontendImageExists = sh(script: 'docker pull analysts/ca4_frontend:latest', returnStatus: true) == 0
                    def backendImageExists = sh(script: 'docker pull analysts/ca4_backend:latest', returnStatus: true) == 0

                    if (frontendImageExists && backendImageExists) {
                        sh 'docker-compose up -d'
                    } else {
                        error 'Required Docker images not found on Docker Hub.'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Docker Compose stack started successfully.'
        }
        failure {
            error 'Failed to start Docker Compose stack.'
        }
    }
}