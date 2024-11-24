# UpsertSyndicationSettingsAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intelligent** | **bool** | Whether to treat all links as flat web links or try to embed more advanced data. | 
**engine_configuration_identifier** | **str** | Customization identifier | 
**initial_display_type** | **str** | Which way to display the list when WinkLinks first loads | [optional] [default to 'GRID_COLUMNS']
**profile_picture_geometry** | **str** | Controls how to display profile picture | [optional] [default to 'CIRCLE']

## Example

```python
from wink_sdk_affiliate_winklinks.models.upsert_syndication_settings_affiliate import UpsertSyndicationSettingsAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSyndicationSettingsAffiliate from a JSON string
upsert_syndication_settings_affiliate_instance = UpsertSyndicationSettingsAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertSyndicationSettingsAffiliate.to_json())

# convert the object into a dict
upsert_syndication_settings_affiliate_dict = upsert_syndication_settings_affiliate_instance.to_dict()
# create an instance of UpsertSyndicationSettingsAffiliate from a dict
upsert_syndication_settings_affiliate_from_dict = UpsertSyndicationSettingsAffiliate.from_dict(upsert_syndication_settings_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


