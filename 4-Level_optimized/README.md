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
- [What is Azure Logic Apps?](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-overview)
- [What is Azure Data Factory?](https://learn.microsoft.com/en-us/azure/data-factory/introduction)
- [Common scenarios, examples, tutorials, and walkthroughs for Azure Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-examples-and-scenarios)
- [Data Factory - Connector overview](https://learn.microsoft.com/en-us/fabric/data-factory/connector-overview)
- [What is Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
- [Resource access management in Azure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/get-started/how-azure-resource-manager-works)

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

####  Azure Automation: Create an Automation Account

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

#### Azure Automation: Develop Runbooks

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
      > For example [Start or Validate VM Status and Update Python Core Libraries](./src/update_vm_and_python_libraries.py)
      > or a simple PowerShell script to start a VM:
        ```powershell
        param(
            [string]$ResourceGroupName,
            [string]$VMName
        )
   
        Start-AzVM -ResourceGroupName $ResourceGroupName -Name $VMName
        ```
   - Click `Save` to save your script.
4. **Publish the Runbook**: After saving the runbook, click `Publish` to make it available for execution.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/a81f903e-ac6d-468f-9d78-6c3e1339d551" />


#### Azure Automation: Schedule Runbooks and Set Up Webhooks

1. **Schedule a Runbook**:
     - In the runbook's overview page, select `Schedules` under the `Resources` section.
     - Click on `+ Add a schedule` to create a new schedule.
     
          <img width="550" alt="image" src="https://github.com/user-attachments/assets/8567ffa2-4d7c-4e23-87f7-494a5a563b3a" />

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/7f81b0e2-84dc-4fd9-92d3-a90209c20512">

     - Fill in the required fields:
          - **Name**: Provide a name for the schedule.
          - **Description**: Optionally, add a description for the schedule.
          - **Start Time**: Set the start time for the schedule.
          - **Recurrence**: Choose the recurrence pattern (e.g., one-time, daily, weekly).
     - Click `Create` to create the schedule.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/255f8c15-c1d9-49a9-a344-e19c6d442235" />

     - Link the schedule to the runbook by selecting the schedule and clicking `OK`.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/0f7ddd74-b5c0-46e4-931f-b3832ae74535" />

2. **Set Up a Webhook**:
     - In the runbook's overview page, select `Webhooks` under the `Resources` section.
     - Click on `+ Add webhook` to create a new webhook.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/93c6c4ff-8e5a-4ebc-9fd4-fc91bdaed591" />

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/6017e040-58fd-4e9d-86c4-5af45d677533" />

   - Fill in the required fields:
     - **Name**: Provide a name for the webhook.
     - **Enabled**: Choose whether the webhook is enabled or disabled.
     - **Expiry Date**: Set an expiry date for the webhook.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/0c6e4d89-69a1-47fc-8f5e-1f5ca226e0f3" />

     - Click `Create` to create the webhook.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/ed36b99c-840d-44b5-881c-2dd0a4d40f88" />

   - Copy the webhook URL and use it to trigger the runbook from external systems or applications.
     

#### Logic Apps: Create a Logic App

> [!NOTE]
> Please create a logic app if you do not already have one or need a specific resource for this purpose. Click here to learn more about [Logic App hosting options](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-overview#create-and-deploy-to-different-environments)

1. **Sign in to Azure Portal**: Go to the [Azure portal](https://portal.azure.com/) and sign in with your Azure account credentials.
2. **Search for Logic Apps**: In the search bar at the top of the Azure portal, type `Logic Apps` and select it from the search results.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/7c740f24-85cc-4428-a5a9-f82cbd5f5a43" />

3. **Create a New Logic App**:
   - Click on the `+ Create` button to start the creation process.
   - Fill in the required fields:
     - **Subscription**: Select the Azure subscription you want to use.
     - **Resource Group**: Choose an existing resource group or create a new one.
     - **Logic App Name**: Provide a unique name for your Logic App.
     - **Region**: Select the region where you want to create the Logic App.
     - **Plan Type**: Choose between `Consumption` (pay-per-use) or `Standard` (fixed pricing).

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/2a2e298f-e6e7-4f2e-be3d-7b64d26114a4" />

   - Click `Review + Create` and then `Create` to finalize the creation.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/49438da5-9cfb-4f0d-b54b-00e4a7401253">

#### Logic Apps: Use Connectors

| Action                         | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| **Explore Built-in Connectors** | - Logic Apps provides a wide range of built-in connectors to integrate with various services, including Azure services, third-party applications, and on-premises systems.<br>- In the Logic App Designer, click on `+` and browse the list of connectors. |
| **Add Connectors to Your Workflow** | - Select the connector you want to use (e.g., `Office 365 Outlook`, `Azure Blob Storage`).<br>- Configure the connector by providing the necessary authentication details and parameters. |
| **Custom Connectors**        | - If a built-in connector is not available for your specific service, you can create a custom connector.<br>- In the Azure portal, search for `Custom connectors` and follow the steps to create and configure a custom connector. |

#### Logic Apps: Create Workflow

1. **Go to Your Logic App**: After the Logic App is created, navigate to it by selecting it from the list of Logic Apps.
2. **Create a workflow**: Under Workflows, click on `+ Add`:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/436d3843-8d23-4898-b9c8-def5c5579fec" />

3. The Logic App Designer provides a visual interface to create and manage workflows, for that click on workflow created:

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/d6e7720d-144b-491a-aeeb-f14e3794bb96" />

4. **Add a Trigger**:
     - Every Logic App workflow starts with a trigger. Click on `New step` and search for a trigger that suits your needs (e.g., `When a HTTP request is received`, `Recurrence` for scheduled workflows).

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/a9f92a5b-9a4f-47f2-9a77-ddc3e63a732b" />

     - Configure the trigger by providing the necessary details (e.g., URL, schedule).

5. **Add Actions**:
     - After adding a trigger, click on `+` to add actions to your workflow.
     
          <img width="550" alt="image" src="https://github.com/user-attachments/assets/2d25e5de-d7e1-4558-8e7b-b6bb388f86c2" />
     
     - Search for and select the actions you need (e.g., `Send an email`, `Create a file in OneDrive`).

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/06ed7e9f-3bf3-4e1e-910d-a37d11e7b2c4" />

     - Configure each action by providing the required parameters.

6. **Use Conditions and Loops**:
     - You can add conditions and loops to control the flow of your workflow.
     - Click on `+` and search for `Condition` to add conditional logic.
     - Search for `Apply to each` or `Until` to add loops.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/7d5d08a1-8c97-4bbb-8690-a95c5f060d07" />

7. **Save and Test the Workflow**:
   - After designing your workflow, click `Save` to save your changes.
   - Use the `Run Trigger` button to manually trigger the workflow and test its functionality.
   - Check the `Runs history` to see the execution details and troubleshoot any issues.

#### Function App: Create a Function App

1. **Sign in to Azure Portal**: Go to the [Azure portal](https://portal.azure.com/) and sign in with your Azure account credentials.
2. **Search for Function Apps**: In the search bar at the top of the Azure portal, type `Function Apps` and select it from the search results. Click here to learn more about [Functions hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale)

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/db60808f-dd64-43e6-a4e8-ab98c530a95a" />

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/d05be964-f594-4e83-a6ae-5bfd443bfd8d">

3. **Create a New Function App**:
     - Click on the `+ Create` button to start the creation process.
     - Fill in the required fields:
          - **Subscription**: Select the Azure subscription you want to use.
          - **Resource Group**: Choose an existing resource group or create a new one.
          - **Function App Name**: Provide a unique name for your Function App.
          - **Region**: Select the region where you want to create the Function App.
          - **Runtime Stack**: Choose the runtime stack for your functions (e.g., .NET, Node.js, Python).
          - **Version**: Select the version of the runtime stack.
          - **Operating System**: Choose the operating system (Windows or Linux).
          - **Plan Type**: Choose between `Consumption` (pay-per-use) or `Premium` (fixed pricing).
     - Click `Review + Create` and then `Create` to finalize the creation.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/d9c2ab80-80b2-45d9-a9e5-5e3f4203d955" />

### Orchestration

- **Azure Logic Apps**: Use Logic Apps to orchestrate complex workflows, ensuring seamless integration between different services and processes.

     > Example Workflow: <br/>
     > - Trigger: When a new email is received in Office 365 Outlook. <br/>
     > - Action: Save the email's attachments to a specific folder in OneDrive. <br/>
     > - Action: Send a notification to Microsoft Teams with the details of the email.

- **Azure Data Factory**: For data integration and ETL processes, use Azure Data Factory to orchestrate data movement and transformation.

     > - Example Pipeline: <br/> 
     > - Extract: Fetch data from an on-premises SQL Server database. <br/> 
     > - Transform: Clean and aggregate the data using data flows or compute services like Azure Databricks. <br/> 
     > - Load: Load the transformed data into an Azure SQL Data Warehouse for analysis.
     
> [!NOTE]
> If you are considering Azure Data Factory, please consider Microsoft Fabric. Click here to review an [essentials workshop about Microsoft Fabric](https://github.com/MicrosoftCloudEssentials-LearningHub/MS-Fabric-Essentials-Workshop).

### Infrastructure as Code (IaC)

#### Azure Resource Manager (ARM) Templates

<p align="center">
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/7d156f6f-0741-494b-8451-039ef4254be2">
</p>

From [Microsoft official documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Consistent Management Layer** | ARM provides a unified management layer for creating, updating, and deleting resources in Azure. It ensures consistent results across all Azure APIs, tools, and SDKs. |
| **Resource Groups**            | Logical containers that hold related resources for an Azure solution. Resources in a group can be managed collectively based on their lifecycle and security needs. |
| **Declarative Syntax**         | ARM templates and Bicep files use declarative syntax to define the infrastructure to deploy. This allows for consistent and repeatable deployments. |
| **Access Control and Security** | Use role-based access control (RBAC), locks, and tags to secure and organize resources. ARM ensures that only authorized users can manage resources. |
| **Resource Providers**         | Services that supply Azure resources, such as Microsoft.Compute for virtual machines and Microsoft.Storage for storage accounts. |
| **Infrastructure as Code (IaC)** | ARM supports IaC, enabling you to manage your infrastructure using code. This includes ARM templates and Bicep files for defining and deploying resources. |

> Steps: 

1. **Create ARM Templates**: Define your infrastructure as code using JSON-based ARM templates.
2. **Deploy Templates**: Use the Azure portal, Azure CLI, or PowerShell to deploy ARM templates and provision resources.

#### Terraform

> Recommended structure:

```
.
├── README.md
├── src
├────── main.tf
├────── variables.tf
├────── provider.tf
├────── terraform.tfvars
├────── remote-storage.tf
├────── outputs.tf
```

- main.tf `(Main Terraform configuration file)`: This file contains the core infrastructure code. It defines the resources you want to create, such as virtual machines, networks, and storage. It's the primary file where you describe your infrastructure in a declarative manner.
- variables.tf `(Variable definitions)`: This file is used to define variables that can be used throughout your Terraform configuration. By using variables, you can make your configuration more flexible and reusable. For example, you can define variables for resource names, sizes, and other parameters that might change between environments.
- provider.tf `(Provider configurations)`: Providers are plugins that Terraform uses to interact with cloud providers, SaaS providers, and other APIs. This file specifies which providers (e.g., AWS, Azure, Google Cloud) you are using and any necessary configuration for them, such as authentication details.
- terraform.tfvars `(Variable values)`: This file contains the actual values for the variables defined in `variables.tf`. By separating variable definitions and values, you can easily switch between different sets of values for different environments (e.g., development, staging, production) without changing the main configuration files.
- remote-storage.tf `(Remote state storage configuration)`: Terraform uses a state file to keep track of the resources it manages. This file configures remote state storage, which allows you to store the state file in a remote location (e.g., an S3 bucket, Azure Blob Storage). Remote state storage is crucial for collaboration and ensuring that the state file is not lost or corrupted.
- outputs.tf `(Output values)`: This file defines the output values that Terraform should return after applying the configuration. Outputs are useful for displaying information about the resources created, such as IP addresses, resource IDs, and other important details. They can also be used as inputs for other Terraform configurations or scripts.

```mermaid 
graph TD;
    A[az login] --> B(terraform init)
    B --> C{Terraform provisioning stage}
    C -->|Review| D[terraform plan]
    C -->|Order Now| E[terraform apply]
    C -->|Delete Resource if needed| F[terraform destroy]
```

> Steps:

1. **Install Terraform**: Set up Terraform on your local machine or CI/CD pipeline.
2. **Write Configuration Files**: Define your infrastructure using HCL (HashiCorp Configuration Language).
3. **Deploy Infrastructure**: Use Terraform commands to plan and apply your infrastructure changes.

> [!TIP]
> Click here to see [an example of deployment using Terraform and Azure RM](https://github.com/MicrosoftCloudEssentials-LearningHub/MS-Fabric-Essentials-Workshop/blob/main/Terraform/README.md).

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
