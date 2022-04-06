string = '''
"{\"id\":\"/subscriptions/284bc6ed-4e92-4149-aa3d-15d98ce038bf/resourceGroups/Demo-Automation/providers/Microsoft.Automation/automationAccounts/Automation/softwareUpdat
eConfigurations/test\",\"name\":\"test\",\"type\":null,\"properties\":{\"updateConfiguration\":{\"operatingSystem\":\"Windows\",\"windows\":{\"includedUpdateClassificat
ions\":\"Critical, Security, UpdateRollup, FeaturePack, ServicePack, Definition, Tools, Updates\",\"excludedKbNumbers\":[],\"includedKbNumbers\":[],\"rebootSetting\":\"
IfRequired\"},\"linux\":null,\"targets\":{\"azureQueries\":[{\"scope\":[\"/subscriptions/284bc6ed-4e92-4149-aa3d-15d98ce038bf/resourcegroups/demo-asr\"],\"tagSettings\"
:{\"tags\":{},\"filterOperator\":\"All\"},\"locations\":[]}],\"nonAzureQueries\":null},\"duration\":\"PT2H\",\"azureVirtualMachines\":[\"/subscriptions/284bc6ed-4e92-41
49-aa3d-15d98ce038bf/resourceGroups/Demo-Automation/providers/Microsoft.Compute/virtualMachines/windowsHRW\"],\"nonAzureComputerNames\":[]},\"scheduleInfo\":{\"descript
ion\":null,\"startTime\":\"2022-04-05T19:43:00-07:00\",\"startTimeOffsetMinutes\":-420.0,\"expiryTime\":\"2022-04-05T19:43:00-07:00\",\"expiryTimeOffsetMinutes\":-420.0
,\"isEnabled\":true,\"nextRun\":\"2022-04-05T19:43:00-07:00\",\"nextRunOffsetMinutes\":-420.0,\"interval\":null,\"frequency\":\"OneTime\",\"creationTime\":\"2022-03-28T
21:50:45.2166667+00:00\",\"lastModifiedTime\":\"2022-04-05T14:41:23.3533333+00:00\",\"timeZone\":\"America/Los_Angeles\",\"advancedSchedule\":null},\"provisioningState\
":\"Succeeded\",\"createdBy\":\"{scrubbed}\",\"error\":null,\"tasks\":{\"preTask\":null,\"postTask\":null},\"creationTime\":\"2022-03-28T21:50:45.22+00:00\",\"lastModif
iedBy\":null,\"lastModifiedTime\":\"2022-04-05T14:41:23.3966667+00:00\"}}"
'''


new_string = string.replace("\\", "\n")
print(new_string)