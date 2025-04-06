# SyndicationSettingsAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **str** | Creator of entry | 
**owner_identifier** | **str** | The user&#39;s owner company this entry associates with | 
**intelligent** | **bool** | Whether to treat all links as flat web links or try to embed more advanced data. | [optional] 
**engine_configuration_identifier** | **str** | Customization identifier | 
**initial_display_type** | **str** | Which way to display the list when WinkLinks first loads | [optional] [default to 'GRID_COLUMNS']
**profile_picture_geometry** | **str** | Controls how to display profile picture | [optional] [default to 'CIRCLE']

## Example

```python
from wink_sdk_affiliate_winklinks.models.syndication_settings_affiliate import SyndicationSettingsAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SyndicationSettingsAffiliate from a JSON string
syndication_settings_affiliate_instance = SyndicationSettingsAffiliate.from_json(json)
# print the JSON string representation of the object
print(SyndicationSettingsAffiliate.to_json())

# convert the object into a dict
syndication_settings_affiliate_dict = syndication_settings_affiliate_instance.to_dict()
# create an instance of SyndicationSettingsAffiliate from a dict
syndication_settings_affiliate_from_dict = SyndicationSettingsAffiliate.from_dict(syndication_settings_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


