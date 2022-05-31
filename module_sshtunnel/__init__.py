from sshtunnel import SSHTunnelForwarder

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    LOCAL_HOST = "127.0.0.1"
    SSH_HOST = "sshhost.com"
    SSH_PORT = 22
    SSH_USER = "test"
    SSH_PASSWORD = "testpassword"

    MYSQL_HOST = "mysql-host"
    MYSQL_PORT = 3306
    MYSQL_USER = "mysql_user"
    MYSQL_PASS = "mysql_pass"
    MYSQL_DB = "test"

    # assume that a mysql service is running on mysql-host, and only sshhost.com can access the mysql service
    # we can access sshhost.com by ssh, now we use sshhost.com as tunnel to access mysql service
    with SSHTunnelForwarder(
        (SSH_HOST, SSH_PORT),
        ssh_password=SSH_PASSWORD,
        ssh_username=SSH_USER,
        remote_bind_address=(MYSQL_HOST, MYSQL_PORT),
    ) as tunnel:
        mysql_url = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{LOCAL_HOST}:{tunnel.local_bind_port}/{MYSQL_DB}"
        logging.info("connect mysql using: %s", mysql_url)
