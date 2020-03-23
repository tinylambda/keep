#!/usr/bin/env bash

# 生成密钥对
openssl genrsa -out mykey.pem 2048

# openssl genrsa -des3 -out mykey2.pem 2048

# 从密钥对中分离出公钥
openssl rsa -in mykey.pem -pubout -out mypubkey.pem

# openss rsa -in mykey2.pem -pubout -out mypubkey2.pem

# 检查密钥对文件是否正确
openssl rsa -in mykey.pem -check -noout

# 显示公钥信息
openssl rsa -pubin -in mypubkey.pem -text

# 创建测试文件
echo "hello" >> plain.txt

# 使用密钥对加密
openssl rsautl -encrypt -inkey mykey.pem -in plain.txt -out cipher.txt
# 使用公钥加密
openssl rsautl -encrypt -pubin -inkey mypubkey.pem -in plain.txt -out cipher2.txt

# 解密
openssl rsautl -decrypt -inkey mykey.pem -in cipher.txt

########## DH start
# 生成一个 2014 比特的参数文件
openssl dhparam -out dhparam.pem -2 1024

# 查看参数文件内容
openssl dhparam -in dhparam.pem -noout -C

# 基于参数文件生成密钥对
openssl genpkey -paramfile dhparam.pem -out dhkey.pem

# 查看密钥对文件内容
openssl pkey -in dhkey.pem -text -noout

#### DH 密钥协商例子
# 通信双方的任何一方生成DH的参数文件，可以对外公开
openssl genpkey -genparam -algorithm DH -out dhp.pem

# 查看参数文件的内容，包括p和g等参数
openssl pkeyparam -in dhp.pem -text

# 发送方A基于参数文件生成一个密钥对
openssl genpkey -paramfile dhp.pem -out akey.pem

# 查看密钥内容
openssl pkey -in akey.pem -text -noout

# 发送方B基于参数文件生成一个密钥对
openssl genpkey -paramfile dhp.pem -out bkey.pem

# 查看密钥对内容
openssl pkey -in bkey.pem -text -noout

# 发送方A拆出公钥文件akey_pub.pem，私钥自己保存
openssl pkey -in akey.pem -pubout -out akey_pub.pem

# 发送方B拆出公钥文件bkey_pub.pem，私钥自己保存
openssl pkey -in bkey.pem -pubout -out bkey_pub.pem

# 发送方A收到B发送过来的公钥，将协商出的密钥保存到data_a.txt文件中
openssl pkeyutl -derive -inkey akey.pem -peerkey bkey_pub.pem -out data_a.txt

# 发送方B收到A发送过来的公钥，将协商出的密钥保存到data_b.txt文件中
openssl pkeyutl -derive -inkey bkey.pem -peerkey akey_pub.pem -out data_b.txt

# 查看系统有多少椭圆曲线
openssl ecparam -list_curves

# 生成一个参数文件，通过-name指定命名曲线
openssl ecparam -name secp256k1 -out secp25k1.pem

# 默认情况下，查看参数文件只会现实曲线的名称
openssl ecparam -in secp25k1.pem -text -noout

# 现实参数文件里的具体参数
openssl ecparam -in secp25k1.pem -text -param_enc explicit -noout

# RSA签名：生成RSA密钥对
openssl genrsa -out rsaprivatekey.pem 1024

# RSA签名：从密钥对中提取出公钥
openssl rsa -in rsaprivatekey.pem -pubout -out rsapublickey.pem

# 对plain.txt使用sha256哈希算法和签名算法，生成签名文件signature.txt
openssl dgst -sha256 -sign rsaprivatekey.pem -out signature.txt plain.txt

# 对应的验签过程
openssl dgst -sha256 -verify rsapublickey.pem -signature signature.txt plain.txt


### DSA算法实践
# 生成参数文件，类似于DH参数文件
openssl dsaparam -out dsaparam.pem 1024

# 通过参数文件生成密钥对 dsaprivatekey.pem
openssl gendsa -out dsaprivatekey.pem dsaparam.pem

# 对私钥文件使用des3算法进行加密
openssl gendsa -out dsaprivatekey2.pem -des3 dsaparam.pem

# 通过密钥对文件，拆分出公钥
openssl dsa -in dsaprivatekey.pem -pubout -out dsapublickey.pem

# 显示私钥文件信息
openssl dsa -in dsaprivatekey.pem -text

# 显示公钥和文件的信息
openssl dsa -pubin -in dsapublickey.pem -text

# dsa签名
openssl dgst -sha256 -sign dsaprivatekey.pem -out signature.txt plain.txt

# dsa验签
openssl dgst -sha256 -verify dsapublickey.pem -signature signature.txt plain.txt

# 生成ECDSA私钥
openssl ecparam -name secp256k1 -genkey -out ecdsa_priv.pem

# 显示ECDSA私钥信息
openssl ec -in ecdsa_priv.pem -text -noout

# 提取ECDSA公钥
openssl ec -in ecdsa_priv.pem -pubout -out ecdsa_pub.pem

# 显示ECDSA公钥信息
openssl ec -in ecdsa_pub.pem -pubin -text -noout

# 使用ECDSA签名
openssl dgst -sha256 -sign ecdsa_priv.pem -out signature.txt plain.txt

# ECDSA验签
openssl dgst -sha256 -verify ecdsa_pub.pem -signature signature.txt plain.txt

# 性能测试
openssl speed aes-128-cbc

# 性能测试，启用EVP模式
openssl speed -evp aes-128-cbc

# 生成私钥对和CSR
openssl req -newkey rsa:1024 -nodes -keyout example_key.pem -out example_csr.pem

# 生成自签名证书
openssl x509 -signkey example_key.pem -in example_csr.pem -req -days 365 -out example_cert.pem
