# Level 4 - Optimized: Machine Learning Operations (MLOps)

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-03-10

----------

<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [Set up MLOps with Azure DevOps - Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-azureml?view=azureml-api-2)
- [Set up MLOps with GitHub - Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-mlops-github-azure-ml?view=azureml-api-2)
- [Model monitoring in production - Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-monitoring?view=azureml-api-2)
- [Safe rollout for online endpoints - Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-safely-rollout-online-endpoints?view=azureml-api-2)

</details>


## Content 

- [Set Up Azure DevOps or GitHub Actions](#set-up-azure-devops-or-github-actions)
- [Define CI/CD Pipelines](#define-cicd-pipelines)
- [Model Monitoring](#model-monitoring)
    - [Set Up Model Monitoring](#set-up-model-monitoring)
    - [Define Monitoring Metrics](#define-monitoring-metrics)
    - [Set Up Alerts](#set-up-alerts)
- [Continuous Delivery](#continuous-delivery)
    - [Register the Model](#register-the-model)
    - [Create Deployment Pipelines](#create-deployment-pipelines)
    - [Blue-Green Deployment Strategy](#blue-green-deployment-strategy)


## Set Up MLOps Pipelines

> Use Azure Machine Learning to create CI/CD pipelines for model deployment and monitoring.

### Create an Azure Machine Learning Workspace

- Sign in to the [Azure portal](https://portal.azure.com/).
- In the search bar, type `Machine Learning` and select `Azure Machine Learning`.
- Click on `+ Create` to create a new workspace.

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/38e7e18c-76d7-45a4-8ea5-082e9f210b5c" />

- Fill in the required fields: Subscription, Resource Group, Workspace Name, and Region.
- Click `Review + Create` and then `Create` to finalize the creation.

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/14d86b9c-4a20-4078-91ee-f2811915735d" />

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/45cf16d3-d3e2-4d1e-a142-97cfe13a0324" />

### Set Up Azure DevOps or GitHub Actions

- **Azure DevOps**:
  - Create a new project in Azure DevOps.
  - Set up a repository to store your code and configuration files.
  - Create service connections to authenticate with Azure Machine Learning.
  - Define pipelines using YAML files to automate the build, training, and deployment processes.
- **GitHub Actions**:
  - Create a new repository in GitHub.
  - Set up GitHub Actions workflows to automate the build, training, and deployment processes.
  - Use the `azure/login` action to authenticate with Azure.

### Define CI/CD Pipelines

- **Build Pipeline**: Automate the process of building and packaging your machine learning model.
- **Training Pipeline**: Automate the training of your model using Azure Machine Learning compute resources.
- **Deployment Pipeline**: Automate the deployment of your model to Azure Machine Learning endpoints.

> Example YAML Configuration: 

```yaml
trigger:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.x'
      addToPath: true

  - script: |
      python -m venv .venv
      source .venv/bin/activate
      pip install -r requirements.txt
    displayName: 'Install dependencies'

  - script: |
      az ml job create --file training-job.yml
    displayName: 'Run training job'

  - script: |
      az ml model deploy --model-id mymodel:1 --endpoint-name myendpoint
    displayName: 'Deploy model'
```

## Model Monitoring

> Implement monitoring solutions to track model performance and detect anomalies.

### Set Up Model Monitoring

- In the Azure Machine Learning workspace, navigate to `Endpoints` and select the deployed model endpoint.
- Click on `Monitoring` to configure monitoring settings.

https://github.com/user-attachments/assets/64dc5bd6-1fff-40c2-9a30-7d5fe38b9850

### Define Monitoring Metrics

- **Performance Metrics**: Track metrics such as accuracy, precision, recall, and F1 score.
- **Data Drift**: Monitor changes in the input data distribution over time.
- **Model Drift**: Monitor changes in the model's predictions over time.

### Set Up Alerts

- Configure alerts to notify you when metrics exceed predefined thresholds.
- Use Azure Monitor and Azure Event Grid to set up and manage alerts.

> Example Monitoring Configuration:

```yaml
monitoring:
  metrics:
    - name: accuracy
      threshold: 0.9
    - name: data_drift
      threshold: 0.1
  alerts:
    - name: accuracy_alert
      condition: accuracy < 0.9
      action: email
    - name: data_drift_alert
      condition: data_drift > 0.1
      action: webhook
```

## Continuous Delivery

> Automate the deployment of new model versions and updates.

### Register the Model

- After training the model, register it in the Azure Machine Learning workspace.
- Use the Azure Machine Learning SDK or CLI to register the model.

    ```python
    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential

    ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace_name)
    model = ml_client.models.create_or_update(name="mymodel", path="model.pkl")
    ```

### Create Deployment Pipelines

- Define deployment pipelines to automate the deployment of new model versions.
- Use Azure DevOps or GitHub Actions to trigger the deployment pipeline when a new model version is registered.

### Blue-Green Deployment Strategy

- Implement a blue-green deployment strategy to minimize downtime and ensure a smooth transition between model versions.
- Deploy the new model version to a staging environment (blue) and gradually shift traffic from the production environment (green) to the staging environment.
- Monitor the performance of the new model version before fully switching to it.

> Example Deployment Script:

```python
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace_name)
endpoint = ml_client.online_endpoints.get(name="myendpoint")

# Deploy new model version
deployment = ml_client.online_deployments.create_or_update(
    name="blue",
    endpoint_name="myendpoint",
    model=model,
    instance_type="Standard_DS3_v2",
    instance_count=1
)

# Gradually shift traffic to the new deployment
endpoint.traffic["blue"] = 50
endpoint.traffic["green"] = 50
ml_client.online_endpoints.begin_create_or_update(endpoint)
```

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
