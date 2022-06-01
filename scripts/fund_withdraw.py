import imp
from scripts.deploy import *
from brownie import FundMe


def fund():
    account = get_account()
    fundme = FundMe[-1]
    entrance_fee = fundme.getEntranceFee()
    print(f"the current entrance fee is {entrance_fee}")
    print("funding")
    fundme.fund({"from": account, "value": entrance_fee})


def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    print("withdrawing the funds")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
