"""
Elastic service script.

"""

from resource_management import *
from elastic_slave  import elastic_slave


class Elasticsearch(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print 'Install the Master'
        self.install_packages(env)
    def configure(self, env):
        import params
        env.set_params(params)
        elastic_slave()   
    def stop(self, env):
        import params
        env.set_params(params)
        stop_cmd = format("source {conf_dir}/elastic-env.sh ; /etc/init.d/elasticsearch stop")
        Execute(stop_cmd)
        print 'Stop the Master'
    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        start_cmd = format("source {conf_dir}/elastic-env.sh; /etc/init.d/elasticsearch start")
        Execute(start_cmd)
        print 'Start the Master'
    def status(self, env):
        import params
	env.set_params(params)
	check_process_status(params.pid_file)
        print 'Status of the Slave'
if __name__ == "__main__":
    Elasticsearch().execute()


