from pytest import fixture

from gateways.mongo import Mongo


@fixture(scope="session")
def mongo():
    return Mongo().connection
