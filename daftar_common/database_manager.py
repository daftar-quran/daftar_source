import json
from datetime import datetime
from decimal import Decimal

from daftar_common.helper_functions import datetime_to_string, replace_decimals


class TableManager:
    def __init__(self, dynamo_resource, table_name):
        self.dynamo = dynamo_resource
        self.table = self.dynamo.Table(table_name)

    def add_item(self, item: dict):
        # UTC to ISO 8601 with Local TimeZone information without microsecond
        created_date = datetime_to_string(datetime.utcnow())
        item["createdDate"] = created_date

        item = json.loads(json.dumps(item), parse_float=Decimal)

        expected_dict = {"id": {"Exists": False}}

        self.table.put_item(Item=item, Expected=expected_dict)

        return True


    def get_item_by_id(self, id_item: str, id_name='id'):
        response = self.table.get_item({id_name: id_item})
        return replace_decimals(response.get('Item', {}))

    def scan_table(self, filter_expression=None, projection_expression=None, limit=None):
        """
        Be cautious with this method
        """
        scan_kwargs = {}
        if filter_expression:
            scan_kwargs['FilterExpression'] = filter_expression
        if projection_expression:
            scan_kwargs['ProjectionExpression'] = projection_expression
        if limit:
            scan_kwargs['Limit'] = limit

        response = self.table.scan(**scan_kwargs)

        items = response.get('Items', [])
        while 'LastEvaluatedKey' in response:
            scan_kwargs['ExclusiveStartKey'] = response['LastEvaluatedKey']
            response = self.table.scan(**scan_kwargs)
            items.extend(response.get('Items', []))

        return [replace_decimals(item) for item in items]


