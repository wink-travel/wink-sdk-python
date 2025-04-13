[![wink.travel logo](https://res.cloudinary.com/traveliko/image/upload/c_scale,h_75/v1653285543/wink/logo_text.png)](https://wink.travel)

# Wink Python SDK

Welcome to the Python SDK that enables you to communicate with all that the Wink Travel Platform has to offer.

## Getting started
This SDK contains libraries you can leverage to communicate with the Wink platform.

### Python Requirements
Python 3.8+

Download libraries from PyPi.

## Affiliate

[API and SDK documentation](wink-sdk-affiliate/README.md)

The Affiliate API exposes endpoints to manage affiliate accounts. This API lets you:

 - Create affiliates.
 - Create account managers.

#### API's

- AffiliateApi: Create affiliates. 
- AccountManagerApi: Create account managers.

#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-affiliate)

You can install the package from PyPi using:
```sh
pip install wink_sdk_affiliate
```


## Affiliate Browse

[API and SDK documentation](wink-sdk-affiliate-browse/README.md)

The Affiliate Browse API exposes endpoints for affiliates to browse inventory. This API lets you:

- Browse suppliers and inventory.
- Retrieve categories to search for.
- Manage curated lists.
- Manage saved searches.


#### API's

- BrowseApi: Browse suppliers and invnentory. 
- CuratedListApi: Manage curated lists.
- SavedSearchApi: Manage saved searches.
- SearchCategoriesApi: Retrieve categories to search for.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-affiliate-browse)

You can install the package from PyPi using:
```sh
pip install wink_sdk_affiliate_browse
```



## Affiliate Inventory

[API and SDK documentation](wink-sdk-affiliate-inventory/README.md)

The Affiliate Inventory API exposes endpoints for affiliates to manage the inventory they want to sell and how they want to sell it. This API lets you:

- Manage customizations.
- Manage shareable supplier / inventory links.
- Manage individual inventory items.
- Manage curated / saved searches / ranked grids.
- Manage maps.


#### API's

- CustomizationApi: Manage customizations. 
- EmbeddableInventoriesApi: Mostly used by our Web Components to retrieve available inventory to embed 
- ItemsApi: Manage individual inventory items.
- GridsApi: Manage curated + saved searches grids.
- MapsApi: Manage maps.
- InventoryLinksApi: Manage shareable inventory links.
- RankedGridsApi: Manage ranked grids.
- SupplierLinksApi: Manage shareable supplier links.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-affiliate-inventory)

You can install the package from PyPi using:
```sh
pip install wink_sdk_affiliate_inventory
```



## Affiliate Sales Channel

[API and SDK documentation](wink-sdk-affiliate-sales-channel/README.md)

The Sales Channel API exposes endpoints for affiliates to manage existing sales channels as well as find new ones. This API lets you:

 - Sales Channel: Manage existing sales channels.
 - Relationship Request: Manage relationship requests.
 - Available Supplier: Browse available suppliers to connect with.


#### API's

- AvailableSupplierApi: Browse available suppliers to connect with.
- RelationshipRequestApi: Manage relationship requests. 
- SalesChannelApi: Manage existing sales channels.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-affiliate-sales-channel)

You can install the package from PyPi using:
```sh
pip install wink_sdk_affiliate_sales_channel
```



## Affiliate WinkLinks

[API and SDK documentation](wink-sdk-affiliate-winklinks/README.md)

The WinkLinks API exposes endpoints to manage WinkLink entries, categories and settings. This API lets you:

 - Entries: Manage WinkLinks entries.
 - Categories: Manage WinkLinks tags.
 - Settings: Configure WinkLinks account.


#### API's

- SyndicationPublisherApi: Manage your WinkLinks account


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-affiliate-winklinks)

You can install the package from PyPi using:
```sh
pip install wink_sdk_affiliate_winklinks
```



## Analytics

[API and SDK documentation](wink-sdk-analytics/README.md)

The Analytics API gives you access to time series data on a variety of data sources to measure bookings and insights on properties, affiliates and traveler data.


#### API's

- AnalyticsApi: Create analytics that is meaningful to you. We provide the filters, sorting mechanisms and data points you need to track everything you want on our platform.
- LeaderboardApi: Track where you stand compared to other affiliates. The metric is bookings.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-analytics)

You can install the package from PyPi using:
```sh
pip install wink_sdk_analytics
```



## Booking

[API and SDK documentation](wink-sdk-booking/README.md)

Welcome to the Booking Engine API - A programmer-friendly way to book inventory that was found on our platform. This API lets you:

- Shopping Cart: Manage shopping cart.
- Checkout: Move shopping cart items through the payment workflow.
- Booking: Move selected inventory through to booking completion.
- Review: Leave a review after a completed stay. 


#### API's

- ShoppingCartApi: Manage shopping cart.
- CheckoutApi: Move shopping cart items through the payment workflow.
- BookingApi: Manage bookings.
- ReviewApi: Leave a review after a completed stay.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-booking)

You can install the package from PyPi using:
```sh
pip install wink_sdk_booking
```



## Channel manager

[API and SDK documentation](wink-sdk-channel-manager/README.md)

The Channel Manager API enables external channel manager partners to map, exchange rate / availability information with us as well as be informed of bookings that occur on the Wink platform for one of their properties.  


#### API's

- ChannelManagerApi: Everything related to pushing rates and availability as well as querying properties managed by your channel manager account with us.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-channel-manager)

You can install the package from PyPi using:
```sh
pip install wink_sdk_channel_manager
```



## Booking Engine Client

[API and SDK documentation](wink-sdk-engine-client/README.md)

A single endpoint to retrieve affiliate information needed to display the booking engine.


#### API's

- ConfigurationApi: Load affiliate information


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-engine-client)

You can install the package from PyPi using:
```sh
pip install wink_sdk_engine_client
```



## Extranet Booking

[API and SDK documentation](wink-sdk-extranet-booking/README.md)

The Booking API exposes endpoints to manage bookings. This API lets you:

- Booking: Manage bookings including cancellations.
- Review: Manage and respond to user reviews.
- Sync w. Calendar: Manage calendar sync with your favorite calendar software.


#### API's

- BookingApi: Manage bookings including cancellations.
- ReviewApi: Manage and respond to user reviews.
- CalendarSyncApi: Sync w. Calendar: Manage calendar sync with your favorite calendar software.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-extranet-booking)

You can install the package from PyPi using:
```sh
pip install wink_sdk_extranet_booking
```



## Extranet Distribution

[API and SDK documentation](wink-sdk-extranet-distribution/README.md)

The Distribution API exposes endpoints for sales channels, connecting with affiliates, managing rates and inventory calendars and more on Wink. This API lets you:

1. Verifier: Test your availability and promotions and create test bookings to simulate the entire booking workflow.
2. Sales Channels: Manage your sales channels.
3. Explore Network: Find new affiliates to work with.
4. Inventory: Manage inventory at the sales channel-level.
5. Calendars: Manage availability calendars for all your inventory.


#### API's

- AffiliateApi: Browse affiliates.
- DailyRateApi: Manage room type / rate plan rates
- InventoryApi: Manage inventory at the sales channel-level.
- InventoryUsageApi: Track current inventory usage.
- SalesChannelApi: Manage sales channels.
- SchedulerApi: Manage availability for all non-room type inventory.
- SalesChannelRelationshipRequestsApi: Manage affiliate relationship requests.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-extranet-distribution)

You can install the package from PyPi using:
```sh
pip install wink_sdk_extranet_distribution
```



## Extranet Experiences

[API and SDK documentation](wink-sdk-extranet-experiences/README.md)

This part of the documentation concerns itself with the management of experiences, on and off the property. This API lets you create:

- Activities: Manage activities on and off the premises.
- Attractions: Manage attractions on and off the premises.
- Places: Manage places on and off the premises.


#### API's

- ActivityApi: Manage activities on and off the premises.
- AttractionApi: Manage attractions on and off the premises.
- PlaceApi: Manage places on and off the premises.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-extranet-experiences)

You can install the package from PyPi using:
```sh
pip install wink_sdk_extranet_experiences
```



## Extranet Facilities

[API and SDK documentation](wink-sdk-extranet-facilities/README.md)

This part of the documentation concerns itself with the management of facilities, on and off the property. This API lets you create:

- Guest room: Manage room types on and off the premises.
- Meeting room: Manage meeting rooms on and off the premises.
- Restaurant: Manage restaurants on and off the premises.
- Spa: Manage spas on and off the premises.


#### API's

- GuestRoomApi: Manage room types on and off the premises.
- MeetingRoomApi: Manage meeting rooms on and off the premises.
- RestaurantApi: Manage restaurants on and off the premises.
- SpaApi: Manage spas on and off the premises.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-extranet-facilities)

You can install the package from PyPi using:
```sh
pip install wink_sdk_extranet_facilities
```



## Extranet Monetize

[API and SDK documentation](wink-sdk-extranet-monetize/README.md)

This part of the documentation concerns itself with the management of cancellation policies, promotions, restrictions etc. This API lets you create:

- Add-ons: Manage add-ons.
- Cancellation policies: Manage cancellation policies for your property.
- Master rates: Manage perks for room type / rate plan combos.
- Promotions: Manage promotions.
- Promotion bundle: Manage bundled promotions.
- Rate plan: Manage rate plans.


#### API's

- AddOnApi: Manage add-ons.
- CancellationPolicyApi: Manage cancellation policies for your property.
- MasterRateApi: Manage perks for room type / rate plan combos.
- PromotionApi: Manage promotions.
- PromotionBundleApi: Manage bundled promotions.
- RatePlanApi: Manage rate plans.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-extranet-monetize)

You can install the package from PyPi using:
```sh
pip install wink_sdk_extranet_monetize
```



## Extranet Property

[API and SDK documentation](wink-sdk-extranet-property/README.md)

This part of the documentation concerns itself with basic property management. It can:

- Property: List existing properties. Manage property status. Change name and similar.
- Notification: Read internal messages sent from Wink to your properties.
- Announcement: Show pertinent messages to travelers in a pop-up window.
- Geo-Location: Set property geo-location.
- Green Index: Answer eco-related questions regarding the property's recycling practices and much more.
- Lifestyles: Manage lifestyles the property caters to.
- Photos / Videos: Manage property media.
- Policy: Manage property policy. I.e. Children, pets, wi-fi, parking etc.
- Reputation: Manage awards, online / offline ratings etc.
- Services: Manage property amenities.
- Social media: Manage property social media networks.
- Welcome text: Manage property descriptions


#### API's

- AnnouncementApi: Manage announcements to travelers in a pop-up window.
- ChannelManagerApi: Set channel manager
- GeoLocationApi: Set property geo-location.
- LifestyleApi: Manage lifestyles the property caters to.
- MediaApi: Manage property media.
- PolicyApi: Manage property policy. I.e. Children, pets, wi-fi, parking etc.
- PropertyApi: List existing properties. Manage property status. Change name and similar.
- RecognitionApi: Manage awards, online / offline ratings etc.
- SocialNetworkApi: Manage property social media networks.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-extranet-property)

You can install the package from PyPi using:
```sh
pip install wink_sdk_extranet_property
```



## Extranet Property Register

[API and SDK documentation](wink-sdk-extranet-property-register/README.md)

This part of the documentation concerns itself about adding new properties to Wink. There are two endpoints for you to onboard a property:

- Manage leads.
- Manually: Use this endpoint if you already have all the property data. Use case: You want to migrate your existing properties to Wink.
- Intelligently: With the assistance of Google Business Pages, you can select an existing property on Google, ingest it with the lead endpoint and let us create a Wink property for you. Note: This isn't always straightforward in places with non-standard addresses.


#### API's

- ManageLeadsApi: Manage leads.
- PropertyRegistrationApi: Create properties.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-extranet-property-register)

You can install the package from PyPi using:
```sh
pip install wink_sdk_extranet_property_register
```



## Inventory

[API documentation](wink-sdk-inventory/README.md)

The Inventory API exposes endpoints to retrieve inventory you already know about. This API lets you:

- Consume shareable links.
- Load up a known property with availability.
- Load up all inventories that were created by our affiliates such as grids, maps, and individual items.


#### API's

- InventoryApi: Everything related to querying property availability.
- ShareableLinkApi: Consume shareable links.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-inventory)

You can install the package from PyPi using:
```sh
pip install wink_sdk_inventory
```



## Lookup

[API and SDK documentation](wink-sdk-lookup/README.md)

The Lookup API exposes endpoints to search for inventory by region, type. It's the entryway to bookable inventory when you don't yet know what you are looking for.


#### API's

- LookupApi: Everything related to querying for best priced room types using various filter mechanisms


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-lookup)

You can install the package from PyPi using:
```sh
pip install wink_sdk_lookup
```



## Notification

[API and SDK documentation](wink-sdk-notification/README.md)

The Notifications API is a way for us to stay in touch with your user, property or affiliate account.


#### API's

- NotificationApi: Retrieve platform notifications.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-notification)

You can install the package from PyPi using:
```sh
pip install wink_sdk_notification
```



## Ping

[API and SDK documentation](wink-sdk-ping/README.md)

Easy way to test your credentials.


#### API's

- PingApi: Test connection with Wink.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-ping)

You can install the package from PyPi using:
```sh
pip install wink_sdk_ping
```



## Reference

[API and SDK documentation](wink-sdk-reference/README.md)

The Reference API exposes endpoints related to supported taxonomies of reference data that this platform supports.


#### API's

- GeoDataApi: Find geo-name lookup data from geonames.org.
- ReferenceApi: Everything related to structured datasets and their meaning. E.g. OTA Room View Code list


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-reference)

You can install the package from PyPi using:
```sh
pip install wink_sdk_reference
```



## Travel Agent

[API and SDK documentation](wink-sdk-travel-agent/README.md)

The Travel Agent API exposes endpoints to manage agent-facilitated bookings. This API lets you:

- Travel Agent: Manage agent entity.
- Booking: Create / Manage bookings


#### API's

- TravelAgentApi: Create agents and manage bookings.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-travel-agent)

You can install the package from PyPi using:
```sh
pip install wink_sdk_travel_agent
```



## User Settings

[API and SDK documentation](wink-sdk-user-settings/README.md)

The User Settings API exposes endpoints to allow 3rd party integrators to communicate with Wink. This API lets you:

- Application: Manage 3rd party access to Wink.
- Bucket List: Manage your bucket list on Wink.
- User: Manage user settings.
- Webhook: Subscribe to receive Wink events as they occur in realtime.


#### API's

- ApplicationApi: Manage 3rd party access to Wink.
- BucketListApi: Manage your bucket list on Wink.
- UserSettingsApi: Manage user settings.
- WebhookApi: Subscribe to receive Wink events as they occur in realtime.


#### How to install

[PyPi URL](https://pypi.org/project/wink-sdk-user-settings)

You can install the package from PyPi using:
```sh
pip install wink_sdk_user_settings
```



## Configuration
You will need a client ID and a client secret to communicate with any of the Wink platform endpoints. You can create your account and get your credentials here:

[https://sell.wink.travel](https://sell.wink.travel)

Steps: 
1. Register your personal user account
2. Log in
3. Create your first account
4. Select that account
5. Choose to create an Application for that account 
6. The application will hold your credentials

Using the client ID and client secret, you can create the OAUTH2 access token. Instructions to create the access token you can find in the API docs Authentication section, eg.
[https://docs.wink.travel/affiliate](https://docs.wink.travel/affiliate)


### ENV variables
Create the access token environment variable in your preferred way:

1. ACCESS_TOKEN=YOUR_ACCESS_TOKEN


## You might also be interested in...
- TripPay Python SDK Repo: [https://github.com/wink-travel/trip-pay-sdk-python](https://github.com/wink-travel/trip-pay-sdk-python)
- WordPress: [https://wordpress.org/plugins/wink2travel/](https://wordpress.org/plugins/wink2travel/) 
