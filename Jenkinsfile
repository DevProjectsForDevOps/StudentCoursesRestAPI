pipeline {
    agent { label 'k8s' }
    triggers { pollSCM('* * * * *') }
    stages {
        stage('vcs') {
            steps {
                git branch: 'develop',
                    url: 'https://github.com/DevProjectsForDevOps/StudentCoursesRestAPI.git'
            }
        }
        stage('build and deploy') {
            steps {
                sh 'docker image build -t shaikkhajaibrahim/courses:latest .'
                sh 'docker image push shaikkhajaibrahim/courses:latest'
            }
        }


    }
}