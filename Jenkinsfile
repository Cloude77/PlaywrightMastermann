pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                powershell(returnStdout: true, script: '''
                    try {
                        Write-Output "----- Начало установки зависимостей -----"
                        & .\\venv\\Scripts\\Activate.ps1
                        pip install -r requirements.txt
                        Write-Output "----- Зависимости установлены -----"
                    } catch {
                        Write-Error $_.Exception.Message
                    }
                    exit 0  #  Выход  с  кодом  0  после  блока  try...catch
                ''')
            }
        }
        stage('Test') {
            steps {
                powershell(returnStdout: true, script: '''
                    & .\\venv\\Scripts\\Activate.ps1  # Активируем окружение
                    playwright test test_main_page.py
                ''')
            }
        }
    }
}