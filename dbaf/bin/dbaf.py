#!/usr/bin/python
import sys
import os
import getopt
import utlcnfg

class s24dbaf():
    def __init__(self):
        self.client_code = ''
        self.hostname = ''
        self.oracle_owner = 'oracle'
        self.global_database_name = ''
        self.database = ''
        self.instance = ''
        self.schema = ''
        self.directory = ''
        self.parfile = ''
        self.ticket = ''
        self.email = ''
        self.os_user = ''
        self.schedule = ''
        self.execute = ''
        self.status = ''
        self.help = False
        self.password_length = 0

        self.s24dbaf_home_dir = ''
        self.backup_base_dir = ''

        self.debug_commands = False
        self.debug_internals = False


if __name__ == '__main__':
    # Set default values
    client_code = ''
    hostname = ''
    oracle_owner = 'oracle'
    global_database_name = ''
    database = ''
    instance = ''
    schema = ''
    directory = ''
    parfile = ''
    ticket = ''
    email = ''
    db_user = ''
    dp_pwd = ''
    os_user = ''
    os_pwd = ''
    schedule = ''
    execute = ''
    status = ''
    help = False
    password_length = 0

    opts, args = getopt.gnu_getopt(sys.argv[1:],
      'c:h:o:g:d:i:s:p:t:e:u:h:?',
      ['client_code=',
        'hostname=',
        'oracle_owner=',
        'gdb=',
        'global_database_name=',
        'db=',
        'database=',
        'instance=',
        'schema=',
        'directory=,'
        'parfile=',
        'ticket=',
        'email=',
        'db_user=',
        'os_user=',
        'schedule=',
        'help',
        'debug',
        'debug_internals',

      # Deploy procedures from s24dply
        'create_directory',
        'create_backup_directories',
        'create_local_directories',
        'create_service_accounts'
        'db_user',
          'create',
          'apply_best_practices',
        'list_oratab',
        'sshkeys',
          'list',
          'list_template',
          'deploy_template',
        'get_random_password',
          'password_length=',
        'password_wallet',
          'enable',
          'disable',

      # RMAN Procedures from s24rman

      # RMAN Catalog Procedures from s24rcat
        'create_rman_catalog_owner',
        'create_rman_catalog',
        'add_rman_catalog_to_tnsnames',
        'register_database',
        'resynch',
        'resynch_from_controlfile_copy',
        'catalog_disk_start_with',
        'unregister_database',
        'drop_catalog'

      # PeopleSoft Procedures from s24psft
      ])


    # ==========================================================================
    # Option Parser
    for opt, arg in opts:
        print opt
        print arg

        # Determines if high level debug statements should be shown while executing the script
        # This is typically used to show high level results
        if opt in ('--debug'):
            self.debug_commands = True
            print ""
            print "===================================================================================================="
            print 'Result Level Debuging Enabled'
            print "----------------------------------------------------------------------------------------------------"

        # Determines if debug statements should be shown while executing the script
        # This is typically used to show debug statements inside of each function
        elif opt in ('--debug_internals'):
            self.debug_commands = True
            self.debug_internals = True
            print ""
            print "===================================================================================================="
            print 'Procedure Level Debuging Enabled'
            print "----------------------------------------------------------------------------------------------------"

        # Sets the client code
        elif opt in ('-c', '--client_code'):
            client_code = arg

        # Sets the hostname of the server
        elif opt in ('-h', '--hostname'):
            hostname = arg

        # Overwrites the oracle owner from 'oracle' to new OS owner
        elif opt in ('-o', '--oracle_owner'):
            oracle_owner = arg

        # Sets the global name of the database
        elif opt in ('-g', '--gdb', '--global_database_name'):
            global_database_name = arg

        # Sets the name of the database
        elif opt in ('-d', '--db', '--database'):
            database = arg

        # Sets the oracle_sid of the database
        elif opt in ('-i', '--instance'):
            instance = arg

        # The name of the parfile to use
        elif opt in ('-s', '--schema'):
            schema = arg

        # The name of the parfile to use
        elif opt in ('-p', '--directory'):
            directory = arg

        # The name of the parfile to use
        elif opt in ('-p', '--parfile'):
            parfile = arg

        # Creates a ticket directory for logs and artifacts
        elif opt in ('-t', '--ticket'):
            ticket = arg

        # Email the results to recipients
        elif opt in ('-e', '--email'):
            email = arg

        # Sets the os os_user
        elif opt in ('-u', '--os_user'):
            os_user = arg

        # Schedule the
        elif opt in ('--schedule'):
            schedule = arg

        # Displays help
        elif opt in ('-?', '--help'):
            help = True

        # --------------------------------------------------------------------------
        # s24dply module
        # Creates a single directory
        elif opt in ('--create_directory':
            execute = 'create_directory'

    s24_dbaf = s24dbaf
    utl_cnfg = utlcnfg.utlcnfg ('s24dply', debug_commands = False)

    s24_dbaf.oracle_owner = oracle_owner.lower()
    s24_dbaf.ticket = ticket.upper()
    s24_dbaf.hostname = utl_cnfg.get_hostname()
    s24_dbaf.oracle_sid = utl_cnfg.get_oracle_sid()
    s24_dbaf.oracle_home = utl_cnfg.get_oracle_home()
    s24_dbaf.module_lib_dir = utl_cnfg.get_module_lib_dir()
    s24_dbaf.module_sql_dir = utl_cnfg.get_module_sql_dir()

    print s24_dbaf.oracle_owner
    print s24_dbaf.ticket
    
    print s24_dbaf.hostname
    print s24_dbaf.oracle_sid
    print s24_dbaf.oracle_home
    print s24_dbaf.module_lib_dir
    print s24_dbaf.module_sql_dir

    print utl_cnfg.get_hostname()
    utl_cnfg.list_oratab()
    utl_cnfg.list_sshkeys()
    utl_cnfg.list_sshkeys_template()
    
