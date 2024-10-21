pipeline {
    agent {
        dockerContainer {
            image 'jenkins/agent'
        }
    }
    stages {
        stage("Unit Test") {
            agent {
                dockerContainer 'python:bookworm'
            }
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
