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
                    // Build and tag the Docker image for the web service.
                    docker.build('ca4_frontend:latest', '.')

                    // Push Docker image to Docker Hub.
                    docker.withRegistry('https://registry.hub.docker.com', 'DockerHubCredentials') {
                        docker.image('ca4_frontend:latest').push()
                    }
                }
            }
        }
    }
}