class ClusterService:
    def __init__(self,name,status='stopped'):
        self.name = name
        self.status = status
    
    def start(self):
        self.status =  'running'
        print(f"{self.name} is started")

    def stop(self):
        self.status = 'stopped'
        print(f"{self.name} is stopped")


P1 = ClusterService("HDFS")

print(P1.name)
print(P1.start())