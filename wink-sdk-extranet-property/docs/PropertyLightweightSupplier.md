# PropertyLightweightSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | Unique hotel identifier | 
**name** | **str** | Unique hotel trade name. The hotel name must be unique. If there are multiple hotels with the same name, we recommend appending destination to the name. [Verify uniqueness here](#operation/isHotelNameUnique). | 
**url_name** | **str** | Unique url-friendly slug to identify property | 
**currency_code** | **str** | Currency code | 
**status** | **str** | wink.travel sets this status as the hotel moves through the payment workflow and manually for approval. | [default to 'APPROVED']
**external_status** | **str** | Property goes active by changing externalStatus. | [default to 'ACTIVE']
**stars** | **int** | Hotel star rating. | [optional] 
**number_of_rooms** | **int** | Number of rooms / keys for property | 
**active** | **bool** | Property is both approved and activated. | [optional] 
**platform_active** | **bool** | Platform approved property. | [optional] 
**property_active** | **bool** | Property activated itself and went live. | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.property_lightweight_supplier import PropertyLightweightSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyLightweightSupplier from a JSON string
property_lightweight_supplier_instance = PropertyLightweightSupplier.from_json(json)
# print the JSON string representation of the object
print(PropertyLightweightSupplier.to_json())

# convert the object into a dict
property_lightweight_supplier_dict = property_lightweight_supplier_instance.to_dict()
# create an instance of PropertyLightweightSupplier from a dict
property_lightweight_supplier_from_dict = PropertyLightweightSupplier.from_dict(property_lightweight_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


