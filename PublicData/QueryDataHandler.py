class QueryDataHandler:
    query_result = dict()
    process_status = None
    parking_detail_label = None
    @staticmethod
    def clear_all_fields():
        QueryDataHandler.query_result = dict()
