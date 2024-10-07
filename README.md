# 程序测试结果

## 开始界面 
显示课程即相关项目简介，以及本项目的制作人：李晨雨，王松妍  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image000.png)

## 第1关：基本测试

根据S-DES算法编写和调试程序，提供GUI解密支持用户交互。输入可以是8bit的数据和10bit的密钥，输出是8bit的密文。

二进制交互界面：  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image001.png)

明文输入格式错误提示：  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image003.png)

密钥输入格式错误提示：  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image005.png)  

## 第2关：交叉测试

本组二进制明文加密结果。  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image007.png)

交叉测试组二进制明文加密结果。  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image009.png)

本组二进制明文解密结果。  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image011.png)
  
交叉测试组二进制明文解密结果。  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image013.png)

经交叉验证结果一致。

## 第3关：扩展功能

考虑到向实用性扩展，加密算法的数据输入可以是ASCII编码字符串(分组为1 Byte)，对应地输出也可以是ASCII字符串(很可能是乱码)。

字符串交互界面  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image015.png)

## 第4关：暴力破解

使用相同密钥的明、密文对(一个或多个)，可使用暴力破解的方法找到正确的密钥Key。

二进制：  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image017.png)

字符串：  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image019.png)

## 第5关：封闭测试

问题1：  

由暴力破解查找所有可能的密钥，可以发现，对于随机选择的一个明密文对结果不止一个密钥。  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image021.png)

问题2：  

密钥1：0101110001  

明文：10101100  

得到密文：01111111  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image023.png)  

密钥2：1000010110  

明文：10101100  

得到密文：01111111  

![image](https://github.com/Wang-songyan/S-DES-/blob/main/image/image025.png)  

可以发现，使用不同的密钥，可能会得到相同的密文。
# S-DES加解密工具开发手册

项目名称：S-DES算法实现加、解密程序
开发人员：王松妍、李晨雨

---

## 一、引言

### 1.1 编写目的

本手册旨在为开发者和用户提供S-DES算法实现程序的详细说明，包括其功能、使用方法和技术细节。通过本手册，读者可以更好地理解该程序的设计理念及其在信息安全中的应用。

### 1.2 术语和缩写词

- **S-DES**: 简化数据加密标准（Simplified Data Encryption Standard），一种对称密钥加密算法，用于演示和学习加密技术。
- **DES**: 数据加密标准（Data Encryption Standard），一种广泛使用的对称密钥加密算法，S-DES是其简化版本。
- **对称密钥加密**: 使用相同的密钥进行加密和解密的加密方法。
- **密文**: 加密后的数据，无法直接读取的形式。
- **明文**: 原始未加密的数据，用户输入的信息。
- **暴力破解**: 一种尝试所有可能密钥组合以解密密文的方法。
- **密钥**: 用于加密和解密数据的字符串，S-DES使用10位密钥。
- **ASCII**: 美国信息交换标准代码（American Standard Code for Information Interchange），一种字符编码标准，用于表示文本。
- **二进制数据**: 由0和1组成的数据格式，用于计算机处理。

---

## 二、项目简介

### 2.1 背景

在当今信息化时代，数据安全问题日益严重。对称密钥加密算法是保护敏感信息的一种有效手段，S-DES（简单数据加密标准）作为DES（数据加密标准）的简化版本，旨在为学习和研究加密技术提供一个易于理解和实现的基础。

### 2.2 目的

本项目的主要目的是开发一个S-DES加密与解密工具，帮助用户理解对称密钥加密的基本原理和应用。通过直观的界面和功能，用户可以轻松进行数据加密和解密操作，从而增强其信息安全意识和加密技术的掌握。

### 2.3 主要功能

该程序提供加密、解密和暴力破解密钥的功能，支持用户交互，并能够接受8位二进制数据（或ASCII编码字符串）以及10位密钥。

1. **数据加密**：用户可以输入明文数据，通过选择密钥进行加密，生成相应的密文。
2. **数据解密**：用户可以输入密文及相应的密钥，进行解密操作，恢复出原始明文。
3. **暴力破解**：暴力破解功能允许用户尝试所有可能的密钥组合，以解密给定的密文。
4. **用户界面**：直观易用的图形用户界面，简化用户操作流程。
5. **示例和说明**：提供相关说明，帮助用户理解每个功能的使用方法。

---

## 三、环境要求

### 3.1 操作系统

- Windows 10及以上
- macOS 10.15及以上
- Linux（如Ubuntu 20.04及以上）

### 3.2 软件

- PyCharm：推荐使用PyCharm作为IDE，确保下载并安装适合您的操作系统的版本。
- Python：安装Python 3.6及以上版本。

### 3.3 库

- Flask：Web框架，用于构建应用程序。

---

## 四、代码结构

### 4.1 各个模块/文件的功能描述

#### 4.1.1 app.py

- **Flask 应用初始化**：
  - 创建一个Flask应用程序 `app`。
  - 使用 `SDES.py` 中定义的 `SDES` 类来处理加密和解密操作。

- **暴力破解功能**：
  - `brute_force_decrypt` 函数使用多线程来尝试破解加密字符串的密钥。它会尝试所有可能的10位二进制密钥，直到找到匹配的明文-密文对。
  - `brute_force_decrypt_binary` 函数是针对二进制数据的暴力破解版本，逐一尝试所有密钥直到找到匹配的密钥。

- **路由功能**：
  - `index_page` 渲染字符串加密解密页面 `string.html`。
  - `binary_page` 渲染二进制加密解密页面 `binary.html`。
  - `encrypt_string_route` 和 `decrypt_string_route` 分别处理字符串的加密和解密请求。
  - `encrypt_binary_route` 和 `decrypt_binary_route` 分别处理二进制数据的加密和解密请求。
  - `brute_force_string_route` 处理对字符串进行暴力破解的请求。
  - `brute_force_binary_route` 处理对二进制数据进行暴力破解的请求。
  - `main_page` 渲染主页面 `main.html`。

#### 4.1.2 SDES.py

实现S-DES加密、解密算法以及相关功能逻辑。各个函数功能如下：

- `validate_binary`：验证输入是否是指定长度的二进制字符串。
- `char_to_binary` 和 `binary_to_char`：字符与二进制之间的转换。
- `permute_bits`：根据置换表对位进行重新排列。
- `circular_left_shift`：位串循环左移。
- `generate_keys`：生成两个子密钥。
- `sbox_lookup`：S盒查找功能。
- `f_function`：应用F函数进行加密的核心步骤。
- `encrypt_binary` 和 `decrypt_binary`：对二进制数据进行加密和解密。
- `encrypt_text` 和 `decrypt_text`：对字符串进行加密和解密。

#### 4.1.3 static/

静态文件目录，包含前端资源如JavaScript、CSS预处理文件和图片。

- **js/**：存放JavaScript文件，用于处理前端交互逻辑。
- **scss/**：存放CSS预处理器文件，编译后生成最终CSS文件，用于样式管理。
- **vendor/**：存放外部插件或库。

#### 4.1.4 templates/

HTML模板文件目录，使用Jinja2引擎渲染，动态生成网页内容。

- **binary.html**: 用于展示二进制加密的页面。
- **main.html**: 网站的主页面模板，展示项目的主要信息或导航。
- **string.html**: 用于处理字符串加密的页面。


# 用户指南

## 开始界面

在主页上选择"关于我们"查看相关内容简介。

## 字符串输入模式

在主页上选择 "字符串" 选项卡，然后您可以执行以下操作：

- **加密字符串**：输入明文文本和10位二进制密钥，然后单击 "加密" 按钮来加密文本。

- **解密字符串**：输入密文文本和10位二进制密钥，然后单击 "解密" 按钮来解密文本。

- **暴力破解字符串**：输入已知的明文和对应的密文，然后单击 "查找可能密钥" 按钮来尝试找到可能的密钥。

## 二进制输入模式

在主页上选择 "二进制" 选项卡，然后您可以执行以下操作：

- **加密二进制数据**：输入明文的二进制表示和10位二进制密钥，然后单击 "加密" 按钮来加密数据。

- **解密二进制数据**：输入密文的二进制表示和10位二进制密钥，然后单击 "解密" 按钮来解密数据。

- **暴力破解二进制数据**：输入已知的明文的二进制表示和对应的密文的二进制表示，然后单击 "查找可能选项" 按钮来尝试找到可能的密钥。

##  注意事项

- 密钥长度为10位，只能包含0和1。
- 当使用暴力破解功能时，应考虑到需要尝试所有可能的密钥，因此速度可能较慢。

##  安全性注意事项

请注意，S-DES是一种较旧的加密算法，不适用于安全性要求高的应用程序。在实际应用中，建议使用更强大的加密算法，如AES（高级加密标准）。

## 结束应用程序

要停止应用程序，在终端中按下 `Ctrl+C`。

#  总结

这个应用程序提供了一个用于学习和演示S-DES加解密算法的平台，以及一种尝试暴力破解可能的密钥的方法。请注意，这只是一个教育和演示用途的应用程序，不适用于实际安全需求。

希望这份开发手册能够帮助您使用S-DES加解密应用程序。如果您有任何疑问或需要进一步的帮助，请随时提问。

编写一份开发手册是一项详尽的任务，以下是一个基本的结构，其中包含了前端页面设计、加解密算法、暴力破解以及用户指南。每个部分都会包括相应功能的原始代码示例。
