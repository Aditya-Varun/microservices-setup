pipeline {
    agent any

    environment {
        DOCKER_COMPOSE = '/usr/local/bin/docker-compose'  // Path to Docker Compose
    }

    stages {
        stage('Clone Repositories') {
            steps {
                script {
                    checkout scm  // This will automatically pull the repository
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    // Build Docker images for all services
                    sh "docker-compose -f docker-compose.yml build"
                }
            }
        }

        stage('Run Integration Tests') {
            steps {
                script {
                    // Start all services using Docker Compose
                    sh "docker-compose -f docker-compose.yml up -d"
                    
                    // Run your integration tests here (e.g., using curl or a testing script)
                    // Example:
                    // sh 'curl http://localhost:8001/healthcheck'
                    // sh 'curl http://localhost:8002/healthcheck'
                    // sh 'curl http://localhost:8003/healthcheck'
                    
                    // Optionally: Run your test suite against the services running on docker-compose
                }
            }
        }

        stage('Tear Down') {
            steps {
                script {
                    // Stop the services
                    sh "docker-compose -f docker-compose.yml down"
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images if needed
            sh "docker system prune -f"
        }
    }
}
