import concurrent.futures
from flask import Flask, render_template, request, jsonify
from SDES import SDES
import time

app = Flask(__name__)
sdes = SDES()

# 使用多线程进行暴力破解的函数，解密字符串
def brute_force_decrypt(known_pairs, sdes_obj):
    total_keys = 2 ** 10  # 共有1024个可能的密钥（10位二进制数）
    valid_keys = []  # 用于存储有效密钥

    # 记录开始时间
    start_time = time.time()

    # 检查单个密钥的有效性
    def validate_single_key(key_value):
        key_str = format(key_value, '010b')
        for plain, cipher in known_pairs:
            if sdes_obj.decrypt_text(cipher, key_str) != plain:
                return None
        return key_str

    # 使用多线程进行并行计算
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for key in executor.map(validate_single_key, range(total_keys)):
            if key:
                valid_keys.append(key)

    # 记录结束时间并计算耗时
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"暴力破解耗时: {elapsed_time:.2f} 秒")  # 打印暴力破解耗时

    return valid_keys


# 使用暴力破解解密二进制数据
def brute_force_decrypt_binary(plain_bin, cipher_bin, sdes_obj):
    found_keys = []

    # 记录开始时间
    start_time = time.time()

    # 遍历所有可能的密钥
    for key_value in range(1024):
        key_str = format(key_value, '010b')
        encrypted_data = sdes_obj.encrypt_binary(plain_bin, key_str)
        if "".join(encrypted_data) == cipher_bin:
            found_keys.append(key_str)

    # 记录结束时间并计算耗时
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"暴力破解耗时: {elapsed_time:.2f} 秒")  # 打印暴力破解耗时

    return found_keys


# 主页路由，渲染字符串加密解密页面
@app.route('/')
def index_page():
    return render_template('string.html')

# 二进制加密解密页面路由
@app.route('/binary')
def binary_page():
    return render_template('binary.html')

# 处理字符串加密请求的路由
@app.route('/encrypt_string', methods=['POST'])
def encrypt_string_route():
    plaintext = request.form.get('plaintext')
    key = request.form.get('key')
    sdes.validate_binary(key, 10)
    encrypted_text = sdes.encrypt_text(plaintext, key)
    return jsonify(ciphertext=encrypted_text)

# 处理字符串解密请求的路由
@app.route('/decrypt_string', methods=['POST'])
def decrypt_string_route():
    ciphertext = request.form.get('ciphertext')
    key = request.form.get('key')
    sdes.validate_binary(key, 10)
    decrypted_text = sdes.decrypt_text(ciphertext, key)
    return jsonify(plaintext=decrypted_text)

# 处理二进制数据加密请求的路由
@app.route('/encrypt_binary', methods=['POST'])
def encrypt_binary_route():
    plaintext_bin = request.form.get('plaintext_bin')
    key = request.form.get('key')
    sdes.validate_binary(key, 10)
    encrypted_bin = ''.join(sdes.encrypt_binary(plaintext_bin, key))
    return jsonify(ciphertext_bin=encrypted_bin)

# 处理二进制数据解密请求的路由
@app.route('/decrypt_binary', methods=['POST'])
def decrypt_binary_route():
    ciphertext_bin = request.form.get('ciphertext_bin')
    key = request.form.get('key')
    sdes.validate_binary(key, 10)
    decrypted_bin = ''.join(sdes.decrypt_binary(ciphertext_bin, key))
    return jsonify(plaintext_bin=decrypted_bin)


# 处理暴力破解字符串加密的路由
@app.route('/brute_force_string', methods=['POST'])
def brute_force_string_route():
    plaintext = request.form.get('plaintext')
    ciphertext = request.form.get('ciphertext')
    known_pairs = [(plaintext, ciphertext)]

    start_time = time.time()  # 开始时间
    keys = brute_force_decrypt(known_pairs, sdes)
    end_time = time.time()  # 结束时间
    elapsed_time = end_time - start_time

    return jsonify(keys=keys, time=f"{elapsed_time:.3f} 秒")


# 处理暴力破解二进制数据加密的路由
@app.route('/brute_force_binary', methods=['POST'])
def brute_force_binary_route():
    plaintext_bin = request.form.get('plaintext_bin')
    ciphertext_bin = request.form.get('ciphertext_bin')

    start_time = time.time()  # 开始时间
    keys = brute_force_decrypt_binary(plaintext_bin, ciphertext_bin, sdes)
    end_time = time.time()  # 结束时间
    elapsed_time = end_time - start_time

    return jsonify(keys=keys, time=f"{elapsed_time:.3f} 秒")


@app.route('/main')
def main_page():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
