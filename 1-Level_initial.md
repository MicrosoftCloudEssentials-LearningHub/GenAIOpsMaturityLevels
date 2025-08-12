# Level 1 - Initial: Quick Guide

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-17

----------

> At this maturity level, organizations are exploring the capabilities of `large language models (LLMs)` but have not yet developed structured practices or systematic approaches.  
> The focus is on familiarizing with `LLM APIs`, experimenting with `prompt design`, and introducing basic metrics for evaluating LLM application performance.

<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [What is Azure OpenAI Service?](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)
- [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)

</details>

## Content

- [Familiarize with LLM APIs](#familiarize-with-llm-apis)
    - [Set Up Azure AI Foundry Service](#set-up-azure-ai-foundry-service)
    - [Explore and Compare Models](#explore-and-compare-models)
    - [Access API Keys](#access-api-keys)
    - [Test the API](#test-the-api)
    - [Explore Documentation](#explore-documentation)
- [Experiment with Prompt Design](#experiment-with-prompt-design)
- [Introduce Basic Metrics](#introduce-basic-metrics)


## Familiarize with LLM APIs

> Explore and understand the functionalities and capabilities of Azure OpenAI Service APIs.

### Set Up Azure AI Foundry Service

- **Sign in to Azure Portal**: Go to the [Azure portal](https://portal.azure.com/) and sign in with your Azure account.
- **Create an Azure OpenAI Resource**:
    1. In the search bar, type `Azure AI Foundry` and select.
    2. Click on `+ Create` to create a new resource.
    
        <img width="550" alt="image" src="https://github.com/user-attachments/assets/84a51444-67bc-4682-9458-dcec5cf035ec" />

    3. Fill in the required fields:
        - **Subscription**: Select your Azure subscription.
        - **Resource Group**: Choose an existing resource group or create a new one.
        - **Region**: Select the region where the service will be hosted
        - **Name**: Provide a unique name for the resource.
    4. Click `Review + Create` and then `Create` to finalize the setup.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/b92d9abc-7ea8-4ff1-819d-2c9ebac33481" />

### Explore and Compare Models

> How to Compare Models in Azure AI Foundry:

1. **Access the Azure AI Foundry Model Catalog**:
   - Sign in to the `Azure AI Foundry portal` at Azure AI Foundry.
   - Navigate to the `Model Catalog` section, where you can explore a wide range of models from providers like OpenAI, Meta, NVIDIA, and Hugging Face.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/ab2927f5-e7b9-440b-a771-d562536f7890" />

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/1dd2d700-c33d-414a-adec-c55532ed69f2" />

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/274c2acb-efde-43ae-a089-3a26ac731279" />

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/094ffb28-a79e-4c36-8671-3e3f725766c9">

2. **Search for Models**:
   - Use the search bar to find specific models or filter models by categories such as `Large Language Models (LLMs)` or `Embedding Models`.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/1008133c-f636-4536-aa1b-953afa89a9d3" />

   - Apply filters like `Collections` (e.g., `Benchmark Results`) to narrow down your options.

        https://github.com/user-attachments/assets/72051879-fc06-4398-876d-cbb29ea1db09

3. **Identify Models with Benchmark Data**: Models with benchmarking data are marked with a `bar graph icon` in the catalog.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/4603850f-d368-4fea-b227-0ef1d34cdecf" />

4. **View Benchmark Results**:
   - On the model's details page, go to the `Benchmarks Tab`.
   - Review the following:
     - `Index Scores`: High-level performance summaries for metrics like generation quality, cost, latency, and throughput.
     - `Comparative Charts`: Visualize the model's performance relative to other models.
     - `Metric Comparison Table`: Detailed results for each individual metric, such as accuracy or response time.

5. **Compare Multiple Models**:
   - Use the `Compare with More Models` button to select multiple models for side-by-side comparison.
   - Evaluate trade-offs across key performance criteria, such as:
     - `Generation Quality`: Accuracy and relevance of model outputs.
     - `Cost`: Resource consumption and pricing.
     - `Latency`: Response time for generating outputs.


        https://github.com/user-attachments/assets/4d91897a-feb5-4321-bb65-f03138237aed

6. **Evaluate Models with Your Own Data**:
   - For supported models, upload your own private datasets to benchmark their performance in your specific use case.
   - Use the benchmarking tools to assess how well the models perform on your data.

        https://github.com/user-attachments/assets/c1721757-8bd9-4f94-bac2-7c4977eeb5b1

> How to Use the Model Catalog: 

1. **Explore Models**:
   - Browse through curated collections like `Curated by Azure AI` or `Open Models from Hugging Face`.
   - Use filters to refine your search based on model type, provider, or task (e.g., summarization, chat completion).
2. **Select a Model**:
   - Click on a model to view its details, including:
     - Supported tasks (e.g., `text generation`, `summarization`).
     - Input/output formats.
     - Performance metrics and benchmarks.
3. **Deploy a Model**:
   - From the model's details page, click `Deploy` to integrate the model into your Azure services.
   - Choose deployment options such as `managed compute` or `serverless APIs` for scalability.
4. **Request Custom Models**:
   - If a specific model is not available, submit a request to add it to the catalog.
   - Provide details about the model, its use case, and performance requirements.

### Access API Keys

- Navigate to the Azure AI Foundry resource you created.
- Go to the `Keys and Endpoint` section to retrieve the API key and endpoint URL. These will be used to authenticate API requests.

### Test the API

> Use tools like **Bruno** or **cURL** to send test requests to the Azure OpenAI API. E.g cURL command to test the API:

   ```bash
   curl -X POST https://<your-endpoint>/openai/deployments/<deployment-name>/completions?api-version=2023-03-15-preview \
   -H "Content-Type: application/json" \
   -H "api-key: <your-api-key>" \
   -d '{
       "prompt": "Hello, how can I help you?",
       "max_tokens": 50
   }'
   ```

### Explore Documentation

> Review the [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/) to understand available models, endpoints, and parameters.

## Experiment with Prompt Design 

> Create and test simple prompts to understand how LLMs respond to different inputs.

1. In the [Azure portal](https://portal.azure.com/), navigate to your Azure AI Foundry resource.
2. If you haven't created a project yet, please do so.
    
   <img width="550" alt="image" src="https://github.com/user-attachments/assets/c1e542fc-83ae-482c-870a-522f0bd7a3a3" />

3. **Launch Prompt Flow**: Open the Prompt Flow interface to start designing and testing prompts.

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/3c49f4c6-e1ee-4c28-ac90-5a556fadc9dd" />

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/05c0a2ed-0d17-4462-8c9c-3174c4e98770" />

4. **Create and Test a Simple Prompt** the prompt in Prompt Flow to see how the model responds.
5. **Iterate and Improve**: Experiment with variations of the prompt to refine the output.
6. **Save and Version Prompts**: Use Prompt Flow to save and version your prompts for future use.

## Introduce Basic Metrics

> Implement basic performance metrics and monitor application performance using Azure Application Insights.

1. **Attach Application Insights to Your Application**:
    1. In the [Azure portal](https://portal.azure.com/), navigate to your application (e.g., a web app or function app).
    2. Go to the `Application Insights` section and enable it.
    3. If Application Insights is not already configured, create a new instance and link it to your application.

    https://github.com/user-attachments/assets/acea6d2f-78eb-42a7-8cf5-0c16a03bf2f9


2. **Collect Metrics**:
   - **Key Metrics to Monitor**:
     - **Request Rate**: Number of API requests sent to the Azure OpenAI Service.
     - **Response Time**: Time taken for the API to respond.
     - **Error Rate**: Percentage of failed requests.
   - Use the Application Insights SDK to log custom metrics:
     ```python
     from opencensus.ext.azure.log_exporter import AzureLogHandler
     import logging

     logger = logging.getLogger(__name__)
     logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=<your-instrumentation-key>'))

     # Log custom metrics
     logger.info('Request sent to Azure OpenAI API')
     logger.warning('Response time exceeded threshold')
     ```

3. **Create Dashboards**:
   - In the [Azure portal](https://portal.azure.com/), navigate to your Application Insights resource.
   - Use the `Metrics` section to create custom dashboards for visualizing key metrics.

        https://github.com/user-attachments/assets/a6297a6c-f1ff-4294-a4ca-e326326bf34f

4. **Set Up Alerts**: Configure alerts to notify you of performance issues.
     1. In Application Insights, go to the `Alerts` section.
     2. Create a new alert rule and define conditions (e.g., response time > 2 seconds).
     3. Set up action groups to send notifications via email or SMS.

        https://github.com/user-attachments/assets/ef4e6513-ce69-4542-b0d6-244335224e62
        
<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1287-limegreen" alt="Total views">
  <p>Refresh Date: 2025-08-12</p>
</div>
<!-- END BADGE -->
