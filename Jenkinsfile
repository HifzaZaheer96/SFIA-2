pipeline {
    agent any
    stages {
        stage('Development Environment') {
            steps {
                sh 'chmod +x ./script/*'
                sh './script/ansible.sh'
                sh './script/docker.sh'
                sh './script/before_installation.sh'
                sh './script/make_service.sh'
           
                
            }
        }
        stage('Wait for installation'){
            steps{
                
                sh 'sleep 10'
               
            }
        }

         stage('Testing'){
            steps {
                sh './script/testing.sh'

            }
         }
    }
}

