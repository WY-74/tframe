import pymysql
import os
from typing import Dict
from conftest import LOGGER


class MySqlUtil:
    @classmethod
    def execute_sql(cls, sql: str, cfg: Dict[str, str | int] | None = None):
        if cfg == None:
            cfg = {
                "host": os.environ.get("mysql_host"),
                "port": int(os.environ.get("mysql_port")),
                "user": os.environ.get("mysql_user"),
                "password": os.environ.get("mysql_password"),
                "database": os.environ.get("mysql_database"),
                "charset": "utf8mb4",
            }
        try:
            conn = pymysql.connect(**cfg)
        except Exception:
            LOGGER.warning("DB connection failure")

        cursor = conn.cursor()
        cursor.execute(sql)
        record = cursor.fetchone()
        LOGGER.info(f"Data from MySQL: {record}")

        conn.close()
        return record
