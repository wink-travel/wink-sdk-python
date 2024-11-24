# SocialNetworksResponseSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | Property identifier associated with social networks | 
**list** | [**List[SocialSupplier]**](SocialSupplier.md) | List of social networks. | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.social_networks_response_supplier import SocialNetworksResponseSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SocialNetworksResponseSupplier from a JSON string
social_networks_response_supplier_instance = SocialNetworksResponseSupplier.from_json(json)
# print the JSON string representation of the object
print(SocialNetworksResponseSupplier.to_json())

# convert the object into a dict
social_networks_response_supplier_dict = social_networks_response_supplier_instance.to_dict()
# create an instance of SocialNetworksResponseSupplier from a dict
social_networks_response_supplier_from_dict = SocialNetworksResponseSupplier.from_dict(social_networks_response_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


