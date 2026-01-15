pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // In a real project, this pulls from GitHub.
                // For this local POC, we just print a message.
                echo 'Checking out code from repository...'
            }
        }

        stage('Setup Environment') {
            steps {
                // Install necessary Python libraries
                // Using 'bat' because you are on Windows
                bat 'pip install pandas scikit-learn joblib'
            }
        }

        stage('Train AI Model') {
            steps {
                // Train the model freshly for every build (for POC purposes)
                echo 'Training the prediction model...'
                bat 'python train_model.py'
            }
        }

        stage('SLA Guardian Check') {
            steps {
                script {
                    // This tries to run the Guardian on the BAD file first.
                    // You can change 'BAD_UPDATE.cbl' to 'GOOD_UPDATE.cbl' to see it pass.
                    echo 'Running Static SLA Analysis...'
                    
                    // The 'returnStatus: true' allows us to capture the failure 
                    // without crashing the pipeline immediately, so we can print a custom message.
                    def exitCode = bat(script: 'python sla_guardian.py HEAVY_JOB.rexx', returnStatus: true)

                    if (exitCode == 1) {
                        error "BUILD FAILED: SLA Guardian detected a performance breach."
                    } else {
                        echo "SLA CHECK PASSED: Code is safe to merge."
                    }
                }
            }
        }
    }
}