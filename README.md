# Assignment1-Devops-2024tm93287
Assignment 1 of DevOps

# Software requirements
Install Python SDK

# Steps to Run Application locally
- Follow the below commands step by step to run the application locally
  - **Step 1:** Create and activate virtual environment: `python -m venv .venv and ..venv\Scripts\activate` 
  - **Step 2:** Install dependencies: `pip install -r requirements.txt`
  - **Step 3:** Start the Flask server: `python -m app.app`
- please refer to the postman collection file for testing

# Steps to execute the tests locally
- Ensure that you have Python and Flask installed in the environment
- use the command `python -m pytest`

# Brief Overview of GitHub Actions
- **Triggers**: Every git push to the repository
- **Steps**:
  - **Build** - Creates Docker image with Flask app and dependencies
  - **Test** - Runs pytest unit tests inside Docker container
  - **Validate** - Builds production-ready runtime image
- **Purpose**: Ensures code quality by automatically testing every change before integration
- **Success**: Green status in Actions tab means all tests pass and code is deployment-ready

