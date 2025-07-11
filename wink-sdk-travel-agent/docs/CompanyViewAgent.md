# CompanyViewAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**company** | [**CompanyAgent**](CompanyAgent.md) |  | 

## Example

```python
from wink_sdk_travel_agent.models.company_view_agent import CompanyViewAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyViewAgent from a JSON string
company_view_agent_instance = CompanyViewAgent.from_json(json)
# print the JSON string representation of the object
print(CompanyViewAgent.to_json())

# convert the object into a dict
company_view_agent_dict = company_view_agent_instance.to_dict()
# create an instance of CompanyViewAgent from a dict
company_view_agent_from_dict = CompanyViewAgent.from_dict(company_view_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


