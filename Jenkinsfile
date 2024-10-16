pipeline {
    agent any
    stages {
        stage("Unit Test") {
            steps {
                sh 'python -m unittest test_calculator.py'
            }
        }
    }
    post {
        success {
            echo "Success"
        }
        failure {
            echo "Failure"
        }
    }
}
