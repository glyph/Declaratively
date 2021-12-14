from logging import Logger
from declaratively import DeclarationCollection
from dataclasses import dataclass


@dataclass
class LogEmitter(object):
    format_string: str
    logger: Logger

    def warning(self, *a):
        self.logger.warning(self.format_string, *a)


def _makeLogger(namespace: str) -> Logger:
    return Logger(namespace)

def _makeEmitter(namespace: str, nstype: Logger, spec: str) -> LogEmitter:
    return LogEmitter(spec, nstype)


log_messages = DeclarationCollection("log messages", _makeEmitter, _makeLogger)
