# TravelAgentSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**self_acquires** | **bool** | Whether the agent is in charge of charging the property. | 
**self_disburses** | **bool** | Whether the agent is in charge of paying the property. | 

## Example

```python
from wink_sdk_affiliate.models.travel_agent_supplier import TravelAgentSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of TravelAgentSupplier from a JSON string
travel_agent_supplier_instance = TravelAgentSupplier.from_json(json)
# print the JSON string representation of the object
print(TravelAgentSupplier.to_json())

# convert the object into a dict
travel_agent_supplier_dict = travel_agent_supplier_instance.to_dict()
# create an instance of TravelAgentSupplier from a dict
travel_agent_supplier_from_dict = TravelAgentSupplier.from_dict(travel_agent_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


