pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code...'
            }
        }
        stage('Setup Environment') {
            steps {
                bat 'pip install pandas scikit-learn joblib'
            }
        }
        stage('Train AI Model') {
            steps {
                bat 'python train_model.py'
            }
        }
        stage('SLA Guardian Check') {
            steps {
                script {
                    // Running the check on your REXX file
                    // returnStatus: true lets us capture the failure without crashing immediately
                    def exitCode = bat(script: 'python sla_guardian.py GOOD_UPDATE.cbl', returnStatus: true)

                    if (exitCode == 1) {
                        // We mark the build as failed, but the 'post' block will handle the email
                        error "⛔ SLA BREACH DETECTED: Prediction exceeded 100ms."
                    } else {
                        echo "✅ SLA CHECK PASSED."
                    }
                }
            }
        }
    }

    // --- NEW: EMAIL NOTIFICATION BLOCK ---
    post {
        failure {
            // This runs ONLY if the build fails (Red Bubble)
            mail to: 'hrushikeshsuryawanshi832@gmail.com', // <--- CHANGE THIS TO YOUR EMAIL
                 subject: "🚨 FAILED: SLA Guardian Alert - Build #${env.BUILD_NUMBER}",
                 body: """
                 The Static SLA Guardian detected a performance breach!
                 
                 --------------------------------------------------
                 PROJECT: ${env.JOB_NAME}
                 BUILD: #${env.BUILD_NUMBER}
                 STATUS: FAILED (SLA Breach)
                 --------------------------------------------------
                 
                 The AI predicted that your recent code changes will slow down the system 
                 beyond the allowed 100ms threshold.
                 
                 Please review the attached logs and optimize your SQL/Loops.
                 
                 Link to Logs: ${env.BUILD_URL}
                 """
        }
        success {
            // Optional: Send an email on success too
            echo 'Build Passed. No email sent.'
        }
    }
}