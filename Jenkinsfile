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
                    try {
                        // Build Docker images for all services
                        sh "docker-compose -f docker-compose.yml build"
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Run Integration Tests') {
            steps {
                script {
                    try {
                        // Start all services using Docker Compose
                        sh "docker-compose -f docker-compose.yml up -d"
                        
                        // Wait for services to be fully up (adjust sleep time if needed)
                        sleep 30  // Optional: wait for services to start properly

                        // Run your integration tests here (e.g., using curl or a testing script)
                        // Example:
                        sh 'curl -f http://localhost:8001/healthcheck || exit 1'
                        sh 'curl -f http://localhost:8002/healthcheck || exit 1'
                        sh 'curl -f http://localhost:8003/healthcheck || exit 1'

                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Tear Down') {
            steps {
                script {
                    try {
                        // Stop and remove the services (containers)
                        sh "docker-compose -f docker-compose.yml down --volumes --remove-orphans"
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images, containers, volumes, etc. after the build
            sh "docker system prune -f"
        }
        success {
            echo 'The pipeline completed successfully.'
        }
        failure {
            echo 'The pipeline failed. Please check the logs for more details.'
        }
    }
}
