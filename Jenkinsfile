pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build and tag the Docker image for the Database service.
                    docker.build('ca4_backend:latest', './db')

                    // Push the Docker image to DockerHub
                    docker.withRegistry('https://registry.hub.docker.com', 'DockerHubCredentials') {
                        docker.image('ca4_backend:latest').push()
                    }
                }
            }
        }
    }
}