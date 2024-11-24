# SuggestProfileResponseSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website** | **str** | Website | 
**ambiance** | **str** | Property ambiance | 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**province** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**architecture** | **str** |  | [optional] 
**design_elements** | **str** |  | [optional] 
**historic** | **str** |  | [optional] 
**number_of_rooms** | **str** |  | [optional] 
**hotel_stars** | **str** |  | [optional] 
**location_category** | **str** |  | [optional] 
**segment** | **str** |  | [optional] 
**property_class** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**chain** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**year_built** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.suggest_profile_response_supplier import SuggestProfileResponseSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestProfileResponseSupplier from a JSON string
suggest_profile_response_supplier_instance = SuggestProfileResponseSupplier.from_json(json)
# print the JSON string representation of the object
print(SuggestProfileResponseSupplier.to_json())

# convert the object into a dict
suggest_profile_response_supplier_dict = suggest_profile_response_supplier_instance.to_dict()
# create an instance of SuggestProfileResponseSupplier from a dict
suggest_profile_response_supplier_from_dict = SuggestProfileResponseSupplier.from_dict(suggest_profile_response_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


