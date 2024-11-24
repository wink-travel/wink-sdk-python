# LifestylesResponseSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | Lifestyles belong to this property identifier  | 
**list** | **List[str]** | List of new lifestyles to set on property. | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.lifestyles_response_supplier import LifestylesResponseSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of LifestylesResponseSupplier from a JSON string
lifestyles_response_supplier_instance = LifestylesResponseSupplier.from_json(json)
# print the JSON string representation of the object
print(LifestylesResponseSupplier.to_json())

# convert the object into a dict
lifestyles_response_supplier_dict = lifestyles_response_supplier_instance.to_dict()
# create an instance of LifestylesResponseSupplier from a dict
lifestyles_response_supplier_from_dict = LifestylesResponseSupplier.from_dict(lifestyles_response_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


