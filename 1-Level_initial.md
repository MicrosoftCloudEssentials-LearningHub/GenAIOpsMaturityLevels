# Level 1 - Initial: Quick Guide

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-03-09

----------

> At this maturity level, organizations are exploring the capabilities of `large language models (LLMs)` but have not yet developed structured practices or systematic approaches.  
> The focus is on familiarizing with `LLM APIs`, experimenting with `prompt design`, and introducing basic metrics for evaluating LLM application performance.

<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [What is Azure OpenAI Service?](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)
- [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)

</details>

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

2. **Search for Models**:
   - Use the search bar to find specific models or filter models by categories such as `Large Language Models (LLMs)` or `Embedding Models`.
   - Apply filters like `Collections` (e.g., `Benchmark Results`) to narrow down your options.

3. **Identify Models with Benchmark Data**:
   - Models with benchmarking data are marked with a `bar graph icon` in the catalog.
   - Click on a model to open its `Model Details Page`.

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

6. **Evaluate Models with Your Own Data**:
   - For supported models, upload your own private datasets to benchmark their performance in your specific use case.
   - Use the benchmarking tools to assess how well the models perform on your data.

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

## Test the API

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




<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
