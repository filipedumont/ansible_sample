import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_apache_is_server_is_running(host):
    # unless we need to do something in the ansible server (192.168...),
    # the molecule server will do the work just fine
    apache_server = host.addr("test-apache")
    print(apache_server)
    assert apache_server.is_resolvable
    assert apache_server.is_reachable


def test_apache_is_installed_and_running(host):
    httpd = host.package("httpd")
    assert httpd.is_installed
    assert host.service("httpd").is_running


def test_index_file_is_customized(host):
    apache_server = host.addr("test-apache")
    cmd = apache_server.run("cat /var/www/html/index.html")
    assert "Hello CM!" in cmd.stdout
