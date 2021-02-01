# dbbackup to manage server databases backups:
- Mysql: this release
- PostgreSQL: next release
- Other: futures releases (need some help...)

Installation:

pip install dbbackup

dbbackup-tools is instaled with dbbackup dependencies

Run it:
- python
- import dbbackup_tools.util
- Enter your folder name to hold dbbackup configuration
- cd to your new dbbackup folder

Configuration:
- ajust the file .env to match your local configration

- To logging on smtp, rename and adjust:

loggin_config_example.yaml to loggin_config.yaml

- To backup Mysql databases, rename and adjust:

mysql-backup-script_example.config to mysql-backup-script.config

Work with it:
- python
- import dbbackup
- from dbbackup import check_dbbackup
