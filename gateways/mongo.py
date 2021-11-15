from mongoengine import connect


class Mongo:
    _connection = None

    def _connect(self):
        return connect(
            db='testing_lecture',
            username='admin',
            password='1337',
            authentication_source='admin'
        )

    @property
    def connection(self):
        if not self._connection:
            self.__class__._connection = self._connect()
        return self._connection
