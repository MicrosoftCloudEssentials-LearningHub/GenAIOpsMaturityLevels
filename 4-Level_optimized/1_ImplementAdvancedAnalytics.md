# Level 4 - Optimized: Implement Advanced Analytics

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-17

----------

## Azure Synapse Analytics

### Set up synapse workspace
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

### Data integration

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

### Analytics and visualization

1. **Create Notebooks**:
     - In Synapse Studio, go to the `Develop` hub.
     - Click on `+` and select `Notebook` to create a new notebook.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/55680c4a-73c2-45c0-be30-8994a77b1ad8" />

     - Use the notebook to perform data analysis using languages like PySpark, SQL, or Scala.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/3ecf51c7-8af7-42a4-9094-35c48bad8014" />

2. **Visualize Data**:
     - Use built-in visualization libraries (e.g., Matplotlib, Seaborn) to create charts and graphs within the notebook.
     - Alternatively, use Synapse Studio's built-in visualization tools to create interactive visualizations.

## Power BI 

### Create Power Bi Reports

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

### Data Connectivity
1. **Connect to Azure Data Sources**:
   - In Power BI Desktop, click on `Get Data` and select the Azure data source you want to connect to (e.g., Azure SQL Database, Azure Blob Storage).
   - Provide the necessary connection details and credentials to establish the connectio.
2. **Real-Time Insights**:
   - Use DirectQuery or Live Connection to connect to your Azure data sources for real-time data access.
   - Create dashboards in the Power BI service to monitor real-time data and gain insights into your LLM performance and usage patterns.
     
<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-354-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-17</p>
</div>
<!-- END BADGE -->
