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

> [!NOTE]
> If you are considering Azure Data Factory, Azure Synapse Analytics, and Power Bi please consider Microsoft Fabric. Click here to review an [essentials workshop about Microsoft Fabric](https://github.com/MicrosoftCloudEssentials-LearningHub/MS-Fabric-Essentials-Workshop).

<div align="center">
  <img src="https://github.com/user-attachments/assets/8fdb3198-8fda-4dd0-869e-b0dccb268a30" alt="Centered Image" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>

From [Microsoft Documentation](https://learn.microsoft.com/pt-br/fabric/fundamentals/microsoft-fabric-overview)

#### Azure Synapse Analytics: Set up synapse workspace
1. **Sign in to Azure Portal**: Go to the [Azure portal](https://portal.azure.com/) and sign in with your Azure account credentials.
2. **Search for Synapse**: In the search bar at the top of the Azure portal, type `Synapse` and select `Azure Synapse Analytics` from the search results.

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/6df7d1d4-458b-4dc7-a13c-971fb5c60ca9" />

3. **Create a New Synapse Workspace**:
     - Click on the `+ Create` button to start the creation process.
     - Fill in the required fields:
          - **Subscription**: Select the Azure subscription you want to use.
          - **Resource Group**: Choose an existing resource group or create a new one.
          - **Workspace Name**: Provide a unique name for your Synapse workspace.
          - **Region**: Select the region where you want to create the workspace.
          - **Data Lake Storage Gen2**: Select or create a Data Lake Storage Gen2 account to use as the primary storage account.
     - Click `Review + Create` and then `Create` to finalize the creation.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/23200833-82f3-4ab0-80de-2c88a0574415" />

#### Azure Synapse Analytics: Data integration

1. **Open Synapse Studio**:
     - After the Synapse workspace is created, navigate to it in the Azure portal.
     - Click on `Open Synapse Studio` from the workspace overview.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/44855c8b-484d-40f1-b01d-979284de37be" />

2. **Integrate Data**:
     - In Synapse Studio, go to the `Data` hub.
     - Click on `+` and select `Linked service` to connect to various data sources (e.g., Azure SQL Database, Azure Blob Storage, on-premises databases).
     - Configure the linked service by providing the necessary connection details and credentials.
     - Create datasets to represent the data you want to integrate and use in your pipelines.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/71917d70-3068-47ac-bd1a-6d8e3129c1ac" />

#### Azure Synapse Analytics: Analytics and visualization

1. **Create Notebooks**:
     - In Synapse Studio, go to the `Develop` hub.
     - Click on `+` and select `Notebook` to create a new notebook.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/55680c4a-73c2-45c0-be30-8994a77b1ad8" />

     - Use the notebook to perform data analysis using languages like PySpark, SQL, or Scala.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/3ecf51c7-8af7-42a4-9094-35c48bad8014" />

2. **Visualize Data**:
     - Use built-in visualization libraries (e.g., Matplotlib, Seaborn) to create charts and graphs within the notebook.
     - Alternatively, use Synapse Studio's built-in visualization tools to create interactive visualizations.

#### Power BI: Create power bi reports

1. **Open Power BI Desktop**:
     - Download and install [Power BI Desktop](https://www.microsoft.com/en-us/power-platform/products/power-bi/desktop?msockid=38ec3806873362243e122ce086486339).
     - Open Power BI Desktop and sign in with your Microsoft account.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/afe7c483-f0a4-48db-af3c-9a734e849c66">

2. **Develop Reports**:
     - Click on `Get Data` to connect to your data sources (e.g., Azure SQL Database, Azure Synapse Analytics).
     
          <img width="954" alt="image" src="https://github.com/user-attachments/assets/ee17b9bd-f977-40fd-81f1-3301cf6be5e2" />
     
     - Use the Power Query Editor to transform and clean your data.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/d73161fa-7de9-476f-854c-4aab55f5fbd0" />

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/dfe32980-e7e4-42e5-944a-23e2dd333a3a" />

     - Create visualizations by dragging and dropping fields onto the report canvas.
     - Customize the visualizations using the formatting options available in Power BI Desktop.

          https://github.com/user-attachments/assets/52a7ba56-ea2a-4424-a03d-3fe1cc9d7047

3. **Publish Reports**:
     - Once your report is ready, click on `Publish` to publish it to the Power BI service.
     - Select the workspace where you want to publish the report.

          https://github.com/user-attachments/assets/41abbe03-441f-4e4c-8f3c-f79ea7711b50

#### Power BI: Data Connectivity
1. **Connect to Azure Data Sources**:
   - In Power BI Desktop, click on `Get Data` and select the Azure data source you want to connect to (e.g., Azure SQL Database, Azure Blob Storage).
   - Provide the necessary connection details and credentials to establish the connectio.
2. **Real-Time Insights**:
   - Use DirectQuery or Live Connection to connect to your Azure data sources for real-time data access.
   - Create dashboards in the Power BI service to monitor real-time data and gain insights into your LLM performance and usage patterns.
     
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
