pipeline {
    agent any
    stages {
        stage("Unit Test") {
            steps {
                sh 'python3 -m unittest test_calculator.py'
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
