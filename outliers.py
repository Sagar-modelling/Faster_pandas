def find_outliers(data):
    """Find outliers in data, return indices of outliers"""
    out = data[(data - data.mean()).abs() > 2 * data.std()]
    return out

#data = pd.Series(np.random.randint(50,60,10000))
#data[7] = 30
#data[100] =1000
