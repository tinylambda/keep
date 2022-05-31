import hdfs


client = hdfs.InsecureClient("http://localhost:9870", user="Felix")

WRITE_FILE = "/tmp/sample_1.log"
with client.write(WRITE_FILE, overwrite=True) as writer:
    writer.write(b"Hello world.")
