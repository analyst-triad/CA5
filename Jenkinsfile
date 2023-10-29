pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image for the Database service
                    docker.build('ca4_frontend:latest', '.')
                }
            }
        }

        
         stage('Docker Login and Push') {
            steps {
                script {
                    // Use Docker Hub credentials
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                        sh "docker push ca4_frontend:latest"
                    }
                }
            }
        }
    }
}