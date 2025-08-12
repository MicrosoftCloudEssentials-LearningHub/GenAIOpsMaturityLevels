# Level 4 - Optimized: Quick Guide

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-17

----------

> Achieving Level 4 in the GenAIOps Maturity Model means you're at the top in managing large language models (LLMs). Here are some key points: <br/> 
> - **Advanced Automation**: Set up CI/CD pipelines, use containerization, and orchestrate for smooth model deployment. <br/> 
> - **Comprehensive Monitoring**: Leverage Azure Monitor and Log Analytics for detailed metrics and real-time alerts. <br/> 
> - **Sophisticated Model Management**: Utilize techniques like transfer learning (is a technique that allows models to apply previously acquired knowledge to new, related tasks), fine-tuning, and advanced prompt engineering. <br/> 
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
- [Towards Inclusive Software Engineering Through - A/B Testing: A Case-Study at Windows](https://www.microsoft.com/en-us/research/uploads/prod/2021/02/AB_Testing_For_Inclusive_and_Equitable_Engineering.pdf)
- [Implement A/B testing and progressive exposure deployment](https://learn.microsoft.com/en-us/training/modules/implement-test-progressive-exposure-deployment/)
- [Quickstart: Create an Azure Synapse Analytics workspace](https://learn.microsoft.com/en-us/azure/synapse-analytics/quickstart-create-workspace)
- [Tutorial: Analyze Azure Open Datasets in Synapse Studio](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/tutorial-data-analyst)
- [Visualize data with Apache Spark - Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/spark/apache-spark-data-visualization-tutorial)
- [Connect to cloud data sources in the Power BI service](https://learn.microsoft.com/en-us/power-bi/connect-data/service-connect-cloud-data-sources)
- [Azure and Power BI](https://learn.microsoft.com/en-us/power-bi/connect-data/service-azure-and-power-bi)
- [Load data into Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/data-factory/load-azure-sql-data-warehouse)

</details>

## Content

- [Content](#content)
- [Implement Advanced Automation](#implement-advanced-automation)
- [Continuous Improvement Practices](#continuous-improvement-practices)
- [Leverage Cutting-Edge Tools and Techniques](#leverage-cutting-edge-tools-and-techniques)
    - [Latest Azure AI Services](#latest-azure-ai-services)
    - [Advanced Analytics](#advanced-analytics)
    - [Machine Learning Operations MLOps](#machine-learning-operations-mlops)
- [Evaluation of GenAI Applications](#evaluation-of-genai-applications)
    - [Base Model Selection](#base-model-selection)
    - [Pre-production Evaluation](#pre-production-evaluation)
    - [Post-production Monitoring](#post-production-monitoring)

## Implement Advanced Automation

| Category                        | Details                                                                 | When to Use                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Automation Tools**           | - **Azure Automation**: Automate routine tasks to reduce manual effort and minimize errors. Pros: improved efficiency, consistency, and the ability to schedule tasks or trigger them based on events.<br>- **Logic Apps**: Design workflows to integrate services and automate processes, enabling seamless data flow and reducing the need for manual intervention. Pros: enhanced productivity, streamlined operations, and easy integration with various services. `Low-Code/No-Code approach`.<br>- **Azure Functions**: Write serverless functions to handle specific tasks, allowing for scalable and event-driven execution. Pros: reduced infrastructure management, cost savings, and the ability to respond quickly to events. `Code-First approach.` | - **Azure Automation**: Use for automating administrative tasks, such as VM management, patching, and backup.<br>- **Logic Apps**: Use for orchestrating workflows that involve multiple services and require visual design and integration with various connectors. Ideal for users with less coding experience.<br>- **Azure Functions**: Use for executing small, discrete pieces of code in response to events, such as HTTP requests, timers, or messages from other services. Suitable for developers with coding experience. |
| **Orchestration**              | - **Azure Logic Apps**: Orchestrate complex workflows to ensure seamless integration between different services and processes. Pros: improved coordination, reduced operational complexity, and the ability to automate end-to-end processes. `Low-Code/No-Code approach`.<br>- **Azure Data Factory**: Use Data Factory for data integration and ETL processes, orchestrating data movement and transformation. Pros: efficient data processing, centralized data management, and the ability to handle large-scale data workflows. | - **Azure Logic Apps**: Use for orchestrating workflows that require integration with multiple services and connectors, especially when visual design is beneficial. Ideal for users with less coding experience.<br>- **Azure Data Factory**: Use for data integration and ETL processes, especially when dealing with large-scale data movement and transformation. |
| **Infrastructure as Code (IaC)** | - **ARM Templates**: Define infrastructure as code using JSON-based ARM templates, enabling consistent and repeatable deployments. Pros: version control, reduced configuration drift, and the ability to automate infrastructure provisioning. `Code-First approach.`<br>- **Terraform**: Use Terraform to write configuration files and deploy infrastructure, providing a unified approach to managing resources across multiple cloud providers. Pros: improved infrastructure management, scalability, and the ability to automate complex deployments. `Code-First approach.` | - **ARM Templates**: Use for Azure-specific infrastructure provisioning when you need tight integration with Azure services and features. Suitable for developers with coding experience.<br>- **Terraform**: Use for multi-cloud infrastructure provisioning and when you need a consistent approach across different cloud providers. Suitable for developers with coding experience. |

Click here to [read more about Implement Advanced Automation](./0_ImplementAdvancedAutomation.md)

## Continuous Improvement Practices

| Practice                  | Description                                                                 | Steps                                                                                          | Examples in Microsoft Ecosystem                                                                 |
|---------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Regular Reviews**       | Conduct regular reviews of LLM performance metrics and operational processes to identify areas for improvement. | - **Performance Reviews**: Assess accuracy, latency, error rates, and user engagement.<br>- **Operational Reviews**: Evaluate deployment pipelines, resource utilization, and incident management. | - **Azure Application Insights**: Use to collect and analyze performance metrics.<br>- **Azure DevOps**: Use to manage and review deployment pipelines. |
| **Feedback Loops**        | Collect and use feedback from users and stakeholders to make iterative improvements. | - **User Feedback**: Gather insights through surveys, interviews, and feedback forms.<br>- **Iterative Improvements**: Analyze feedback, prioritize improvements, implement changes, and monitor impact. | - **Microsoft Forms**: Use to create and distribute surveys.<br>- **UserVoice**: Implement to collect and manage user feedback. |
| **A/B Testing**           | Implement A/B testing `(A/B testing, also known as split testing, is a method of comparing two versions of a product, service, or idea to determine which performs better. It involves randomly assigning users to different variants (A and B) and measuring their performance based on predefined metrics. This helps in making data-driven decisions and optimizing performance)` to compare different versions of models or prompts and make data-driven decisions. | - **Set Up A/B Tests**: Define variants, randomly assign users, and measure performance metrics.<br>- **Analyze Results**: Collect data, perform statistical analysis, and decide on the best variant. | - **Azure Machine Learning**: Use to set up and manage A/B tests.<br>- **Power BI**: Use to visualize and analyze A/B test results. | 

## Leverage Cutting-Edge Tools and Techniques

### Latest Azure AI Services

> [Azure AI Foundry Model Catalog](https://ai.azure.com/explore/models)

| Action                         | Description                                                                 | Details                                                                                          |
|------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Explore Models**           | Use the Azure AI Foundry Model Catalog to discover and evaluate a wide range of models from various providers. | - **Providers**: Includes models from OpenAI, Meta, NVIDIA, Hugging Face, and more.<br>- **Model Collections**: Organized into collections such as `Curated by Azure AI` and `Open models from Hugging Face`.<br>- **Search and Filters**: Use keyword search and filters to find models that meet your needs.<br>- **Benchmark Metrics**: Access model performance benchmark metrics for select models. |
| **Model Deployment**         | Deploy models directly from the catalog to Azure services, ensuring seamless integration and scalability. | - **Deployment Options**: Choose between managed compute and serverless APIs.<br>- **Integration**: Models can be deployed to Azure services like Azure Machine Learning and Azure OpenAI Service.<br>- **Scalability**: Benefit from Azure's scalable infrastructure to handle varying workloads.<br>- **Support**: Microsoft provides support for deployment problems for models curated by Azure AI. |
| **Custom Model Requests**    | Submit requests to add specific models to the catalog.                      | - **Request Submission**: Use the provided form to submit a request to add a model to the catalog.<br>- **Model Details**: Provide details about the model, including its use case and performance metrics. |

https://github.com/user-attachments/assets/5b10270d-b5fe-40f7-9af2-df2cdc77658b

### Advanced Analytics

> - **Azure Synapse Analytics**: <br/>
>    1. **Set Up Synapse Workspace**: Create a Synapse workspace in the Azure portal. <br/>
>    2. **Data Integration**: Integrate data from various sources for comprehensive analysis. <br/>
>    3. **Analytics and Visualization**: Use Synapse Studio to perform advanced analytics and visualize data insights. <br/>
> - **Power BI**: <br/>
>    1. **Create Power BI Reports**: Develop interactive reports and dashboards to visualize LLM performance and usage patterns. <br/>
>    2. **Data Connectivity**: Connect Power BI to Azure data sources for real-time insights.

Click here to read more about [Implement Advanced Analytics](./1_ImplementAdvancedAnalytics.md)

> [!NOTE]
> If you are considering Azure Data Factory, Azure Synapse Analytics, and Power Bi please consider Microsoft Fabric. Click here to review an [essentials workshop about Microsoft Fabric](https://github.com/MicrosoftCloudEssentials-LearningHub/MS-Fabric-Essentials-Workshop).

<div align="center">
  <img src="https://github.com/user-attachments/assets/8fdb3198-8fda-4dd0-869e-b0dccb268a30" alt="Centered Image" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px; width: 70%; height: auto;" />
</div>

From [Microsoft Documentation](https://learn.microsoft.com/pt-br/fabric/fundamentals/microsoft-fabric-overview)

### Machine Learning Operations (MLOps)

1. **Set Up MLOps Pipelines**: Use Azure Machine Learning to create CI/CD pipelines for model deployment and monitoring.
2. **Model Monitoring**: Implement monitoring solutions to track model performance and detect anomalies.
3. **Continuous Delivery**: Automate the deployment of new model versions and updates.

Click here to read more about [Machine Learning Operations (MLOps)](./2_MLOps.md)

## Evaluation of GenAI Applications

<div align="center">
  <img src="https://github.com/user-attachments/assets/cb4d2d89-380c-4ef9-b016-42c606a735b4" alt="Centered Image" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px; width: 70%; height: auto;"/>
</div>

From [Microsoft Documentation](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/evaluation-approach-gen-ai)

### Base Model Selection

- **Model Comparison**: Compare different models by testing their outputs against criteria relevant to your application. Consider accuracy, performance, and ethical considerations.

### Pre-production Evaluation

- **Evaluation Data**: Use your own evaluation data to test AI applications in pre-production. Utilize Azure AI Foundry or Azure AI Evaluation SDK’s supported evaluators.
- **Quality and Safety**: Assess generation quality, safety, and custom evaluators to ensure the application meets desired standards.

<div align="center">
  <img src="https://github.com/user-attachments/assets/11e15924-c290-420b-b0f3-fe5384be1132" alt="Centered Image" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px; width: 70%; height: auto;"/>
</div>

From [Microsoft Documentation](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/evaluation-approach-gen-ai)

### Post-production Monitoring

- **Ongoing Evaluation**: Continuously monitor AI applications in production to ensure they maintain performance and compliance standards.
- **Feedback Integration**: Incorporate feedback from real-world usage to refine and improve the applications.

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1287-limegreen" alt="Total views">
  <p>Refresh Date: 2025-08-12</p>
</div>
<!-- END BADGE -->
