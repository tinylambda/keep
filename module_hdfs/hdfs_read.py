import hdfs

from module_hdfs.hdfs_write import WRITE_FILE


client = hdfs.InsecureClient("http://localhost:9870", user="Felix")
with client.read(WRITE_FILE, encoding="utf-8", delimiter="\n") as reader:
    for line in reader:
        print(line)
