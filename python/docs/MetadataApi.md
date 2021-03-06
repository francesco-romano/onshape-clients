# onshape_client.oas.MetadataApi

All URIs are relative to *https://cad.onshape.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_veop_standard_content_metadata**](MetadataApi.md#get_veop_standard_content_metadata) | **GET** /api/metadata/standardcontent/d/{did}/v/{vid}/e/{eid}/{otype}/{oid}/p/{pid} | 
[**get_wmve_ps_metadata**](MetadataApi.md#get_wmve_ps_metadata) | **GET** /api/metadata/d/{did}/{wvm}/{wvmid}/e/{eid}/p | 
[**get_wmvep_metadata**](MetadataApi.md#get_wmvep_metadata) | **GET** /api/metadata/d/{did}/{wvm}/{wvmid}/e/{eid}/p/{pid} | 
[**get_wv_es_metadata**](MetadataApi.md#get_wv_es_metadata) | **GET** /api/metadata/d/{did}/{wv}/{wvid}/e | 
[**get_wv_metadata**](MetadataApi.md#get_wv_metadata) | **GET** /api/metadata/d/{did}/{wv}/{wvid} | 
[**get_wve_metadata**](MetadataApi.md#get_wve_metadata) | **GET** /api/metadata/d/{did}/{wv}/{wvid}/e/{eid} | 
[**update_veop_standard_content_part_metadata**](MetadataApi.md#update_veop_standard_content_part_metadata) | **POST** /api/metadata/standardcontent/d/{did}/v/{vid}/e/{eid}/{otype}/{oid}/p/{pid} | 
[**update_wv_metadata**](MetadataApi.md#update_wv_metadata) | **POST** /api/metadata/d/{did}/{wv}/{wvid} | 
[**update_wve_metadata**](MetadataApi.md#update_wve_metadata) | **POST** /api/metadata/d/{did}/{wv}/{wvid}/e/{eid} | 
[**update_wvep_metadata**](MetadataApi.md#update_wvep_metadata) | **POST** /api/metadata/d/{did}/{wvm}/{wvmid}/e/{eid}/p/{pid} | 


# **get_veop_standard_content_metadata**
> get_veop_standard_content_metadata(did, vid, eid, otype, oid, pid, configuration=configuration, link_document_id=link_document_id)



### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import onshape_client.oas
from onshape_client.oas.rest import ApiException
from pprint import pprint
configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"
# Create an instance of the API class
api_instance = onshape_client.oas.MetadataApi(onshape_client.oas.ApiClient(configuration))
did = 'did_example' # str | 
vid = 'vid_example' # str | 
eid = 'eid_example' # str | 
otype = 'otype_example' # str | 
oid = 'oid_example' # str | 
pid = 'pid_example' # str | 
configuration = 'configuration_example' # str |  (optional)
link_document_id = 'link_document_id_example' # str |  (optional)

try:
    api_instance.get_veop_standard_content_metadata(did, vid, eid, otype, oid, pid, configuration=configuration, link_document_id=link_document_id)
except ApiException as e:
    print("Exception when calling MetadataApi->get_veop_standard_content_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **vid** | **str**|  | 
 **eid** | **str**|  | 
 **otype** | **str**|  | 
 **oid** | **str**|  | 
 **pid** | **str**|  | 
 **configuration** | **str**|  | [optional] 
 **link_document_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8;qs=0.1, application/json;charset=UTF-8; qs=0.09

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmve_ps_metadata**
> get_wmve_ps_metadata(did, wvm, wvmid, eid, configuration=configuration, link_document_id=link_document_id, infer_metadata_owner=infer_metadata_owner)



### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import onshape_client.oas
from onshape_client.oas.rest import ApiException
from pprint import pprint
configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"
# Create an instance of the API class
api_instance = onshape_client.oas.MetadataApi(onshape_client.oas.ApiClient(configuration))
did = 'did_example' # str | 
wvm = 'wvm_example' # str | 
wvmid = 'wvmid_example' # str | 
eid = 'eid_example' # str | 
configuration = 'configuration_example' # str |  (optional)
link_document_id = 'link_document_id_example' # str |  (optional)
infer_metadata_owner = False # bool |  (optional) (default to False)

try:
    api_instance.get_wmve_ps_metadata(did, wvm, wvmid, eid, configuration=configuration, link_document_id=link_document_id, infer_metadata_owner=infer_metadata_owner)
except ApiException as e:
    print("Exception when calling MetadataApi->get_wmve_ps_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wvm** | **str**|  | 
 **wvmid** | **str**|  | 
 **eid** | **str**|  | 
 **configuration** | **str**|  | [optional] 
 **link_document_id** | **str**|  | [optional] 
 **infer_metadata_owner** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8;qs=0.1, application/json;charset=UTF-8; qs=0.09

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmvep_metadata**
> get_wmvep_metadata(did, wvm, wvmid, eid, pid, configuration=configuration, link_document_id=link_document_id, infer_metadata_owner=infer_metadata_owner)



### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import onshape_client.oas
from onshape_client.oas.rest import ApiException
from pprint import pprint
configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"
# Create an instance of the API class
api_instance = onshape_client.oas.MetadataApi(onshape_client.oas.ApiClient(configuration))
did = 'did_example' # str | 
wvm = 'wvm_example' # str | 
wvmid = 'wvmid_example' # str | 
eid = 'eid_example' # str | 
pid = 'pid_example' # str | 
configuration = 'configuration_example' # str |  (optional)
link_document_id = 'link_document_id_example' # str |  (optional)
infer_metadata_owner = False # bool |  (optional) (default to False)

try:
    api_instance.get_wmvep_metadata(did, wvm, wvmid, eid, pid, configuration=configuration, link_document_id=link_document_id, infer_metadata_owner=infer_metadata_owner)
except ApiException as e:
    print("Exception when calling MetadataApi->get_wmvep_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wvm** | **str**|  | 
 **wvmid** | **str**|  | 
 **eid** | **str**|  | 
 **pid** | **str**|  | 
 **configuration** | **str**|  | [optional] 
 **link_document_id** | **str**|  | [optional] 
 **infer_metadata_owner** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8;qs=0.1, application/json;charset=UTF-8; qs=0.09

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wv_es_metadata**
> get_wv_es_metadata(did, wv, wvid, link_document_id=link_document_id, infer_metadata_owner=infer_metadata_owner)



### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import onshape_client.oas
from onshape_client.oas.rest import ApiException
from pprint import pprint
configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"
# Create an instance of the API class
api_instance = onshape_client.oas.MetadataApi(onshape_client.oas.ApiClient(configuration))
did = 'did_example' # str | 
wv = 'wv_example' # str | 
wvid = 'wvid_example' # str | 
link_document_id = 'link_document_id_example' # str |  (optional)
infer_metadata_owner = False # bool |  (optional) (default to False)

try:
    api_instance.get_wv_es_metadata(did, wv, wvid, link_document_id=link_document_id, infer_metadata_owner=infer_metadata_owner)
except ApiException as e:
    print("Exception when calling MetadataApi->get_wv_es_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wv** | **str**|  | 
 **wvid** | **str**|  | 
 **link_document_id** | **str**|  | [optional] 
 **infer_metadata_owner** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8;qs=0.1, application/json;charset=UTF-8; qs=0.09

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wv_metadata**
> get_wv_metadata(did, wv, wvid, link_document_id=link_document_id, infer_metadata_owner=infer_metadata_owner)



### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import onshape_client.oas
from onshape_client.oas.rest import ApiException
from pprint import pprint
configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"
# Create an instance of the API class
api_instance = onshape_client.oas.MetadataApi(onshape_client.oas.ApiClient(configuration))
did = 'did_example' # str | 
wv = 'wv_example' # str | 
wvid = 'wvid_example' # str | 
link_document_id = 'link_document_id_example' # str |  (optional)
infer_metadata_owner = False # bool |  (optional) (default to False)

try:
    api_instance.get_wv_metadata(did, wv, wvid, link_document_id=link_document_id, infer_metadata_owner=infer_metadata_owner)
except ApiException as e:
    print("Exception when calling MetadataApi->get_wv_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wv** | **str**|  | 
 **wvid** | **str**|  | 
 **link_document_id** | **str**|  | [optional] 
 **infer_metadata_owner** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8;qs=0.1, application/json;charset=UTF-8; qs=0.09

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wve_metadata**
> get_wve_metadata(did, wv, wvid, eid, configuration=configuration, link_document_id=link_document_id, infer_metadata_owner=infer_metadata_owner)



### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import onshape_client.oas
from onshape_client.oas.rest import ApiException
from pprint import pprint
configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"
# Create an instance of the API class
api_instance = onshape_client.oas.MetadataApi(onshape_client.oas.ApiClient(configuration))
did = 'did_example' # str | 
wv = 'wv_example' # str | 
wvid = 'wvid_example' # str | 
eid = 'eid_example' # str | 
configuration = 'configuration_example' # str |  (optional)
link_document_id = 'link_document_id_example' # str |  (optional)
infer_metadata_owner = False # bool |  (optional) (default to False)

try:
    api_instance.get_wve_metadata(did, wv, wvid, eid, configuration=configuration, link_document_id=link_document_id, infer_metadata_owner=infer_metadata_owner)
except ApiException as e:
    print("Exception when calling MetadataApi->get_wve_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wv** | **str**|  | 
 **wvid** | **str**|  | 
 **eid** | **str**|  | 
 **configuration** | **str**|  | [optional] 
 **link_document_id** | **str**|  | [optional] 
 **infer_metadata_owner** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8;qs=0.1, application/json;charset=UTF-8; qs=0.09

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_veop_standard_content_part_metadata**
> update_veop_standard_content_part_metadata(did, vid, eid, otype, oid, pid, body, link_document_id=link_document_id)



### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import onshape_client.oas
from onshape_client.oas.rest import ApiException
from pprint import pprint
configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"
# Create an instance of the API class
api_instance = onshape_client.oas.MetadataApi(onshape_client.oas.ApiClient(configuration))
did = 'did_example' # str | 
vid = 'vid_example' # str | 
eid = 'eid_example' # str | 
otype = 'otype_example' # str | 
oid = 'oid_example' # str | 
pid = 'pid_example' # str | 
body = 'body_example' # str | 
link_document_id = 'link_document_id_example' # str |  (optional)

try:
    api_instance.update_veop_standard_content_part_metadata(did, vid, eid, otype, oid, pid, body, link_document_id=link_document_id)
except ApiException as e:
    print("Exception when calling MetadataApi->update_veop_standard_content_part_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **vid** | **str**|  | 
 **eid** | **str**|  | 
 **otype** | **str**|  | 
 **oid** | **str**|  | 
 **pid** | **str**|  | 
 **body** | **str**|  | 
 **link_document_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8; qs=0.09
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8;qs=0.1, application/json;charset=UTF-8; qs=0.09

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wv_metadata**
> update_wv_metadata(did, wv, wvid, body)



### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import onshape_client.oas
from onshape_client.oas.rest import ApiException
from pprint import pprint
configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"
# Create an instance of the API class
api_instance = onshape_client.oas.MetadataApi(onshape_client.oas.ApiClient(configuration))
did = 'did_example' # str | 
wv = 'wv_example' # str | 
wvid = 'wvid_example' # str | 
body = 'body_example' # str | 

try:
    api_instance.update_wv_metadata(did, wv, wvid, body)
except ApiException as e:
    print("Exception when calling MetadataApi->update_wv_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wv** | **str**|  | 
 **wvid** | **str**|  | 
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8; qs=0.09
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8;qs=0.1, application/json;charset=UTF-8; qs=0.09

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wve_metadata**
> update_wve_metadata(did, wv, wvid, eid, body)



### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import onshape_client.oas
from onshape_client.oas.rest import ApiException
from pprint import pprint
configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"
# Create an instance of the API class
api_instance = onshape_client.oas.MetadataApi(onshape_client.oas.ApiClient(configuration))
did = 'did_example' # str | 
wv = 'wv_example' # str | 
wvid = 'wvid_example' # str | 
eid = 'eid_example' # str | 
body = 'body_example' # str | 

try:
    api_instance.update_wve_metadata(did, wv, wvid, eid, body)
except ApiException as e:
    print("Exception when calling MetadataApi->update_wve_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wv** | **str**|  | 
 **wvid** | **str**|  | 
 **eid** | **str**|  | 
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8; qs=0.09
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8;qs=0.1, application/json;charset=UTF-8; qs=0.09

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wvep_metadata**
> update_wvep_metadata(did, wvm, wvmid, eid, pid, sub_resource, body)



### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import onshape_client.oas
from onshape_client.oas.rest import ApiException
from pprint import pprint
configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"
# Create an instance of the API class
api_instance = onshape_client.oas.MetadataApi(onshape_client.oas.ApiClient(configuration))
did = 'did_example' # str | 
wvm = 'wvm_example' # str | 
wvmid = 'wvmid_example' # str | 
eid = 'eid_example' # str | 
pid = 'pid_example' # str | 
sub_resource = 'sub_resource_example' # str | 
body = 'body_example' # str | 

try:
    api_instance.update_wvep_metadata(did, wvm, wvmid, eid, pid, sub_resource, body)
except ApiException as e:
    print("Exception when calling MetadataApi->update_wvep_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wvm** | **str**|  | 
 **wvmid** | **str**|  | 
 **eid** | **str**|  | 
 **pid** | **str**|  | 
 **sub_resource** | **str**|  | 
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8; qs=0.09
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8;qs=0.1, application/json;charset=UTF-8; qs=0.09

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

