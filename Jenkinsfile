pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                powershell(returnStdout: true, script: '''
                    try {
                        & .\\venv\\Scripts\\Activate.ps1
                        pip install -r requirements.txt
                    } catch {
                        Write-Error $_.Exception.Message
                        exit 1
                    }
                ''')
            }
        }
        stage('Test') {
            steps {
                powershell 'playwright test test_main_page.py'
            }
        }
    }
}