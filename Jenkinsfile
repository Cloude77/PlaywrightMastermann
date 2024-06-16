pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    #!/bin/bash
                    set -e
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    #!/bin/bash
                    set -e
                    source venv/bin/activate
                    playwright test test_main_page.py
                '''
            }
        }
    }
}