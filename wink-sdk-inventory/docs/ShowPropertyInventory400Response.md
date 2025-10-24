# ShowPropertyInventory400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.show_property_inventory400_response import ShowPropertyInventory400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShowPropertyInventory400Response from a JSON string
show_property_inventory400_response_instance = ShowPropertyInventory400Response.from_json(json)
# print the JSON string representation of the object
print(ShowPropertyInventory400Response.to_json())

# convert the object into a dict
show_property_inventory400_response_dict = show_property_inventory400_response_instance.to_dict()
# create an instance of ShowPropertyInventory400Response from a dict
show_property_inventory400_response_from_dict = ShowPropertyInventory400Response.from_dict(show_property_inventory400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


