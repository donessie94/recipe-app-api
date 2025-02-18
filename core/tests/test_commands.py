"""
Test custom Django management commands.
"""
from unittest.mock import patch
from psycopg import OperationalError as PsycopgError
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """
    Test command.
    """
    def test_wait_for_db_ready(self, pacthed_check):
        """Test waiting for database if database ready."""
        pacthed_check.return_value = True

        #calling our custom management command
        call_command('wait_for_db')

        pacthed_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, pacthed_check):
        """Test waiting for database when getting OperationalError"""
        
        #this is how you pass errors to the mocked object, we will return 2 PsycopgErrors first, then
        #3 OperationErrors and finally we will return true (database ready)
        pacthed_check.side_effect = [PsycopgError] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')
        self.assertEqual(pacthed_check.call_count, 6)
        pacthed_check.assert_called_with(databases=['default'])