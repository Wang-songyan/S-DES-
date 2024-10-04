class SDES:
    def __init__(self):
        self.P10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]  # 10位置换
        self.P8 = [5, 2, 6, 3, 7, 4, 9, 8]  # 8位置换
        self.IP = [1, 5, 2, 0, 3, 7, 4, 6]  # 初始置换
        self.IPinv = [3, 0, 2, 4, 6, 1, 7, 5]  # 初始置换的逆
        self.EP = [3, 0, 1, 2, 1, 2, 3, 0]  # 扩展置换
        self.S0 = [
            [1, 0, 3, 2],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 0, 2]
        ]
        self.S1 = [
            [0, 1, 2, 3],
            [2, 3, 1, 0],
            [3, 0, 1, 2],
            [2, 1, 0, 3]
        ]
        self.P4 = [1, 3, 2, 0]  # 4位置换

    def validate_binary(self, binary_input, expected_length):
        """确保输入是特定长度的二进制字符串"""
        if not all(bit in ['0', '1'] for bit in binary_input):
            raise ValueError("输入仅可包含0或1")
        if len(binary_input) != expected_length:
            raise ValueError(f"输入需为{expected_length}位")

    def char_to_binary(self, char):
        """将字符转换为8位二进制字符串"""
        return format(ord(char), '08b')

    def binary_to_char(self, binary_str):
        """将8位二进制字符串还原为字符"""
        return chr(int(binary_str, 2))

    def permute_bits(self, bits, perm_table):
        """根据给定的置换表对位进行排列"""
        return [bits[i] for i in perm_table]

    def circular_left_shift(self, bit_string, shift_amount):
        """对位串进行循环左移"""
        return bit_string[shift_amount:] + bit_string[:shift_amount]

    def generate_keys(self, master_key):
        """生成两个子密钥"""
        key_permuted = self.permute_bits(master_key, self.P10)
        left_half, right_half = key_permuted[:5], key_permuted[5:]
        left_shifted, right_shifted = self.circular_left_shift(left_half, 1), self.circular_left_shift(right_half, 1)
        k1 = self.permute_bits(left_shifted + right_shifted, self.P8)
        left_shifted, right_shifted = self.circular_left_shift(left_shifted, 1), self.circular_left_shift(right_shifted, 1)
        k2 = self.permute_bits(left_shifted + right_shifted, self.P8)
        return k1, k2

    def sbox_lookup(self, sbox, bits):
        """S盒查找操作"""
        row, col = int(bits[0] + bits[3], 2), int(bits[1] + bits[2], 2)
        return format(sbox[row][col], '02b')

    def f_function(self, bit_data, key):
        """应用F函数并返回结果"""
        left_part, right_part = bit_data[:4], bit_data[4:]
        right_expanded = self.permute_bits(right_part, self.EP)
        xor_result = [str(int(right_expanded[i]) ^ int(key[i])) for i in range(8)]
        left_sbox_result = self.sbox_lookup(self.S0, xor_result[:4])
        right_sbox_result = self.sbox_lookup(self.S1, xor_result[4:])
        sbox_combined = left_sbox_result + right_sbox_result
        permuted_sbox_result = self.permute_bits(sbox_combined, self.P4)
        final_result = [str(int(left_part[i]) ^ int(permuted_sbox_result[i])) for i in range(4)]
        return final_result + right_part

    def encrypt_binary(self, plaintext_bin, key):
        """对二进制数据加密"""
        k1, k2 = self.generate_keys(key)
        permuted_data = self.permute_bits(plaintext_bin, self.IP)
        fk1_result = self.f_function(permuted_data, k1)
        swapped = fk1_result[4:] + fk1_result[:4]
        fk2_result = self.f_function(swapped, k2)
        return self.permute_bits(fk2_result, self.IPinv)

    def decrypt_binary(self, ciphertext_bin, key):
        """对二进制数据解密"""
        k1, k2 = self.generate_keys(key)
        permuted_data = self.permute_bits(ciphertext_bin, self.IP)
        fk2_result = self.f_function(permuted_data, k2)
        swapped = fk2_result[4:] + fk2_result[:4]
        fk1_result = self.f_function(swapped, k1)
        return self.permute_bits(fk1_result, self.IPinv)

    def encrypt_char(self, char, key):
        """对单个字符进行加密"""
        bin_char = self.char_to_binary(char)
        encrypted_bin = self.encrypt_binary(bin_char, key)
        return self.binary_to_char("".join(encrypted_bin))

    def decrypt_char(self, char, key):
        """对单个字符进行解密"""
        bin_char = self.char_to_binary(char)
        decrypted_bin = self.decrypt_binary(bin_char, key)
        return self.binary_to_char("".join(decrypted_bin))

    def encrypt_text(self, text, key):
        """加密整个字符串"""
        self.validate_binary(key, 10)
        return ''.join([self.encrypt_char(char, key) for char in text])

    def decrypt_text(self, encrypted_text, key):
        """解密整个字符串"""
        self.validate_binary(key, 10)
        return ''.join([self.decrypt_char(char, key) for char in encrypted_text])
