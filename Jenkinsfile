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
                    exit 0  #  Выход с кодом 0 после блока try...catch
                '''
            }
        }
        // … остальной  код
    }
}