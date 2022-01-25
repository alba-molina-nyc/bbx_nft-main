
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder as MyJSONEncoder
from .models import Item
from django.http import JsonResponse
from main_nft_app.models import Item, Collection

item_meta_data_json = serialize('json', Item.objects.all())
response = JsonResponse(item_meta_data_json, encoder=MyJSONEncoder)

[

item_meta_data_json = {
   "model":"main_nft_app.item",
   "pk":1,
   "fields":{
      "file":"https://lh3.googleusercontent.com/dD4Cu1DLdd4iPkokA4vsQNYuYKu3S1j8nXuIJ5aaRE6s-Fdve31EP9E7DSQGh3qJFzTyRWPAPdVU3IbedB3EPgBzHkTHStOgvKlMnw=w362",
      "name":"xxx",
      "details_link":"xxx",
      "description":"xxx",
      "properties":"xxx",
      "levels":"xxxx",
      "stats":"xx",
      "unlockable_content":true,
      "explicit_or_sensitive_content":true,
      "supply":1,
      "blockchain":"xxx",
      "user":1
   }
},
{
   "model":"main_nft_app.collection",
   "pk":3,
   "fields":{
      "collection":1,
      "collection_choice_text":"ssssss"
   }
},



]
