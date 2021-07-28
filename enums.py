"""This module contains Enum values used by this library
"""

from enum import Enum

class Scopes(Enum):
    """Scopes supported by Intuit for OAuth and OpenID flows
    """

    PROFILE = 'profile'
    EMAIL = 'email'
    PHONE = 'phone'
    ADDRESS = 'address'
    OPENID = 'openid'
    ACCOUNTING = 'com.intuit.quickbooks.accounting'
    PAYMENT = 'com.intuit.quickbooks.payment'
    
    # for whitelisted Beta apps only
    PAYROLL = 'com.intuit.quickbooks.payroll'
    PAYROLL_TIMETRACKING = 'com.intuit.quickbooks.payroll.timetracking'
    PAYROLL_BENEFITS = 'com.intuit.quickbooks.payroll.benefits'
    PAYSLIP_READ = 'com.intuit.quickbooks.payroll.payslip.read'

    # For migrated apps only
    # To not see consent page they should pass the following scopes - openid intuit_name email
    INTUIT_NAME = 'intuit_name'