import hdfs

client = hdfs.InsecureClient('http://localhost:9870', user='Felix')

UPLOAD_HDFS_FILE = '/tmp/sample_2.log'
client.upload(UPLOAD_HDFS_FILE, '/tmp/localdata/sample_1.log')

