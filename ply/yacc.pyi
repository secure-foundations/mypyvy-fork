from typing import Any, Optional

class LRParser:
    def parse(self, input: Optional[str]=None, lexer: Any=None, debug: bool=False, tracking: bool=False, tokenfunc: Any=None, filename: Optional[str]=None) -> Any: ...

def yacc(start: Optional[str]=None, errorlog: Any=None, debug: bool=True, forbid_rebuild: bool=False) -> LRParser: ...

class NullLogger(object): ...
