from urllib.parse import urlparse


if __name__ == '__main__':
    scheme = 'jdbc:hive2'
    url = '//hiveserver-zk1.internal:2181,hiveserver-zk2.internal:2181,hiveserver-zk3.internal:2181,' \
        'hiveserver-zk4.internal:2181,hiveserver-zk5.internal:2181/default;serviceDiscoveryMode=zooKeeper;' \
        'zooKeeperNamespace=hiveserver2?sample.bigdata.job.jobtype=ETL_ROUNTINE;task.group.id=200;task.priority=0'

    parsed = urlparse(url, scheme='jdbc:hive2')
    print(parsed)

