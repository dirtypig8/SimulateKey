class QueryDataHandler:
    query_result = dict()
    process_status = None
    @staticmethod
    def clear_all_fields():
        QueryDataHandler.query_result = dict()
