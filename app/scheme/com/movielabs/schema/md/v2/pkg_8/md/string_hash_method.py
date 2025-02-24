from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringHashMethod(Enum):
    C4 = "C4"
    CRC16 = "CRC16"
    CRC32 = "CRC32"
    CRC64 = "CRC64"
    MD2 = "MD2"
    MD4 = "MD4"
    MD5 = "MD5"
    SHA_0 = "SHA-0"
    SHA_1 = "SHA-1"
    SHA_2 = "SHA-2"
    SHA_3 = "SHA-3"
