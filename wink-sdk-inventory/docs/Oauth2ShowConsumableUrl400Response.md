# Oauth2ShowConsumableUrl400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.oauth2_show_consumable_url400_response import Oauth2ShowConsumableUrl400Response

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2ShowConsumableUrl400Response from a JSON string
oauth2_show_consumable_url400_response_instance = Oauth2ShowConsumableUrl400Response.from_json(json)
# print the JSON string representation of the object
print(Oauth2ShowConsumableUrl400Response.to_json())

# convert the object into a dict
oauth2_show_consumable_url400_response_dict = oauth2_show_consumable_url400_response_instance.to_dict()
# create an instance of Oauth2ShowConsumableUrl400Response from a dict
oauth2_show_consumable_url400_response_from_dict = Oauth2ShowConsumableUrl400Response.from_dict(oauth2_show_consumable_url400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


