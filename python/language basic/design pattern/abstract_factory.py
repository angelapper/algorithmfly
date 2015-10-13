#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc


class Switch (object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


# Intent
# Provide an interface for creating families of related or dependent objects without specifying their concrete classes

# AbstractFactory

class DbAdminFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_data_provider(self):
        return

    @abc.abstractmethod
    def get_configuration_helper(self):
        return

# ConcreteFactory


class MySQLAdminFactory(DbAdminFactory):
    def get_data_provider(self):
        return MySQLDataProvider()

    def get_configuration_helper(self):
        return MySQLConfigurationHelper()


class OracleAdminFactory(DbAdminFactory):
    def get_data_provider(self):
        return OracleDataProvider()

    def get_configuration_helper(self):
        return OracleConfigurationHelper()

# AbstractProduct


class DbDataProvider(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_connection(self, connection_string):
        return


class DbConfigurationHelper(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def print_manual(self):
        return

    @abc.abstractmethod
    def change_default_engine(self):
        return

# ConcreteProduct


class MySQLDataProvider(DbDataProvider):
    def get_connection(self, connection_string):
        print("MySQL: Trying to connect", connection_string)
        return


class MySQLConfigurationHelper(DbConfigurationHelper):
    def print_manual(self):
        print("MySQL: Help")
        return

    def change_default_engine(self):
        print("MySQL: Change Engine to")
        return


class OracleDataProvider(DbDataProvider):
    def get_connection(self, connection_string):
        print("Oracle: Trying to connect", connection_string)
        return


class OracleConfigurationHelper(DbConfigurationHelper):
    def print_manual(self):
        print("Oracle: Help")
        return

    def change_default_engine(self):
        print("Oracle: Change Engine to")
        return


# Client


class DatabaseClient:
    def __init__(self, database_desc):
        for case in Switch(database_desc):
            if case('mysql'):
                self.database = MySQLAdminFactory()
                break
            if case('Oracle'):
                self.database = OracleAdminFactory()
                break

        self.provider = self.database.get_data_provider()
        self.helper = self.database.get_configuration_helper()

    def connect(self, connection_string):
        self.provider.get_connection(connection_string)

    def help(self):
        self.helper.print_manual()

    def change_engine(self):
        self.helper.change_default_engine()


if __name__ == "__main__":
    mysql_client = DatabaseClient('mysql')
    oracle_client = DatabaseClient('Oracle')
    mysql_client.connect('angelapper@mysql')
    oracle_client.connect('angelapper@Oracle')
    mysql_client.help()
    oracle_client.help()

# OUTPUT ###
# MySQL: Trying to connect angelapper@mysql
# Oracle: Trying to connect angelapper@Oracle
# MySQL: Help
# Oracle: Help
