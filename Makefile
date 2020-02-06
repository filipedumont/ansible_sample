ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

up: start_apache
down: stop_apache
destroy: destroy_apache

start_apache:
	@echo " > starting apache server..."
	@cd vagrantfiles/apache ; vagrant up

stop_apache:
	@echo " > stopping apache server..."
	@cd vagrantfiles/apache ; vagrant halt

destroy_apache:
	@echo " > removing apache server..."
	@cd vagrantfiles/apache ; vagrant destroy --force

apache: start_apache ansible_apache

ansible_apache:
	@echo " > installing Apache ..."
	@ansible-playbook -i inventories/apache -b apache.yml

