# ApiUrls

## 概要

- 任意のAPIのドメインクラスを作成するためのミックスイン

### 使用方法

- ReadOnlyなAPIエンドポイントを保持するクラスを作成

```
>>> from apiurls.api_urls import ApiUrlsMixin
>>> from apiurls.sub_directories import SubDirecotries
>>> class SampleAPI(ApiUrlsMixin):
...     _protocol = 'https'
...     _domain = 'sample.com'
...     _sub_directories = SubDirecotries(
...         {
...             'item_create':'/user/create',
...             'item_update': '/item/update/',
...             'items_list': 'items/list',
...         }
...     )
... 
>>> sample_api = SampleAPI() 
>>> sample_api.item_create
'https://sample.com/user/create'
>>> sample_api.item_update
'https://sample.com/item/update/'
>>> sample_api.items_list    
'https://sample.comitems/list'
```