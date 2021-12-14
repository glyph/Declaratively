from declaratively import DeclarationCollection
from dataclasses import dataclass


@dataclass
class SQLRunner(object):
    sql_string: str

    def run(self, cursor, *anon, **named):
        if anon and named:
            raise Exception("Pick a style.")
        params = anon or named
        return cursor.execute(self.sql_string, params)


def _nothing(namespace: str) -> None:
    return None


def _makeRunner(namespace: str, nstype: None, spec: str) -> SQLRunner:
    return SQLRunner(spec)


sql_statements = DeclarationCollection("SQL statements", _makeRunner, _nothing)
