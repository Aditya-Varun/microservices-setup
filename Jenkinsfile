pipeline {
    agent any

    environment {
        // Optional: Define environment variables here
    }

    stages {
        stage('Clone Repositories') {
            steps {
                script {
                    // Clone your services repositories (if not already part of the setup)
                    checkout scm
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    // Build Docker images for all services
                    sh 'docker-compose -f docker-compose.yml build'
                }
            }
        }
        stage('Run Integration Tests') {
            steps {
                script {
                    // Run the containers using Docker Compose for integration testing
                    sh 'docker-compose -f docker-compose.yml up -d'
                    // Add your integration tests here (e.g., curl requests or other test scripts)
                    // Example: sh './run_integration_tests.sh'
                }
            }
        }
        stage('Teardown') {
            steps {
                script {
                    // Stop and remove the containers after testing
                    sh 'docker-compose -f docker-compose.yml down'
                }
            }
        }
    }

    post {
        always {
            // This block will run after the pipeline finishes
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
