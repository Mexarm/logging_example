pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('python') {
            steps {
                sh 'python --version'
            }
        }
        stage('install deps') {
            steps {
                sh 'pip install pipenv'
                dir('django') {
                    sh 'pipenv install'
                }
            }
        }
        stage('run tests') {
            steps {
                dir('django'){
                    sh 'pipenv run python manage.py test'    
                }
            }   
        }
    }
}