### STACKING UP
players = pd.read_csv('players.csv')

############################################################################
# average height of players by position and division
players = players.fillna('none')

positions = ['LIBERO','DEFENSIVE SPECIALIST', 'OUTSIDE HITTER', 
             'RIGHT SIDE', 'MIDDLE BLOCKER', 'SETTER', 'UTILITY']

d1_heights, d3_heights = [], []

for position in positions:
    df = players[players['position'].str.contains(position)]
    df = df[df.height != 'none']
    d1_heights.append(df.height[df.division == 'D1'].mean())
    d3_heights.append(df.height[df.division == 'D3'].mean())
    
pos_height = pd.DataFrame(columns=['position','d1_average_height','d3_average_height'])
pos_height['position'] = positions
pos_height['d1_average_height'] = d1_heights
pos_height['d3_average_height'] = d3_heights

pos_height.sort_values('d1_average_height').round(2)


############################################################################
# outside hitter height over time
players = pd.read_csv('players.csv')
players = players.dropna()

seasonlist = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016',
             '2016-2017','2017-2018','2018-2019','2019-2020']

d1_heights, d3_heights = [], []

for season in seasonlist:
    df = players[players['position'].str.contains('OUTSIDE HITTER')]
    df = df[df.height != 'none']
    d1_heights.append(df.height[(df.division == 'D1') & (df.season == season)].mean())
    d3_heights.append(df.height[(df.division == 'D3') & (df.season == season)].mean())
    
yearlist = [num for num in range(2010,2020)]
sns.set()
fig,ax1 = plt.subplots()

ax1.plot(yearlist, d3_heights, label='D3')
ax1.plot(yearlist, d1_heights, color='tab:orange', label='D1')

ax1.set_title('Outside hitter height over time', fontsize=15, fontweight='bold')
ax1.set_ylabel('Height (inches)')
ax1.set_xlabel('Season start year')

plt.legend()
plt.show


############################################################################
# team average height over time
seasonlist = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016',
             '2016-2017','2017-2018','2018-2019','2019-2020']

d1_heights, d3_heights = [], []

for season in seasonlist:
    df = players.dropna()
    d1_heights.append(df.height[(df.division == 'D1') & (df.season == season)].mean())
    d3_heights.append(df.height[(df.division == 'D3') & (df.season == season)].mean())
    
yearlist = [num for num in range(2010,2020)]
sns.set()

fig,ax1 = plt.subplots()

ax1.plot(yearlist, d3_heights, label='D3')
ax1.plot(yearlist, d1_heights, color='tab:orange', label='D1')

ax1.set_title('Team average height over time', fontsize=15, fontweight='bold')
ax1.set_ylabel('Height (inches)')
ax1.set_xlabel('Season start year')

plt.legend()
plt.show
