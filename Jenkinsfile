pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/NiharikaSankhla/summer-training-project'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t titanic-ml:v1.0 .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name titanic-ci titanic-ml:v1.0'
            }
        }
    }
}