from asd.chapter_one.bloom import BloomFilter


def test_one():
    bloom_filter = BloomFilter(32)

    strings = ['0123456789', '1234567890', '2345678901','3456789012', '4567890123','5678901234',
               '6789012345','7890123456','8901234567','9012345678']

    for i in strings:
        bloom_filter.add(i)

    false_counter = 0
    for i in strings:
        if bloom_filter.is_value(i) is False:
            false_counter += 1

    assert false_counter == 0
