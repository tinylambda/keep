import copy
import typing


class EntityESOperationMixin:
    SEARCH_BODY = {"query": {"bool": {"must": [], "filter": []}}}

    async def entity_create(self, entity_body: typing.Dict) -> typing.AnyStr:
        """return unique id of new created entity"""
        r = await self.storage.index(index=self.DB_NAME, body=entity_body, refresh=True)
        unique_id = r["_id"]
        return unique_id

    async def entity_update(self, unique_id: typing.AnyStr, entity_body: typing.Dict):
        r = await self.storage.update(
            index=self.DB_NAME, id=unique_id, body={"doc": entity_body}
        )

    async def entity_delete(self, unique_id):
        """physically or logically"""
        r = await self.storage.delete(index=self.DB_NAME, id=unique_id)

    async def entity_get(self, unique_id) -> typing.Dict:
        """get entity by unique_id"""
        r = await self.storage.get(self.DB_NAME, id=unique_id)
        return r["_source"]

    async def entity_exists(self, unique_id):
        r = await self.storage.exists(self.DB_NAME, id=unique_id)
        return r

    async def entity_filter(self, conditions: typing.Dict) -> typing.List:
        search_body: typing.Dict = copy.deepcopy(self.SEARCH_BODY)
        for k, v in conditions.items():
            search_body["query"]["bool"]["filter"].append({"term": {k: v}})
        r = await self.storage.search(index=self.DB_NAME, body=search_body)
        return_data = []
        for item in r["hits"]["hits"]:
            doc: typing.Dict = item["_source"]
            doc.update({"id": item["_id"]})
            return_data.append(doc)
        return return_data
