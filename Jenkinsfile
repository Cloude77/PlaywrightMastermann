pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Cloude77/PlaywrightMastermann.git'
            }
        }
        stage('Setup') {
            steps {
                // Указываем путь к виртуальному окружению
                powershell '''
                    & .\\venv\\Scripts\\Activate.ps1
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                // Запускаем тесты Playwright
                powershell 'playwright test test_main_page.py'
            }
        }
    }
}