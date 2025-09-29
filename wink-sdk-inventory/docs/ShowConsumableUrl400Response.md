# ShowConsumableUrl400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.show_consumable_url400_response import ShowConsumableUrl400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShowConsumableUrl400Response from a JSON string
show_consumable_url400_response_instance = ShowConsumableUrl400Response.from_json(json)
# print the JSON string representation of the object
print(ShowConsumableUrl400Response.to_json())

# convert the object into a dict
show_consumable_url400_response_dict = show_consumable_url400_response_instance.to_dict()
# create an instance of ShowConsumableUrl400Response from a dict
show_consumable_url400_response_from_dict = ShowConsumableUrl400Response.from_dict(show_consumable_url400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


