import sys

from sqlalchemy.orm import registry as registry
from sqlalchemy.schema import MetaData

from app.core.config import ConstantInitalizer #noqa: F401
from app.core.const import ServiceConstant

_IS_PYTEST = False
if "pytest" in sys.modules:
    _IS_PYTEST = True

if _IS_PYTEST:
    metadata = MeataData(schema="test")
else:
    metadata = MetaData(schema=ServiceConstant.DB_SCHEMA)

registry = Registry(metadata=metadata)