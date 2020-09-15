### TEAM-LEVEL ANALYSIS
wins = pd.read_csv('team_winrates.csv')

df = wins
deltadf = df.dropna().reset_index(drop=True)

deltadf['height_change'] = deltadf.index
deltadf['winpct_change'] = deltadf.index
deltadf['percentile_change'] = deltadf.index

def calculate_delta(index, column):
    if index != 0:
        if deltadf.college[index-1] == deltadf.college[index]:
            delta = deltadf[column][index] - deltadf[column][index-1]
        else:
            delta = np.nan
    else:
        delta = np.nan
        
    return delta

deltadf['height_change'] = deltadf.height_change.apply(lambda x: calculate_delta(x, 'height'))
deltadf['winpct_change'] = deltadf.winpct_change.apply(lambda x: calculate_delta(x, 'winpct'))
deltadf['percentile_change'] = deltadf.percentile_change.apply(lambda x: calculate_delta(x, 'percentile'))

deltadf['winpct_direction'] = deltadf.height_change * deltadf.winpct_change
deltadf['percentile_direction'] = deltadf.height_change * deltadf.percentile_change

def moves_together(number):
    if number > 0:
        value = 'yes'
    elif number < 0:
        value = 'no'
    else:
        value = np.nan
    return value

deltadf['winpct_direction'] = deltadf.winpct_direction.apply(lambda x: moves_together(x))
deltadf['percentile_direction'] = deltadf.percentile_direction.apply(lambda x: moves_together(x))

d1_delta = deltadf[deltadf.division == 'D1']
d3_delta = deltadf[deltadf.division == 'D3']
oneinchdf = deltadf[abs(deltadf.height_change) >= 1]
d1_delta_oneinch = oneinchdf[oneinchdf.division == 'D1']
d3_delta_oneinch = oneinchdf[oneinchdf.division == 'D3']

dflist = [d1_delta, d3_delta, d1_delta_oneinch, d3_delta_oneinch]

ratiolist = []
r2list = []

for df in dflist:
    tile_ratio = df.loc[df.percentile_direction == 'yes', 'percentile_direction'].count()/(df.loc[df.percentile_direction == 'no', 'percentile_direction'].count()+df.loc[df.percentile_direction == 'yes', 'percentile_direction'].count())
    pct_ratio = df.loc[df.winpct_direction == 'yes', 'winpct_direction'].count()/(df.loc[df.winpct_direction == 'no', 'winpct_direction'].count()+df.loc[df.winpct_direction == 'yes', 'winpct_direction'].count())
    
    ratiolist.append(tile_ratio)
    ratiolist.append(pct_ratio)
    
    tile_r2 = df['height_change'].corr(df['percentile_change'])
    pct_r2 = df['height_change'].corr(df['winpct_change'])
    
    r2list.append(tile_r2)
    r2list.append(pct_r2)

change_type = ['all height changes', 'all height changes', 'all height changes', 'all height changes',
        '1 in+ change', '1 in+ change', '1 in+ change', '1 in+ change']

division = ['D1', 'D1', 'D3', 'D3', 'D1', 'D1', 'D3', 'D3']

metric = ['rank percentile', 'win percentage', 'rank percentile', 'win percentage',
        'rank percentile', 'win percentage', 'rank percentile', 'win percentage']


pivotdf = pd.DataFrame(columns=['change','metric','division','proportion','r2'])

pivotdf.change = change_type
pivotdf.metric = metric
pivotdf.division = division
pivotdf.proportion = ratiolist
pivotdf.r2 = r2list

pivot = pd.pivot_table(pivotdf, values=['proportion', 'r2'], index=['change', 'metric', 'division']
                       , aggfunc=np.mean)

th_props = [
  ('font-size', '12px'),
  ('text-align', 'center'),
  ('font-weight', 'bold'),
  ('color', 'black'),
  ('background-color', 'light grey')
  ]

td_props = [
  ('font-size', '11px')
  ]

styles = [
  dict(selector="th", props=th_props),
  dict(selector="td", props=td_props)
  ]

pivot.style.format({'proportion': "{:.2%}", 'r2': "{:.2}"}).set_table_styles(styles)
