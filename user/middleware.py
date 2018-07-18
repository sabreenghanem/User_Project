from user import Session


class SqlAlchemySession:
    def __init__(self):
        self.Session = Session()

    def process_request(self, request):
        request.db_session = self.Session()
        return None

    def process_exception(self, request, exception):
        setattr(request, '_exception', exception)
        try:
            session = request.db_session
        except AttributeError:
            pass
        else:
            session.rollback()
        return None

    def process_response(self, request, response):
        try:
            session = request.db_session
        except AttributeError:
            return response
        else:
            if getattr(request, '_exception', None) is None:
                session.commit()
        session.close()
        return response