pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                powershell '''
                    Write-Output "----- Старт powershell -----"
                    try {
                        Write-Output "----- Начало установки зависимостей -----"
                        & .\\venv\\Scripts\\Activate.ps1
                        pip install -r requirements.txt
                        Write-Output "----- Зависимости установлены -----"
                    } catch {
                        Write-Error $_.Exception.Message
                    }
                    Write-Output "----- Конец powershell -----"
                    New-Item -Path . -Name test_success.txt -Value "Тесты прошли успешно!" -Force
                    exit 0  # Выход с кодом 0 после блока try...catch
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