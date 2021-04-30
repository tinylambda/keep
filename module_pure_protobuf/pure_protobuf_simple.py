from dataclasses import dataclass

from pure_protobuf.dataclasses_ import field, message
from pure_protobuf.types import int32


@message
@dataclass
class SearchRequest:
    query: str = field(1, default='')
    page_number: int32 = field(2, default=int32(0))
    result_per_page: int32 = field(3, default=int32(0))


if __name__ == '__main__':
    sr = SearchRequest(
        query='hello',
        page_number=int32(1),
        result_per_page=int32(10)
    )
    print(sr)
    print(sr.dumps())
    print(sr.dumps() == b'\x0A\x05hello\x10\x01\x18\x0A')

