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
        stage ('Veracode SCA') {
            steps {
                echo 'Veracode SCA'
                withCredentials([ string(credentialsId: 'SCA_Token', variable: 'SRCCLR_API_TOKEN')]) {
                    withMaven(maven:'maven-3') {
                        script {
                            sh '''
                                cp ./requirements/deployment.txt req_tmp.txt
                                while IFS= read -r line
                                    do
                                        if [ ${line:0:3}!="-r " ]
                                        then
                                            echo $line
                                        else
                                            echo "-r requirements/${line:3}"
                                        fi
                                    done < req_tmp.txt > requirements.txt
                                rm req_tmp.txt
                            '''
                            
                                // To run through entire folder:
                                // cd ./requirements
                                // for i in *
                                // do
                                //     echo "-r requirements/$i"
                                // done > ../requirements.txt
                                // cd ..
                                // srcclr scan .
                                // rm ./requirements.txt

                            sh "curl -sSL https://download.sourceclear.com/ci.sh | sh"

                            // debug, no upload
                            //sh "curl -sSL https://download.sourceclear.com/ci.sh | DEBUG=1 sh -s -- scan --no-upload"
                        }
                    }
                }
            }
        }
    }
}
