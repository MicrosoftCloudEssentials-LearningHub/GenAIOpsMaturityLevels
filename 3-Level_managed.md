# Level 3 - Managed: Quick Guide

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-17

----------

> At this maturity level, organizations have established `robust processes for managing large language models (LLMs)`.
> This includes comprehensive `monitoring, detailed logging, and performance optimization` to ensure efficient and reliable operations.


<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [Overview of Log Analytics in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)
- [Log Analytics tutorial - Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial)
- [Design a Log Analytics workspace architecture](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/workspace-design)
- [Optimize Checkpoint Performance for Large Models - Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/reference-checkpoint-performance-for-large-models?view=azureml-api-2)
- [Azure Policy compliance states](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/compliance-states)
- [Azure Policy documentation](https://learn.microsoft.com/en-us/azure/governance/policy/)
- [Analyze metrics with Azure Monitor metrics explorer](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/analyze-metrics#pin-charts-to-dashboards)
- [Tutorial: Build policies to enforce compliance - Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/create-and-manage)
- [Quickstart: Create policy assignment using Azure portal - Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/assign-policy-portal)
- [Tutorial: Create a custom policy definition - Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/create-custom-policy-definition)

</details>

## Content 

- [Content](#content)
- [Enhance Monitoring and Logging](#enhance-monitoring-and-logging)
   - [Use Azure Monitor and Log Analytics for comprehensive monitoring](#use-azure-monitor-and-log-analytics-for-comprehensive-monitoring)
   - [Set up alerts and dashboards for real-time insights](#set-up-alerts-and-dashboards-for-real-time-insights)
- [Ensure Compliance](#ensure-compliance)
   - [Adhere to best practices and compliance standards](#adhere-to-best-practices-and-compliance-standards)
       - [Create Policies](#create-policies)
       - [Assign Policies](#assign-policies)
   - [Use Azure Policy to enforce compliance rules](#use-azure-policy-to-enforce-compliance-rules)
- [Optimize Performance](#optimize-performance)
   - [Implement performance optimization techniques](#implement-performance-optimization-techniques)
   - [Use Azure Machine Learning for model training and fine-tuning](#use-azure-machine-learning-for-model-training-and-fine-tuning)



## Enhance Monitoring and Logging

> [!IMPORTANT]
> The cost of your workspace depends on how much data you bring in and how long you keep it. You can find regional pricing details on the [Azure Monitor pricing page](https://azure.microsoft.com/en-us/pricing/details/monitor/). You can switch to another pricing tier after setting up your workspace. Learn more about [Log Analytics pricing models](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs#pricing-model).

| Before  | After | 
| --- | --- | 
| <img width="550" alt="image" src="https://github.com/user-attachments/assets/dd44dc11-0f84-42f8-a451-f45a8cede608" /> | <img width="550" alt="image" src="https://github.com/user-attachments/assets/57599fb3-2f0e-4293-8f24-c8e4d1bcfe29" /> | 

### Use Azure Monitor and Log Analytics for comprehensive monitoring

- **Create a Log Analytics Workspace**:
     1. **Navigate to Log Analytics**: In the [Azure portal](https://portal.azure.com), search for `Log Analytics` and select `Create`.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/1e801dfc-b679-49f7-b6cd-7c4fe37114da" />

     2. **Configure Workspace**: Choose your subscription, create or select a Resource Group, provide a name for the workspace, select a region, and click `Review + Create`.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/901eb973-71c0-4dd1-88c3-e7e420f05d3d" />

- **Configure Data Collection**:
     1. **Set Up Diagnostic Settings**: Navigate to the resource you want to monitor, select `Diagnostic settings`, and configure it to send logs and metrics to your Log Analytics workspace.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/549c143e-fef3-4283-8a50-31787cd2f97f" />

        | Before configuration | Example of configuration |
        | ---- | ---- |
        | <img width="550" alt="image" src="https://github.com/user-attachments/assets/4f7c841b-4536-46cf-933d-6a9bfee86e9c" /> | <img width="550" alt="image" src="https://github.com/user-attachments/assets/b3dc58ce-95ed-4b3a-841c-5f943af1859d" /> |

     2. **Enable Monitoring**: Use Azure Monitor to enable monitoring for your resources, ensuring comprehensive data collection.
          1. Access Azure Monitor:
             - Log in to the [Azure Portal](https://portal.azure.com/).
             - In the left-hand menu, select `Monitor`.

                  <img width="550" alt="image" src="https://github.com/user-attachments/assets/6e9b5439-1803-4121-98b7-90ad0b95d6ed" />

                  <img width="550" alt="image" src="https://github.com/user-attachments/assets/247d81c7-5a1e-4bfa-b0de-e4d22d9f4b12" />

          2. Configure Data Collection:
             - Navigate to the `Settings` section and select `Data Collection Rules`.
             - Click on `+ Create` to set up a new data collection rule.

                  <img width="550" alt="image" src="https://github.com/user-attachments/assets/9abe3244-9cd9-4833-b590-a0d3c15a304f" />

             - Provide a name for the rule and select the subscription and resource group.
             - Choose the resources you want to monitor (e.g., Virtual Machines, Storage Accounts).

                  <img width="550" alt="image" src="https://github.com/user-attachments/assets/92b9c9b3-f244-42d6-b968-054be9dfc14e" />
                  
- **Write and Run Queries**:
     1. **Log Analytics Interface**: Open Log Analytics from the Azure Monitor menu, and use the query window to write and run Kusto Query Language (KQL) queries.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/16517b1b-5341-475b-996d-014a840f3bdb" />

     2. **Example Queries**: Utilize example queries provided in the Log Analytics interface to learn and customize your own queries.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/16517b1b-5341-475b-996d-014a840f3bdb" />

### Set up alerts and dashboards for real-time insights

| Before  | After | 
| --- | --- | 
| <img width="550" alt="image" src="https://github.com/user-attachments/assets/57599fb3-2f0e-4293-8f24-c8e4d1bcfe29" />  | <img width="550" alt="image" src="https://github.com/user-attachments/assets/8bf9fde7-9909-4af9-8e8e-f25376e1db96" /> | 

- **Create Alerts**:
     1. **Define Alert Rules**:

        - In Azure Monitor, select `Alerts` and then `New alert rule`:

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/8e9d7783-8121-408c-8266-d0f804814e88" />

        - Define the scope: 

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/73115fa4-1156-485f-9f60-1cacdc045730" />

        - Define the condition for the alert:

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/70154f53-9d47-4856-9c1e-aabf837a9a6b" />

        - Define the action group for the alert:

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/d65cc881-b328-41d8-869a-13983d57b8e1">

     3. **Configure Notifications**: Set up notifications to receive alerts via email, SMS, or other channels.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/8baf2d53-ef5f-4f80-8408-c121481aa87e" />

- **Create Dashboards**:
     1. **Custom Dashboards**: Use Azure Monitor to create custom dashboards. Add visualizations for key metrics and log query results.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/44bb41d7-6b63-4c41-bae1-931567639c75" />

     2. **Share Dashboards**: Share dashboards with your team for collaborative monitoring and real-time insights.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/429a006e-fdaa-4c0c-ba93-8d9348929161" />

## Ensure Compliance

### Adhere to best practices and compliance standards

#### Create Policies
 
 | **Policy Component**  | **Description**                                                                                   |
 |-----------------------|---------------------------------------------------------------------------------------------------|
 | **Azure Policy**      | Use Azure Policy to create policies that enforce compliance across your resources. Policies can be defined for various aspects such as resource configurations, tagging, and security standards.  |
 | **Policy Definitions**| Write policy definitions that specify the desired state of your resources. For example, you can create a policy to ensure all resources have specific tags or that certain configurations are enforced. |
 | **Policy Initiatives**| Group multiple policies into initiatives to manage them as a single unit. This is useful for enforcing a set of related policies across your environment.    |

- **Azure Policy**:
     1. Sign in to the [Azure portal](https://portal.azure.com/).
     2. In the search bar, type `Policy` and select `Policy` from the results.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/8dd5008a-56b4-4ffd-98fe-c5c4149d9f2a" />

- **Policy Definitions**: Create a policy definition.
     
     1. In the Azure Policy dashboard, select `Definitions` from the left-hand menu.
     2. Click on `+ Policy definition` to create a new policy.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/7e03407e-4074-432e-8d41-72c6a157b7a9" />

     3. Fill in the required fields:
          - **Definition location**: Select the scope (management group or subscription) where the policy will be available.
          - **Name**: Provide a name for the policy.
          - **Description**: Add a description to explain the purpose of the policy.
          - **Category**: Choose a category or create a new one.

               <img width="550" alt="image" src="https://github.com/user-attachments/assets/f0a3c647-05de-41ac-8af1-48cff361fdc2" />

     4. In the `Policy rule` section, define the policy rule using JSON. For example, to ensure all resources have a specific tag:

          ```json
          {
           "if": {
             "field": "[resourceType]",
             "equals": "Microsoft.Resources/subscriptions/resourceGroups"
           },
           "then": {
             "effect": "append",
             "details": {
               "field": "tags",
               "value": {
                 "Environment": "Production"
               }
             }
           }
          }
          ```
        
        <img width="550" alt="image" src="https://github.com/user-attachments/assets/2374221b-484e-41f7-95b2-e193c9322931" />

     5. Click `Save` to create the policy definition.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/d787c6a9-f49c-4bb9-93df-5d59a079bfcc" />

-  **Policy Initiatives**: Create a policy initiative.
      1. In the Azure Policy dashboard, select `Initiatives` from the left-hand menu.
      2. Click on `+ Initiative definition` to create a new initiative.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/4d209c8a-e368-4550-a969-b7f06a7af465" />

      3. Fill in the required fields:
         - **Definition location**: Select the scope (management group or subscription) where the initiative will be available.
         - **Name**: Provide a name for the initiative.
         - **Description**: Add a description to explain the purpose of the initiative.
         - **Category**: Choose a category or create a new one.

              <img width="550" alt="image" src="https://github.com/user-attachments/assets/96156e08-5a6b-4b88-9abe-6df842aff392" />

      4. Add policies to the initiative by selecting `Add policy` and choosing the relevant policy definitions.

         <img width="550" alt="image" src="https://github.com/user-attachments/assets/ab4d17cc-e1a4-49ac-aadd-8dfdea6e615e" />

      5. Click `Create` to create the initiative.
         

#### Assign Policies
       
| **Assignment Component**       | **Description**                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------------------|
| **Scope Assignment**          | Assign policies to specific scopes such as subscriptions, resource groups, or individual resources. This ensures that the policies are applied to the relevant resources.  |
| **Policy Assignment Parameters**| Configure parameters for policy assignments to customize their behavior. For example, you can specify which tags should be enforced or which configurations should be checked. |

- **Scope Assignment**: Assign a policy.
     1. In the Azure Policy dashboard, select `Assignments` from the left-hand menu.
     2. Click on `+ Assign policy` to create a new policy assignment.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/159fd69a-bef0-47ef-99c2-a8576538e9af" />

     3. Fill in the required fields:
          - **Scope**: Select the scope (management group, subscription, or resource group) where the policy will be enforced.
          - **Policy definition**: Choose the policy definition you created earlier.
          - **Assignment name**: Provide a name for the policy assignment.
     4. Optionally, configure exclusions to exclude specific resources from the policy.
     5. Click `Next` to configure parameters.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/b242e0bc-ecd6-402e-9413-ed99963d64e4" />

- Policy assignment parameters: Configure parameters.
   1. If the policy definition includes parameters, configure them as needed. For example, specify the tag key and value to be enforced.
   2. Click `Next` to review and create the policy assignment.
   3. Click `Create` to finalize the policy assignment.
    
   https://github.com/user-attachments/assets/5a0a7ac5-db43-4751-af84-e99ffbb3c072



### Use Azure Policy to enforce compliance rules

- **Evaluate Compliance**:
     1. **Compliance Dashboard**: Regularly evaluate the compliance state of your resources using the Azure Policy compliance dashboard.
     2. **Compliance States**: Understand the different compliance states (compliant, non-compliant, error, conflicting, exempt) and take appropriate actions.
- **Remediate Non-compliant Resources**:
     1. **Remediation Tasks**: Set up remediation tasks to automatically correct non-compliant resources. Use deployIfNotExists and modify policies to enforce compliance.
     2. **Manual Remediation**: For resources that cannot be automatically remediated, perform manual remediation to ensure compliance.

## Optimize Performance

### Implement performance optimization techniques

- **Choose Appropriate VM SKUs**:
     1. **Select VM SKU**: Choose the best VM SKU for your ML service based on CPU, memory, and network requirements. Consider using GPU SKUs for intensive ML workloads.
     2. **Understand VM Configurations**: Pay attention to CPU type, memory size, disk type, and network bandwidth when selecting a VM.
- **Autoscaling**:
     1. **Configure Autoscaling**: Set up autoscaling for training clusters and managed online endpoints using Azure Machine Learning. This ensures resources scale based on workload demands.

### Use Azure Machine Learning for model training and fine-tuning
- **Model Training**:
     1. **Train Models**: Use Azure Machine Learning to train your models with optimized configurations. Implement parallel training and hyperparameter tuning to improve model performance.
     2. **Checkpointing**: Use Nebula with ACPT on Azure Machine Learning to quickly checkpoint your model training jobs.
- **Model Deployment**:
     1. **Deploy Models**: Deploy models using Azure Machine Learning endpoints. Monitor and optimize the deployed models for latency and throughput.

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-18-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-17</p>
</div>
<!-- END BADGE -->
