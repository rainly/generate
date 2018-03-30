import hashlib
m = hashlib.md5()


import uuid



for _ in range(100):
    m.update(bytes(str(uuid.uuid1()),encoding='utf-8'))
    print("INSERT INTO `ssc_key` VALUES ('" + m.hexdigest() + "', '2099-01-01 23:59:59', '网站：ajjkk6779', '', '0000-00-00 00:00:00', '0');")

