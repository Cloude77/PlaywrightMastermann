pipeline {
    agent any
    stages {
        stage('Install Dependencies') {  //  Изменили название этапа
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