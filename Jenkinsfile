pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                powershell '''
                    & .\\venv\\Scripts\\Activate.ps1
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                powershell '''
                    & .\\venv\\Scripts\\Activate.ps1
                    playwright test test_main_page.py
                '''
            }
        }
    }
}