# Level 2 - Defined: Quick Guide

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-17

----------

> At this maturity level, organizations have started to systematize `LLM operations` with structured development and experimentation. The focus is on developing `complex prompts`, integrating them into applications, and implementing systematic approaches for `LLM application deployment`.

<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [Prompt Flow in Azure AI Foundry portal](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/prompt-flow)
- [How to Build with Prompt Flow](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/flow-develop)
- [Deploy a Flow as a Managed Online endpoint for Real-Time Inference](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/flow-deploy?tabs=azure-studio)
- [Integrate Prompt Flow with GenAIOps](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-integrate-with-llm-app-devops?view=azureml-api-2&tabs=cli)
- [GenAI Evaluation with Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai)
- [GenAI Evaluation and Monitoring Metrics](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-metrics-built-in?tabs=warning)
- [Azure Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview)
- [Responsible AI Tools and Practices](https://azure.microsoft.com/en-us/blog/infuse-responsible-ai-tools-and-practices-in-your-llmops/#:%7E:text=Azure%20AI%20offers%20robust%20tools,or%20build%20your%20own%20metrics)
  
</details>

## Content

- [Develop Complex Prompts](#develop-complex-prompts)
    - [Access Azure Machine Learning Studio](#access-azure-machine-learning-studio)
    - [Use Prompt Flow](#use-prompt-flow)
    - [Collaborate on Prompts](#collaborate-on-prompts)
- [Integrate Prompts into Applications](#integrate-prompts-into-applications)
    - [Set Up Azure Functions](#set-up-azure-functions)
    - [Use Logic Apps](#use-logic-apps)
    - [Test the Integration](#test-the-integration)
- [Systematic Deployment](#systematic-deployment)
    - [Set Up CI/CD Pipelines](#set-up-cicd-pipelines)
    - [Automate Deployment](#automate-deployment)
    - [Monitor and Maintain Applications](#monitor-and-maintain-applications)

## Develop Complex Prompts

- Design more sophisticated prompts.
- Utilize Azure AI Hub for managing prompt versions.

### Access Azure Machine Learning Studio

1. Log in to the [Azure Machine Learning Studio](https://ml.azure.com/home).
2. Create a new workspace or select an existing one.
   - Navigate to `Workspaces` and click `Create`.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/15c8536d-84b2-4a72-a1e1-12ef633f78ee" />

   - Fill in the required details (e.g., subscription, resource group, workspace name).
   - Click `Create` to finalize.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/fcb6a7a3-8027-4509-9a9e-cdae3bf729b1" />

### Use Prompt Flow 

1. In the [Azure Machine Learning Studio](https://ml.azure.com/), go to `Prompt Flow` under the `Authoring` section.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/eb582e8c-e88c-424d-9a33-40785529917e" />

2. Create a new `Prompt Flow project`:
   - Click `+ Create`:

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/8c4e2602-cbe1-4ca4-9016-47a87d995e1d" />

   - Select a template or start from scratch.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/3e8fa322-a043-4836-a3c6-9573d102afd9">

        https://github.com/user-attachments/assets/c9bcb62b-856c-4cd5-b103-01adbc446f7d

3. Design and test prompts:
   - Add a `Prompt Node` to the flow.
   - Write your prompt in the editor and test it with sample inputs.
   - Adjust the prompt iteratively based on the output quality.

### Collaborate on Prompts

1. Set up a repository in `Azure DevOps` or `GitHub`:
   - Create a new repository and upload your prompt files.
   - Use branches to manage different versions or experiments.
2. Collaborate with your team:
   - Use pull requests for reviewing changes.
   - Add comments and suggestions directly in the repository.

## Integrate Prompts into Applications

- Embed prompts into applications using Azure Functions or Logic Apps.
- Ensure seamless integration with existing workflows.

### Set Up Azure Functions

1. In the Azure portal, go to `Create a Resource` and search for `Function App`.
2. Click `Create` and fill in the required details: Subscription, resource group, function app name, runtime stack (e.g., Python or Node.js), and region.

      https://github.com/user-attachments/assets/c8ddae07-d93b-4bb6-9484-daf527606e3d

3. Deploy your function:
   - Write code to send prompts to the Azure OpenAI API and process responses.
   - Use the Azure Functions editor or deploy from a local development environment using tools like Visual Studio Code.

### Use Logic Apps

1. In the Azure portal, search for `Logic Apps` and click `Create`.
2. Choose a `Consumption` or `Standard` plan and fill in the required details.
3. Design your workflow:
   - Add a trigger (e.g., HTTP request, timer, or event).
   - Use the `Azure OpenAI connector` to send prompts and receive responses.
   - Add actions to process the response and integrate it into your application.

### Test the Integration

1. Use the Azure portal's testing tools to simulate requests.

    https://github.com/user-attachments/assets/9cc719a3-a0d4-49a3-88b6-fc6d0677ce61

2. Or use  `Bruno` testing tools to simulate requests.

   https://github.com/user-attachments/assets/ad931fe9-4946-48b4-a4ab-d249aa4fee66

3. Verify that the prompts are executed correctly and the responses are as expected.
4. Debug any issues using the logs in Azure Functions or Logic Apps.

## Systematic Deployment

- Implement CI/CD pipelines using Azure DevOps.
- Automate deployment processes for LLM applications.

### Set Up CI/CD Pipelines

1. In `Azure DevOps`, create a new project.
2. Set up a repository for your application code and prompts.
3. Create a pipeline:
   - Go to `Pipelines` and click `New Pipeline`.
   - Select your repository and configure the pipeline using a YAML file or the visual editor.
   - Add tasks for testing, building, and deploying your application.

### Automate Deployment

1. Use `Azure Pipelines` to automate the deployment process:
   - Add deployment tasks to your pipeline (e.g., deploy to Azure Functions or Logic Apps).
   - Configure environment variables and secrets using Azure Key Vault.
2. Deploy to production:
   - Use `Azure App Services`, `Kubernetes`, or other platforms for hosting your application.
   - Monitor the deployment process in the Azure portal.

### Monitor and Maintain Applications

1. Use `Azure Monitor` to track application performance:
   - Set up metrics and logs for your Azure Functions or Logic Apps.
   - Create alerts for issues like high latency or errors in prompt execution.
2. Regularly update and optimize:
   - Iterate on prompts based on user feedback and performance data.
   - Use version control to manage updates and rollbacks.

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-354-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-17</p>
</div>
<!-- END BADGE -->
