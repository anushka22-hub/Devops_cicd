
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Retrieving source code from GitHub'

                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/Devops_Exp.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building REST API application'

                bat '''
                    py -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt

                    if not exist dist mkdir dist

                    powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path app.py,requirements.txt -DestinationPath dist\\rest-api.zip -Force"
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running REST API tests'

                bat '''
                    if not exist reports mkdir reports

                    .venv\\Scripts\\python.exe -m pytest test_app.py --junitxml=reports\\test-results.xml
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo 'Archiving generated artifacts'

                archiveArtifacts artifacts: 'dist/*.zip',
                                 fingerprint: true
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'reports/*.xml'
        }

        success {
            echo 'REST API pipeline completed successfully!'
        }

        failure {
            echo 'REST API pipeline failed!'
        }
    }
}
