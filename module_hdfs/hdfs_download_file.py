import hdfs

from module_hdfs.hdfs_write import WRITE_FILE

client = hdfs.InsecureClient("http://localhost:9870", user="Felix")

client.download(WRITE_FILE, "/tmp/localdata/")
