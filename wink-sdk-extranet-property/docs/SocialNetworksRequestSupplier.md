# SocialNetworksRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[SocialSupplier]**](SocialSupplier.md) | List of social networks. | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.social_networks_request_supplier import SocialNetworksRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SocialNetworksRequestSupplier from a JSON string
social_networks_request_supplier_instance = SocialNetworksRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(SocialNetworksRequestSupplier.to_json())

# convert the object into a dict
social_networks_request_supplier_dict = social_networks_request_supplier_instance.to_dict()
# create an instance of SocialNetworksRequestSupplier from a dict
social_networks_request_supplier_from_dict = SocialNetworksRequestSupplier.from_dict(social_networks_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


