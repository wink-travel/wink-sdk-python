# GeneralManagerSupplier

General manager related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of GM currently managing the property. | 
**image** | [**SimpleMultimediaSupplier**](SimpleMultimediaSupplier.md) |  | [optional] 
**descriptions** | [**List[LocalizedDescriptionSupplier]**](LocalizedDescriptionSupplier.md) | Localized welcome message from GM. | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.general_manager_supplier import GeneralManagerSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralManagerSupplier from a JSON string
general_manager_supplier_instance = GeneralManagerSupplier.from_json(json)
# print the JSON string representation of the object
print(GeneralManagerSupplier.to_json())

# convert the object into a dict
general_manager_supplier_dict = general_manager_supplier_instance.to_dict()
# create an instance of GeneralManagerSupplier from a dict
general_manager_supplier_from_dict = GeneralManagerSupplier.from_dict(general_manager_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


