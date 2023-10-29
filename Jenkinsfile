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
            sh 'docker build -t analysts/ca4_frontend:latest .'
        }
        }
        stage('Login') {
        steps {
            sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
        }
        }
        stage('Push') {
        steps {
            sh 'docker push analysts/ca4_frontend:latest'
        }
    }
    }
}