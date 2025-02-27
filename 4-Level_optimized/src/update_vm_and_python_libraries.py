import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import subprocess

# Parameters
resource_group_name = os.environ.get("ResourceGroupName")
vm_name = os.environ.get("VMName")

# Authenticate
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, os.environ.get("AZURE_SUBSCRIPTION_ID"))

# Function to check VM status
def get_vm_status(resource_group_name, vm_name):
    vm = compute_client.virtual_machines.get(resource_group_name, vm_name, expand='instanceView')
    statuses = vm.instance_view.statuses
    for status in statuses:
        if 'PowerState' in status.code:
            return status.code.split('/')[-1]
    return None

# Check VM status
vm_status = get_vm_status(resource_group_name, vm_name)
print(f"Current VM status: {vm_status}")

# Start VM if it's not running
if vm_status != 'running':
    print(f"Starting VM: {vm_name} in resource group: {resource_group_name}")
    async_vm_start = compute_client.virtual_machines.begin_start(resource_group_name, vm_name)
    async_vm_start.result()
    print(f"Started VM: {vm_name} in resource group: {resource_group_name}")
else:
    print(f"VM: {vm_name} is already running in resource group: {resource_group_name}")

# Update Python core libraries
def update_python_libraries():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "setuptools"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "wheel"])
        print("Python core libraries updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating Python libraries: {e}")

# Update libraries
update_python_libraries()
