

if __name__ == '__main__':
    print('What is Bitcoin price today?')
    current_btc_to_usd = int(input())
    print('How much $ do you have?')
    current_available_usd = int(input())
    can_buy = current_available_usd / current_btc_to_usd
    print(f'You can buy {can_buy} BTC')
