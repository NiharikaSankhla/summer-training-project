pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build --no-cache -t titanic-ml:v1.0 .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker stop titanic-ci || exit 0'
                bat 'docker rm titanic-ci || exit 0'
                bat 'docker run -d -p 5000:5000 --name titanic-ci titanic-ml:v1.0'
            }
        }
    }
}