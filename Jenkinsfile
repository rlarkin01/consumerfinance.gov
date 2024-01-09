/*
 * Normal Jenkinsfile to demonstrate dual JS/Python SCA scans when using requirements folder in place of requirements.txt
 */

pipeline {
    agent any

    options {
        // only keep the last x build logs and artifacts (for space saving)
        buildDiscarder(logRotator(numToKeepStr: '20', artifactNumToKeepStr: '20'))
    }

    stages{
        // stage ('Prep') {
        //     steps {
        //         npm "install -g yarn"
        //     }
        // }
        
        stage ('Veracode SCA') {
            steps {
                echo 'Veracode SCA'
                withCredentials([ string(credentialsId: 'SCA_Token', variable: 'SRCCLR_API_TOKEN')]) {
                    withMaven(maven:'maven-3') {
                        script {
                            // npm 'install -g yarn'
                            // yarn "init -y"
                            
                            sh "echo '-r ./requirements/deployment.txt' > requirements.txt"
                            sh "echo 'skip_collectors: \"yarn\"' > srcclr.yml"
                            sh "curl -sSL https://download.sourceclear.com/ci.sh | sh"
                            // sh "pip install -r requirements.txt"

                            // debug, no upload
                            //sh "curl -sSL https://download.sourceclear.com/ci.sh | DEBUG=1 sh -s -- scan --no-upload"
                        }
                    }
                }
            }
        }
    }
}
