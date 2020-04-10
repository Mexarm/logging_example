pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('python') {
            steps {
                sh 'python --version'
            }
        }
        stage('install') {
            steps {
                sh 'pip install pipenv'
                dir('django') {
                    sh 'pipenv install'
                }
            }
        }
    }
}