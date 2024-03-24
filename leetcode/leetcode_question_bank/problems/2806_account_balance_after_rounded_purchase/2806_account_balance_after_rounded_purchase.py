class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        account_balance = 100
        if purchaseAmount >= 0 and purchaseAmount <= 100:
            if purchaseAmount % 10 <= 4 :
                purchaseAmount -= purchaseAmount % 10
                account_balance -= purchaseAmount
            else:
                purchaseAmount += 10 - (purchaseAmount % 10)
                account_balance -= purchaseAmount
        return account_balance
