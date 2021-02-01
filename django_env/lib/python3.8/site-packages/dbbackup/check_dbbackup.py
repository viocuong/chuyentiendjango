"""
* Written by: Eduardo Cuducos
* Project: alchemydumps
* this is the check_dbbackup module
*
"""

# TODO 
# send msg all possible exception

# configure loggin for cleandbbackup
import logging
from dbbackup import add_module_handler
logger = logging.getLogger(__name__)
add_module_handler(logger)

# import from mymodules
from . mymodules.backup import Backup
from . mymodules.backupAutoClean import BackupAutoClean

# check if there are backups
backup = Backup()
backup.files = tuple(backup.target.get_files())
if not backup.files:
    logger.info('No backups found.')
    
# get black and white list
cleaning = BackupAutoClean(backup.get_timestamps())
white_list = cleaning.white_list
black_list = cleaning.black_list
delete_list = list()
if not black_list:
    logger.info('No backup to be deleted.')
else:
    logger.info(f'{len(black_list)} backups will be delete')
    
    for date_id in black_list:
        date_formated = backup.target.parse_timestamp(date_id)
        for f in backup.by_timestamp(date_id):
            delete_list.append(f)

    # delete old backups
    for name in delete_list:
        logger.warning(f'ID: {date_id} from: {date_formated} {name} will be delete')
        backup.target.delete_file(name)
        #backup.close_ftp()

# print the list of files to be kept
logger.info(f'{len(white_list)} backups will be kept')

for date_id in white_list:
    date_formated = backup.target.parse_timestamp(date_id)
    logger.debug(f'ID: {date_id} from: {date_formated} will be kept')

