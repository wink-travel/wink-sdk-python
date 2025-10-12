# SyndicationSettingsQrCodeOptionsAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_identifier** | **str** | Custom image ID for subscribers | [optional] 
**shape** | **str** | QR code shape | [optional] [default to 'SQUARE']
**dots_type** | **str** | QR code shape | [optional] [default to 'SQUARE']
**dots_round_size** | **bool** | Dots round size | [optional] [default to True]
**dots_gradient_type** | **str** | Dots gradient | [optional] [default to 'LINEAR']
**dots_gradient_rotation** | **int** | Dots gradient rotation | [optional] [default to 0]
**dots_start_color** | **str** | Dots primary color | [optional] 
**dots_end_color** | **str** | Dots gradient color | [optional] 
**corner_square_type** | **str** | Corner square type | [optional] [default to 'SQUARE']
**corner_square_gradient_type** | **str** | Corners square gradient | [optional] [default to 'LINEAR']
**corner_square_gradient_rotation** | **int** | Corners square gradient rotation | [optional] [default to 0]
**corner_square_start_color** | **str** | Corner square primary color | [optional] 
**corner_square_end_color** | **str** | Corner square gradient color | [optional] 
**corner_dot_type** | **str** | Corner dot type | [optional] [default to 'SQUARE']
**corner_dot_gradient_type** | **str** | Corners dot gradient | [optional] [default to 'LINEAR']
**corner_dot_gradient_rotation** | **int** | Corners dot gradient rotation | [optional] [default to 0]
**corner_dot_start_color** | **str** | Corner dot primary color | [optional] 
**corner_dot_end_color** | **str** | Corner dot gradient color | [optional] 
**background_round** | **int** | Corner square type | [optional] [default to 0]
**background_gradient_type** | **str** | Corners square gradient | [optional] [default to 'LINEAR']
**background_gradient_rotation** | **int** | Corners square gradient rotation | [optional] [default to 0]
**background_start_color** | **str** | Corner square primary color | [optional] 
**background_end_color** | **str** | Corner square gradient color | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.syndication_settings_qr_code_options_affiliate import SyndicationSettingsQrCodeOptionsAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SyndicationSettingsQrCodeOptionsAffiliate from a JSON string
syndication_settings_qr_code_options_affiliate_instance = SyndicationSettingsQrCodeOptionsAffiliate.from_json(json)
# print the JSON string representation of the object
print(SyndicationSettingsQrCodeOptionsAffiliate.to_json())

# convert the object into a dict
syndication_settings_qr_code_options_affiliate_dict = syndication_settings_qr_code_options_affiliate_instance.to_dict()
# create an instance of SyndicationSettingsQrCodeOptionsAffiliate from a dict
syndication_settings_qr_code_options_affiliate_from_dict = SyndicationSettingsQrCodeOptionsAffiliate.from_dict(syndication_settings_qr_code_options_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


