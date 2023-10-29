pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('Docker_Account')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ca4_backend:latest ./db'
            }
        }

        stage('Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Docker_Account', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
                }
            }
        }

        stage('Push') {
            steps {
                sh 'docker push ca4_backend:latest'
            }
        }
    }
}
