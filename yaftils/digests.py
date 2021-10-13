#!/usr/bin/env python3
from enum import Enum
import re
import logging

logger = logging.getLogger(__name__)


class HashKind(Enum):
    '''
        contradiction
    '''
    UNK = r"\b\B"
    MD5 = r"^[a-fA-F0-9]{32}$"
    SHA1 = r"^[a-fA-F0-9]{40}$"
    SHA256 = r"^[a-fA-F0-9]{64}$"


def recog_hash(val: str) -> HashKind:
    for hk in HashKind:
        result = re.match(hk.value, val)
        if result:
            return hk
    logger.warning("hash recog fail: %s is not known hash format" % (val))
    return HashKind.UNK


if __name__ == "__main__":
    pass
