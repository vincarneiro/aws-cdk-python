# CDK Pipeline Project
This project utilizes AWS Cloud Development Kit (CDK) to automate the deployment of AWS infrastructure components through a pipeline. It includes custom constructs, CDK stacks, and deployment stages configured to streamline the deployment process.

## File Structure
```sh
cdk-pipeline/
│
├── README.md                     # Project documentation
├── custom_constructs/            # Custom CDK constructs
│   └── vpc.py                    # Custom VPC construct
├── stacks/                       # CDK Stacks
│   ├── cdk_pipeline_stack.py     # Main CDK pipeline stack
│   └── s3_stack.py               # Example S3 stack
├── stages/                       # Deployment stages
│   └── deploy_stage.py           # Deployment stage configuration
├── tests/                        # Unit tests
│   └── unit/                     # Unit tests directory
├── .gitignore                    # Git ignore file
├── app.py                        # Main entry point for the CDK application
├── cdk.json                      # CDK configuration file
├── config.json                   # Configuration file (example)
├── requirements.txt              # Production dependencies
└── requirements-dev.txt          # Development dependencies
```

## Description
This project implements a CDK pipeline to automate AWS infrastructure deployments. It includes custom constructs like VPC configuration, various CDK stacks for different AWS resources, and deployment stages managed through AWS CDK.

## Key Components

#### app.py
This file is the main entry point for the CDK application. It initializes the CDK app and deploys the CdkPipelineStack, which sets up the entire pipeline infrastructure.

### custom_constructs/vpc.py
This custom construct defines a Virtual Private Cloud (VPC) with public, private, and isolated subnets.

### stacks/cdk_pipeline_stack.py
This file sets up a CodePipeline for continuous deployment using AWS CDK. It reads configurations from config.json to define pipeline stages for different environments.

### stacks/s3_stack.py
This demonstrates an example resource stack to be deployed by the pipeline

### Pipeline Stages
Defined in stages/ folder, each file represents one stage and define the resorces and constructs to be deployed.

# Using a Virtual Environment (.venv)
To set up and activate a virtual environment for this project:

### Create a Virtual Environment:

```
python3 -m venv .venv
```

This command creates a .venv directory in your project folder, which contains a self-contained Python environment.


### Activate the Virtual Environment:

On macOS/Linux:
```
source .venv/bin/activate
```

On Windows:
```
.venv\Scripts\activate
```

Activating the virtual environment changes your shell's PATH to use the Python interpreter and pip from the virtual environment (.venv). You should see (.venv) in your command prompt to indicate that the virtual environment is active.


### Install Project Dependencies:
After activating the virtual environment, install dependencies using pip:
```
pip install -r requirements.txt
```

This installs the required packages specified in requirements.txt into your virtual environment.


### Deactivate the Virtual Environment:
To deactivate the virtual environment and return to your global Python environment, simply run:
```
deactivate
```

This restores your shell's PATH to its default state.

Using a virtual environment ensures that project dependencies are managed independently of system-wide Python packages, promoting consistency and reproducibility across different environments.

## Configuration
Ensure config.json is properly configured with environment-specific details before deploying. AWS credentials must be set up correctly for deployment.

### Installation
To install dependencies, run:
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Usage
Deploy the CDK application using:
```
cdk deploy
```

Ensure to replace placeholders like AWS account details (account and region) in app.py with actual values.
