# CommissionableEntryAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**identifier** | **str** |  | 
**type** | **str** |  | 
**commission_percent** | **float** |  | 

## Example

```python
from wink_sdk_travel_agent.models.commissionable_entry_agent import CommissionableEntryAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionableEntryAgent from a JSON string
commissionable_entry_agent_instance = CommissionableEntryAgent.from_json(json)
# print the JSON string representation of the object
print(CommissionableEntryAgent.to_json())

# convert the object into a dict
commissionable_entry_agent_dict = commissionable_entry_agent_instance.to_dict()
# create an instance of CommissionableEntryAgent from a dict
commissionable_entry_agent_from_dict = CommissionableEntryAgent.from_dict(commissionable_entry_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


