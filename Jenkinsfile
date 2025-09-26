pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/dilkkumar/flask-ci-demo2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$(pwd)
                pytest test_app.py
                '''
            }
        }

        stage('Build & Deploy') {
            steps {
                sh '''
                . venv/bin/activate
                nohup python app.py &
                '''
            }
        }
    }
}
