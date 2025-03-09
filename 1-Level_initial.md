# Level 1 - Initial: Quick Guide

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-02-19

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
    3. Fill in the required fields:
        - **Subscription**: Select your Azure subscription.
        - **Resource Group**: Choose an existing resource group or create a new one.
        - **Region**: Select the region where the service will be hosted
        - **Name**: Provide a unique name for the resource.
    4. Click `Review + Create` and then `Create` to finalize the setup.

## Access API Keys

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

## Explore Documentation

> Review the [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/) to understand available models, endpoints, and parameters.




<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
