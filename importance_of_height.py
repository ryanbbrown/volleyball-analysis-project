### THE IMPORTANCE OF HEIGHT
wins = pd.read_csv('team_winrates.csv')
players = pd.read_csv('players.csv')

############################################################################
# rank percentile vs. height
sns.set(style='whitegrid')
sns.lmplot(x='height', y='winpct', hue='division', data=wins, palette='muted')

plt.title("Win percentage vs. Height", fontsize=15, fontweight='bold')
plt.ylabel('Win percentage')
plt.xlabel('Height (inches)')

plt.figtext(0.18,0.85,'D3 R2 - 0.21\nD1 R2 - 0.046', 
            bbox={"facecolor":"white", "edgecolor":"black", "alpha":0.7, "pad":5})

plt.show()


############################################################################
# win percentage vs. height
sns.set(style='whitegrid')
sns.lmplot(x='height', y='percentile', hue='division', data=wins, palette='muted')

plt.title("Win percentage vs. Rank percentile", fontsize=15, fontweight='bold')
plt.ylabel('Win percentage')
plt.xlabel('Height (inches)')

plt.figtext(0.18,0.85,'D3 R2 - 0.21\nD1 R2 - 0.046', 
            bbox={"facecolor":"white", "edgecolor":"black", "alpha":0.7, "pad":5})

plt.show()


############################################################################
# correlation of height and rank percentile over time
def corr(x, y):
    return stats.pearsonr(x, y)[0]

yearlist = [num for num in range(2010,2020)]
seasonlist = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016',
             '2016-2017','2017-2018','2018-2019','2019-2020']

df = wins
df = df.dropna().reset_index(drop=True)

d1_corr_percentile = [corr(df['height'][(df.season==season) & (df.division=='D1')],
  df['percentile'][(df.season==season) & (df.division=='D1')]) for season in seasonlist]
d3_corr_percentile = [corr(df['height'][(df.season==season) & (df.division=='D3')],
  df['percentile'][(df.season==season) & (df.division=='D3')]) for season in seasonlist]

sns.set()

fig,ax1 = plt.subplots()

ax1.plot(yearlist, d3_corr_percentile, label='D3')
ax1.plot(yearlist, d3_corr_percentile, color='tab:orange', label='D1')

ax1.set_title('Correlation of height and rank percentile over time', fontsize=15, fontweight='bold')
ax1.set_ylabel('Correlation')
ax1.set_xlabel('Season start year')

plt.legend()
plt.show


############################################################################
# correlation of height and win percentage over time
def corr(x, y):
    return stats.pearsonr(x, y)[0]

yearlist = [num for num in range(2010,2020)]
seasonlist = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016',
             '2016-2017','2017-2018','2018-2019','2019-2020']

df = wins
df = df.dropna().reset_index(drop=True)

d1_r2_percentile = [corr(df['height'][(df.season==season) & (df.division=='D1')],
  df['winpct'][(df.season==season) & (df.division=='D1')]) for season in seasonlist]
d3_r2_percentile = [corr(df['height'][(df.season==season) & (df.division=='D3')],
  df['winpct'][(df.season==season) & (df.division=='D3')]) for season in seasonlist]

sns.set()

fig,ax1 = plt.subplots()

ax1.plot(yearlist, d3_r2_percentile, label='D3')
ax1.plot(yearlist, d1_r2_percentile, color='tab:orange', label='D1')

ax1.set_title('Correlation of height and win percentage over time', fontsize=15, fontweight='bold')
ax1.set_ylabel('Correlation')
ax1.set_xlabel('Season start year')

plt.legend()
plt.show


############################################################################
# R2 of height and rank percentile over time
def r2(x, y):
    return (stats.pearsonr(x, y)[0])**2

yearlist = [num for num in range(2010,2020)]
seasonlist = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016',
             '2016-2017','2017-2018','2018-2019','2019-2020']

df = wins
df = df.dropna().reset_index(drop=True)

d1_r2_percentile = [r2(df['height'][(df.season==season) & (df.division=='D1')],
  df['winpct'][(df.season==season) & (df.division=='D1')]) for season in seasonlist]
d3_r2_percentile = [r2(df['height'][(df.season==season) & (df.division=='D3')],
  df['winpct'][(df.season==season) & (df.division=='D3')]) for season in seasonlist]

sns.set()

fig,ax1 = plt.subplots()

ax1.plot(yearlist, d3_r2_percentile, label='D3')
ax1.plot(yearlist, d1_r2_percentile, color='tab:orange', label='D1')

ax1.set_title('R2 of height and win percentage over time', fontsize=15, fontweight='bold')
ax1.set_ylabel('R2')
ax1.set_xlabel('Season start year')

plt.legend()
plt.show


############################################################################
# R2 of height and win percentage over time
def r2(x, y):
    return (stats.pearsonr(x, y)[0])**2

yearlist = [num for num in range(2010,2020)]
seasonlist = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016',
             '2016-2017','2017-2018','2018-2019','2019-2020']

df = wins
df = df.dropna().reset_index(drop=True)

d1_corr_percentile = [r2(df['height'][(df.season==season) & (df.division=='D1')],
  df['percentile'][(df.season==season) & (df.division=='D1')]) for season in seasonlist]
d3_corr_percentile = [r2(df['height'][(df.season==season) & (df.division=='D3')],
  df['percentile'][(df.season==season) & (df.division=='D3')]) for season in seasonlist]

sns.set()

fig,ax1 = plt.subplots()

ax1.plot(yearlist, d3_corr_percentile, label='D3')
ax1.plot(yearlist, d1_corr_percentile, color='tab:orange', label='D1')

ax1.set_title('R2 of height and rank percentile over time', fontsize=15, fontweight='bold')
ax1.set_ylabel('R2')
ax1.set_xlabel('Season start year')

plt.legend()
plt.show


############################################################################
# number of 6'5+ players over time
playersd3 = players[players.division == 'D3']
playersd3tall = playersd3[playersd3.height >= 77]
playersd3tall = playersd3tall.groupby(playersd3tall['season']).count()

playersd1 = players[players.division == 'D1']
playersd1tall = playersd1[playersd1.height >= 77]
playersd1tall = playersd1tall.groupby(playersd1tall['season']).count()

d1list = playersd1tall.height.tolist()
d3list = playersd3tall.height.tolist()

yearlist = [num for num in range(2010,2020)]
sns.set()

fig,ax1 = plt.subplots()

ax1.plot(yearlist, d3list, label='D3')
ax1.plot(yearlist, d1list, color='tab:orange', label='D1')

ax1.set_title("Number of 6'5+ players over time", fontsize=15, fontweight='bold')
ax1.set_ylabel('# of players')
ax1.set_xlabel('Season start year')

plt.legend()
plt.show
