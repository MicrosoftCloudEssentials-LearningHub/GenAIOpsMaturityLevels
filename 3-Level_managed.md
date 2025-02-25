# Level 3 - Managed: Quick Guide

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-02-19

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

</details>

## Enhance Monitoring and Logging

> [!IMPORTANT]
> The cost of your workspace depends on how much data you bring in and how long you keep it. You can find regional pricing details on the [Azure Monitor pricing page](https://azure.microsoft.com/en-us/pricing/details/monitor/). You can switch to another pricing tier after setting up your workspace. Learn more about [Log Analytics pricing models](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs#pricing-model).

| Before any maturity implementation | After | 
| --- | --- | 
| <img width="550" alt="image" src="https://github.com/user-attachments/assets/dd44dc11-0f84-42f8-a451-f45a8cede608" /> | <img width="550" alt="image" src="https://github.com/user-attachments/assets/57599fb3-2f0e-4293-8f24-c8e4d1bcfe29" /> | 

### Use Azure Monitor and Log Analytics for comprehensive monitoring

- **Create a Log Analytics Workspace**:
     1. **Navigate to Log Analytics**: In the [Azure portal](https://portal.azure.com), search for `Log Analytics` and select `Create`.

        <div align="center">
          <img src="https://github.com/user-attachments/assets/1e801dfc-b679-49f7-b6cd-7c4fe37114da" alt="Centered Image" style="border: 2px solid #4CAF50;  border-radius: 5px; padding: 5px;";  width="750" />
        </div>

     2. **Configure Workspace**: Choose your subscription, create or select a Resource Group, provide a name for the workspace, select a region, and click `Review + Create`.

        <div align="center">
          <img src="https://github.com/user-attachments/assets/901eb973-71c0-4dd1-88c3-e7e420f05d3d" alt="Centered Image" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"; width="750"/>
        </div>

- **Configure Data Collection**:
     1. **Set Up Diagnostic Settings**: Navigate to the resource you want to monitor, select `Diagnostic settings`, and configure it to send logs and metrics to your Log Analytics workspace.
     2. **Enable Monitoring**: Use Azure Monitor to enable monitoring for your resources, ensuring comprehensive data collection.
- **Write and Run Queries**:
     1. **Log Analytics Interface**: Open Log Analytics from the Azure Monitor menu, and use the query window to write and run Kusto Query Language (KQL) queries.
     2. **Example Queries**: Utilize example queries provided in the Log Analytics interface to learn and customize your own queries.

### Set up alerts and dashboards for real-time insights

- **Create Alerts**:
     1. **Define Alert Rules**: In Azure Monitor, select `Alerts` and then `New alert rule`. Define the scope, condition, and action group for the alert.
     2. **Configure Notifications**: Set up notifications to receive alerts via email, SMS, or other channels.
- **Create Dashboards**:
     1. **Custom Dashboards**: Use Azure Monitor to create custom dashboards. Add visualizations for key metrics and log query results.
     2. **Share Dashboards**: Share dashboards with your team for collaborative monitoring and real-time insights.

## Ensure Compliance

### Adhere to best practices and compliance standards

- **Define Policies**:
     1. **Create Policies**: Use Azure Policy to define and assign policies that enforce compliance. Create policies for resource configurations, tagging, and security standards.
     2. **Assign Policies**: Assign policies to your resources to ensure they adhere to compliance standards.

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






<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
