# Level 4 - Optimized: Quick Guide

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-02-27

----------

> Achieving Level 4 in the GenAIOps Maturity Model means you're at the top in managing large language models (LLMs). Here are some key points: <br/> 
> - **Advanced Automation**: Set up CI/CD pipelines, use containerization, and orchestrate for smooth model deployment. <br/> 
> - **Comprehensive Monitoring**: Leverage Azure Monitor and Log Analytics for detailed metrics and real-time alerts. <br/> 
> - **Sophisticated Model Management**: Utilize techniques like transfer learning, fine-tuning, and advanced prompt engineering. <br/> 
> - **Continuous Learning and Innovation**: Keep up with the latest LLM advancements and encourage a culture of experimentation. <br/> 
> - **Community Engagement**: Share best practices and contribute to the community to build thought leadership.

<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [Advance your maturity level for Generative Artificial Intelligence Operations (GenAIOps)](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/concept-llmops-maturity?view=azureml-api-2)
- [GenAIOps for MLOps practitioners](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/genaiops-for-mlops)
- [MLOps and GenAIOps for AI workloads on Azure](https://learn.microsoft.com/en-us/azure/well-architected/ai/mlops-genaiops)
- [Model catalog and collections in Azure AI Foundry portal](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/model-catalog-overview)
- [Evaluation of generative AI applications with Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/evaluation-approach-gen-ai)

</details>

## Content

## Implement Advanced Automation

| Category                        | Details                                                                 | When to Use                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Automation Tools**           | - **Azure Automation**: Automate routine tasks to reduce manual effort and minimize errors. Pros: improved efficiency, consistency, and the ability to schedule tasks or trigger them based on events.<br>- **Logic Apps**: Design workflows to integrate services and automate processes, enabling seamless data flow and reducing the need for manual intervention. Pros: enhanced productivity, streamlined operations, and easy integration with various services. `Low-Code/No-Code approach`.<br>- **Azure Functions**: Write serverless functions to handle specific tasks, allowing for scalable and event-driven execution. Pros: reduced infrastructure management, cost savings, and the ability to respond quickly to events. `Code-First approach.` | - **Azure Automation**: Use for automating administrative tasks, such as VM management, patching, and backup.<br>- **Logic Apps**: Use for orchestrating workflows that involve multiple services and require visual design and integration with various connectors. Ideal for users with less coding experience.<br>- **Azure Functions**: Use for executing small, discrete pieces of code in response to events, such as HTTP requests, timers, or messages from other services. Suitable for developers with coding experience. |
| **Orchestration**              | - **Azure Logic Apps**: Orchestrate complex workflows to ensure seamless integration between different services and processes. Pros: improved coordination, reduced operational complexity, and the ability to automate end-to-end processes. `Low-Code/No-Code approach`.<br>- **Azure Data Factory**: Use Data Factory for data integration and ETL processes, orchestrating data movement and transformation. Pros: efficient data processing, centralized data management, and the ability to handle large-scale data workflows. | - **Azure Logic Apps**: Use for orchestrating workflows that require integration with multiple services and connectors, especially when visual design is beneficial. Ideal for users with less coding experience.<br>- **Azure Data Factory**: Use for data integration and ETL processes, especially when dealing with large-scale data movement and transformation. |
| **Infrastructure as Code (IaC)** | - **ARM Templates**: Define infrastructure as code using JSON-based ARM templates, enabling consistent and repeatable deployments. Pros: version control, reduced configuration drift, and the ability to automate infrastructure provisioning. `Code-First approach.`<br>- **Terraform**: Use Terraform to write configuration files and deploy infrastructure, providing a unified approach to managing resources across multiple cloud providers. Pros: improved infrastructure management, scalability, and the ability to automate complex deployments. `Code-First approach.` | - **ARM Templates**: Use for Azure-specific infrastructure provisioning when you need tight integration with Azure services and features. Suitable for developers with coding experience.<br>- **Terraform**: Use for multi-cloud infrastructure provisioning and when you need a consistent approach across different cloud providers. Suitable for developers with coding experience. |

### Automation Tools

1. **Create an Automation Account**: In the Azure portal, search for `Automation Accounts` and create a new account.
2. **Runbooks**: Develop runbooks to automate routine tasks. Use PowerShell or Python scripts to define the automation logic.
3. **Schedules and Webhooks**: Schedule runbooks to run at specific times or trigger them via webhooks for event-driven automation.

####  Create an Automation Account

1. **Sign in to Azure Portal**: Go to the [Azure portal](https://portal.azure.com) and sign in with your Azure account credentials.
2. **Search for Automation Accounts**: In the search bar at the top of the Azure portal, type `Automation Accounts` and select it from the search results.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/903189dc-3cd5-4ada-855c-a25edca93163" />

3. **Create a New Automation Account**:
   - Click on the `+ Create` button to start the creation process.
   - Fill in the required fields:
     - **Subscription**: Select the Azure subscription you want to use.
     - **Resource Group**: Choose an existing resource group or create a new one.
     - **Name**: Provide a unique name for your Automation Account.
     - **Region**: Select the region where you want to create the Automation Account.
   - Click `Review + Create` and then `Create` to finalize the creation.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/e41d8168-31b6-4c46-ad78-18522efcc2cd" />

#### Develop Runbooks

1. **Navigate to Your Automation Account**: After the Automation Account is created, navigate to it by selecting it from the list of Automation Accounts.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/2b60bef5-eb3c-4fb7-bbc7-9f924b07435a" />

2. **Create a Runbook**:
   - In the Automation Account menu, select `Runbooks` under the `Process Automation` section.
   - Click on `+ Create a runbook` to start the creation process.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/4d57222b-0929-47cf-a7b0-f59ea82e9a2f" />

   - Fill in the required fields:
     - **Name**: Provide a name for your runbook.
     - **Runbook Type**: Select the type of runbook (e.g., PowerShell, Python).
     - **Description**: Optionally, add a description for your runbook.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/93d715ba-d883-465b-afc6-0d3ee1ac1b9c" />

   - Click `Create` to create the runbook. For example:

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/d453d39d-06c6-4732-aa3f-53dd6825d1e4" />

3. **Edit the Runbook**:
   - After creating the runbook, you will be taken to the runbook editor.
   - Write your automation logic using PowerShell or Python scripts.
      > For example: Click [here to review all code](./src/update_vm_and_python_libraries.py)

          ```python
          import os
          from azure.identity import DefaultAzureCredential
          from azure.mgmt.compute import ComputeManagementClient
          import subprocess
          
          # Parameters
          resource_group_name = os.environ.get("ResourceGroupName")
          vm_name = os.environ.get("VMName")
          
          # Authenticate
          credential = DefaultAzureCredential()
          compute_client = ComputeManagementClient(credential, os.environ.get("AZURE_SUBSCRIPTION_ID"))
          
          # Function to check VM status
          def get_vm_status(resource_group_name, vm_name):
              vm = compute_client.virtual_machines.get(resource_group_name, vm_name, expand='instanceView')
              statuses = vm.instance_view.statuses
              for status in statuses:
                  if 'PowerState' in status.code:
                      return status.code.split('/')[-1]
              return None
          
          # Check VM status
          vm_status = get_vm_status(resource_group_name, vm_name)
          print(f"Current VM status: {vm_status}")
          
          # Start VM if it's not running
          if vm_status != 'running':
              print(f"Starting VM: {vm_name} in resource group: {resource_group_name}")
              async_vm_start = compute_client.virtual_machines.begin_start(resource_group_name, vm_name)
              async_vm_start.result()
              print(f"Started VM: {vm_name} in resource group: {resource_group_name}")
          else:
              print(f"VM: {vm_name} is already running in resource group: {resource_group_name}")
          
          # Update Python core libraries
          def update_python_libraries():
              try:
                  subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
                  subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "setuptools"])
                  subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "wheel"])
                  print("Python core libraries updated successfully.")
              except subprocess.CalledProcessError as e:
                  print(f"Error updating Python libraries: {e}")
          
          # Update libraries
          update_python_libraries()
          ```

        > Another example, a simple PowerShell script to start a VM might:
             ```powershell
             param(
                 [string]$ResourceGroupName,
                 [string]$VMName
             )
        
             Start-AzVM -ResourceGroupName $ResourceGroupName -Name $VMName
             ```
   - Click `Save` to save your script.

4. **Publish the Runbook**: After saving the runbook, click `Publish` to make it available for execution.


- **Logic Apps**:
   1. **Create a Logic App**: In the Azure portal, search for `Logic Apps` and create a new logic app.
   2. **Design Workflows**: Use the visual designer to create workflows that integrate various services and automate processes.
   3. **Connectors**: Utilize built-in connectors to integrate with Azure services, third-party applications, and on-premises systems.

- **Azure Functions**:
   1. **Create a Function App**: In the Azure portal, search for `Function Apps` and create a new function app.
   2. **Develop Functions**: Write serverless functions in languages like C#, JavaScript, or Python to handle specific tasks.
   3. **Triggers and Bindings**: Configure triggers to execute functions based on events and bindings to connect to other services.

### Orchestration

- **Azure Logic Apps**: Use Logic Apps to orchestrate complex workflows, ensuring seamless integration between different services and processes.
- **Azure Data Factory**: For data integration and ETL processes, use Azure Data Factory to orchestrate data movement and transformation.

### Infrastructure as Code (IaC)

- **Azure Resource Manager (ARM) Templates**:
   1. **Create ARM Templates**: Define your infrastructure as code using JSON-based ARM templates.
   2. **Deploy Templates**: Use the Azure portal, Azure CLI, or PowerShell to deploy ARM templates and provision resources.

- **Terraform**:
   1. **Install Terraform**: Set up Terraform on your local machine or CI/CD pipeline.
   2. **Write Configuration Files**: Define your infrastructure using HCL (HashiCorp Configuration Language).
   3. **Deploy Infrastructure**: Use Terraform commands to plan and apply your infrastructure changes.

## Continuous Improvement Practices

### Regular Reviews

- **Performance Reviews**: Conduct regular reviews of LLM performance metrics to identify areas for improvement.
- **Operational Reviews**: Evaluate operational processes and workflows to streamline and optimize them.

### Feedback Loops

- **User Feedback**: Collect feedback from users and stakeholders to understand their needs and experiences.
- **Iterative Improvements**: Use the feedback to make iterative improvements to your LLM operations and applications.

### A/B Testing

- **Set Up A/B Tests**: Implement A/B testing to compare different versions of models or prompts.
- **Analyze Results**: Evaluate the results of A/B tests to determine the most effective configurations and make data-driven decisions.

## Leverage Cutting-Edge Tools and Techniques

### Latest Azure AI Services

> Azure AI Foundry Model Catalog

1. **Explore Models**: Use the [Azure AI Foundry Model Catalog](https://ai.azure.com/explore/models) to discover and evaluate a wide range of models from providers like OpenAI, Meta, NVIDIA, and Hugging Face.
2. **Model Deployment**: Deploy models directly from the catalog to Azure services, ensuring seamless integration and scalability.

### Advanced Analytics

- **Azure Synapse Analytics**:
   1. **Set Up Synapse Workspace**: Create a Synapse workspace in the Azure portal.
   2. **Data Integration**: Integrate data from various sources for comprehensive analysis.
   3. **Analytics and Visualization**: Use Synapse Studio to perform advanced analytics and visualize data insights.

- **Power BI**:
   1. **Create Power BI Reports**: Develop interactive reports and dashboards to visualize LLM performance and usage patterns.
   2. **Data Connectivity**: Connect Power BI to Azure data sources for real-time insights.

### Machine Learning Operations (MLOps)

1. **Set Up MLOps Pipelines**: Use Azure Machine Learning to create CI/CD pipelines for model deployment and monitoring.
2. **Model Monitoring**: Implement monitoring solutions to track model performance and detect anomalies.
3. **Continuous Delivery**: Automate the deployment of new model versions and updates.

## Evaluation of GenAI Applications

### Base Model Selection

- **Model Comparison**: Compare different models by testing their outputs against criteria relevant to your application. Consider accuracy, performance, and ethical considerations.

### Pre-production Evaluation

- **Evaluation Data**: Use your own evaluation data to test AI applications in pre-production. Utilize Azure AI Foundry or Azure AI Evaluation SDK’s supported evaluators.
- **Quality and Safety**: Assess generation quality, safety, and custom evaluators to ensure the application meets desired standards.

### Post-production Monitoring

- **Ongoing Evaluation**: Continuously monitor AI applications in production to ensure they maintain performance and compliance standards.
- **Feedback Integration**: Incorporate feedback from real-world usage to refine and improve the applications.



<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
