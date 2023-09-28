import pandas as pd
df = pd.read_csv('')
print(type(df))
df.index
df.columns
df.shape
df.describe()
# create price difference
df[pricedoiff]= df[price]-df[close]
#daily return
df[dailyreturn]= df[pricefdiff]/df[close]
# create a direction column
df[direction] = [1 if df.loc[ei, 'pricediff']>0 else -1
                 for ei in df.index]
# moving average
df['Average3']=(df['close'] + df['close'].shift(1) + df['close'].shift(2))/3
#calculate moving average using .rolling()
df['MA40'] = df['close'].rolling(40).mean()
#plot moving average
df['close'].plot()
df['MA40'].plot()
df['MA200'].plot()
#daily profit
df'[close1'] = df['close'].shift(-1)
df['profit'] = [df.loc[ei,'close1']- df.loc[ei,close]
                if df.loc[ei,'share'] ==1
                else 0 for ei in df.index]
df['profit'].plot()
#cumulative wealth
df['wealth'] = df['profit'].cumsum()

print("Total money you win is ", df.loc[df.index[-2],'wealth'])
print("Total money you spend is", df.loc[df.index[0], 'close'])




