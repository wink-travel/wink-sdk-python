# GeneralManagerAffiliate

General manager related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of GM currently managing the property. | 
**image** | [**SimpleMultimediaAffiliate**](SimpleMultimediaAffiliate.md) | Cloudinary image identifier of GM currently managing the property. | [optional] 
**descriptions** | [**List[LocalizedDescriptionAffiliate]**](LocalizedDescriptionAffiliate.md) | Localized welcome message from GM. | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.general_manager_affiliate import GeneralManagerAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralManagerAffiliate from a JSON string
general_manager_affiliate_instance = GeneralManagerAffiliate.from_json(json)
# print the JSON string representation of the object
print(GeneralManagerAffiliate.to_json())

# convert the object into a dict
general_manager_affiliate_dict = general_manager_affiliate_instance.to_dict()
# create an instance of GeneralManagerAffiliate from a dict
general_manager_affiliate_from_dict = GeneralManagerAffiliate.from_dict(general_manager_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


