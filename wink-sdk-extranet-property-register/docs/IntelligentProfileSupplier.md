# IntelligentProfileSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ambiance** | **str** | Textual description of property ambiance | [optional] 
**architecture** | **str** | Property architecture | 
**design_elements** | **str** | Textual description of property design elements | [optional] 
**historic** | **str** | Textual description of property&#39;s historic significance | [optional] 
**number_of_rooms** | **int** | Number of keys for this property | 
**hotel_stars** | **int** | Number of stars for this propert. | 
**location_category** | **str** | Property location code | 
**segment** | **str** | Property segment code | 
**property_class** | **str** | Property class code | 
**style** | **str** | Textual description of property style | [optional] 
**chain** | **str** | Textual name of property chain | [optional] 
**brand** | **str** | Textual name of property brand | [optional] 
**year_built** | **str** | The year the property was built | [optional] 

## Example

```python
from wink_sdk_extranet_property_register.models.intelligent_profile_supplier import IntelligentProfileSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of IntelligentProfileSupplier from a JSON string
intelligent_profile_supplier_instance = IntelligentProfileSupplier.from_json(json)
# print the JSON string representation of the object
print(IntelligentProfileSupplier.to_json())

# convert the object into a dict
intelligent_profile_supplier_dict = intelligent_profile_supplier_instance.to_dict()
# create an instance of IntelligentProfileSupplier from a dict
intelligent_profile_supplier_from_dict = IntelligentProfileSupplier.from_dict(intelligent_profile_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


