class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = 0 # Битовый массив.

    def hash1(self, str1):
        calculated_hash = 0
        for c in str1:
            code = ord(c)
            calculated_hash = (calculated_hash * 17 + code) % self.filter_len
        return 1 << calculated_hash 

    def hash2(self, str1):
        calculated_hash = 0
        for c in str1:
            code = ord(c)
            calculated_hash = (calculated_hash * 223 + code) % self.filter_len
        return 1 << calculated_hash 

    def add(self, str1):
        hash_results = self.hash1(str1) | self.hash2(str1)
        self.bit_array |= hash_results

    def is_value(self, str1):
        hash_results = self.hash1(str1) | self.hash2(str1)
        return self.bit_array & hash_results == hash_results
