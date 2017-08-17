#!/usr/bin/env python
"""
Elasticsearch Params configurations
"""

from resource_management.libraries.script.script import Script
from urlparse import urlparse

# server configurations
config = Script.get_config()

elastic_home = '/etc/elasticsearch/'
elastic_bin = '/usr/share/elasticsearch/bin/'

conf_dir = "/etc/elasticsearch"
elastic_user = config['configurations']['elastic-env']['elastic_user']
user_group = config['configurations']['cluster-env']['user_group']
log_dir = config['configurations']['elastic-env']['elastic_log_dir']
pid_dir = '/var/run/elasticsearch'
pid_file = '/var/run/elasticsearch/elasticsearch.pid'
hostname = config['hostname']

java64_home = config['hostLevelParams']['java_home']
elastic_env_sh_template = config['configurations']['elastic-env']['content']

## configurations sample
http_port = config['configurations']['elastic-site']['http_port']
cluster_name = config['configurations']['elastic-site']['cluster_name']


