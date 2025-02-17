pipeline
{ 
    agent any
    stages
    {
        stage("checkout scm"){
            steps{
                checkout scm          
            }            
        }
        stage("Execute grafana"){
            steps{
                sh "sudo ansible-playbook roles/prometheus.yml"
                
            }            
        }
    }
}
