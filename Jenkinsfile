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
                sh "docker image build -t shaikkhajaibrahim/courses:develop-$env.BUILD_ID ."
                sh "docker image push shaikkhajaibrahim/courses:develop-$env.BUILD_ID"
            }
        }
        stage('deploy') {
            steps {
                sh "cd deployments/courses/overlays/develop && kustomize edit set image courses=shaikkhajaibrahim/courses:develop-$env.BUILD_ID"
                sh 'kubectl apply -k deployments/courses/overlays/develop'
            }
        }

    }
}