"""
# ************************************************************************** #
#                                                                        	#
#            	Account.py                                              	#
#            	Created on  : Thu Nov 20 19:43:15 1989                  	#
#            	Last update : Wed Jan 04 14:54:06 1992                  	#
#            	Made by : Brad "Buddy" McLane <bm@gbu.com>              	#
#                                                                        	#
# ************************************************************************** #
"""

import datetime

# ************************************************************************** #
#                           	Account Class                            	#
# ************************************************************************** #

class Account:
	_nbAccounts = 0
	_totalAmount = 0
	_totalNbDeposits = 0
	_totalNbWithdrawals = 0

	@staticmethod
	def getNbAccounts():
    	return Account._nbAccounts

	@staticmethod
	def getTotalAmount():
    	return Account._totalAmount

	@staticmethod
	def getNbDeposits():
    	return Account._totalNbDeposits

	@staticmethod
	def getNbWithdrawals():
    	return Account._totalNbWithdrawals

	@staticmethod
	def displayAccountsInfos():
    	Account._displayTimestamp()
    	print(f"accounts:{Account.getNbAccounts()};total:{Account.getTotalAmount()};deposits:{Account.getNbDeposits()};withdrawals:{Account.getNbWithdrawals()}")

	def __init__(self, initial_deposit):
    	self._accountIndex = Account._nbAccounts
    	self._amount = initial_deposit
    	self._nbDeposits = 0
    	self._nbWithdrawals = 0

    	Account._totalAmount += initial_deposit
    	Account._nbAccounts += 1

    	Account._displayTimestamp()
    	print(f"index:{self._accountIndex};amount:{initial_deposit};created")

	def __del__(self):
    	Account._displayTimestamp()
    	print(f"index:{self._accountIndex};amount:{self._amount};closed")

	def displayStatus(self):
    	Account._displayTimestamp()
    	print(f"index:{self._accountIndex};amount:{self._amount};deposits:{self._nbDeposits};withdrawals:{self._nbWithdrawals}")

	def makeDeposit(self, deposit):
    	past_amount = self._amount
    	self._amount += deposit
    	self._nbDeposits += 1
    	Account._totalAmount += deposit
    	Account._totalNbDeposits += 1

    	Account._displayTimestamp()
    	print(f"index:{self._accountIndex};p_amount:{past_amount};deposit:{deposit};amount:{self._amount};nb_deposits:{self._nbDeposits}")

	def makeWithdrawal(self, withdrawal):
    	new_amount = self._amount - withdrawal
    	Account._displayTimestamp()
    	print(f"index:{self._accountIndex};p_amount:{self._amount};", end="")
    	if new_amount < 0:
        	print("withdrawal:refused")
        	return False
    	else:
        	self._nbWithdrawals += 1
        	Account._totalNbWithdrawals += 1
        	self._amount = new_amount
        	Account._totalAmount -= withdrawal
        	print(f"withdrawal:{withdrawal};amount:{new_amount};nb_withdrawals:{self._nbWithdrawals}")
        	return True

	def checkAmount(self):
    	return self._amount

	@staticmethod
	def _displayTimestamp():
    	now = datetime.datetime.now()
    	print(f"[{now.year}{now.month:02d}{now.day:02d}_{now.hour:02d}{now.minute:02d}{now.second:02d}] ", end="")

	@classmethod
	def _reset_static_variables(cls):
    	"""Reseta as variáveis estáticas da classe para seus valores iniciais."""
    	cls._nbAccounts = 0
    	cls._totalAmount = 0
    	cls._totalNbDeposits = 0
    	cls._totalNbWithdrawals = 0

# ************************************************************************** #
# vim: set ts=4 sw=4 tw=80 noexpandtab:                                  	#
# -*- indent-tabs-mode:t;                                               	-*-
# -*- mode: c++-mode;                                                   	-*-
# -*- fill-column: 75; comment-column: 75;                              	-*-
# ************************************************************************** #