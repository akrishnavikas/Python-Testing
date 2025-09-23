def services(*args):
    for i in args:
        print(f"{i} is a service")


services("hdfs","hive","impala")

