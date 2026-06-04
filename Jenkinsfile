pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'dir'
                bat 'docker build --no-cache -t titanic-ml:v1.0 .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker rm -f titanic-ci || exit 0'
                bat 'docker run -d -p 5000:5000 --name titanic-ci titanic-ml:v1.0'
            }
        }
    }

    post {
        success {
            echo 'Build and Deployment SUCCESS'
        }
        failure {
            echo 'Pipeline FAILED Check logs'
        }
    }
}