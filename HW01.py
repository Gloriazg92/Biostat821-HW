def get_data(filepath):
    """Read the data in a text file, and return a list of lists of integers."""
    f = open(filepath, "r")
    data = []
    lines = f.readlines()
    for line in lines:
        line_data = line.strip().split(" ")
        result = map(int, line_data)
        data.append(list(result))
    f.close()
    return data


def analyze_data(list, opt):
    """Calculate sample statistics (average, standard deviation, covariance, correlation) for the given data."""
    flat_list = [item for sublist in list for item in sublist]
    if opt == "average":
        avg_num = sum(flat_list) / len(flat_list)
        return avg_num
    elif opt == "standard deviation":
        mean = sum(flat_list) / len(flat_list)
        variance = sum([((x - mean) ** 2) for x in flat_list]) / len(flat_list)
        sd_num = variance ** 0.5
        return sd_num
    elif opt == "covariance":
        x, y = list
        mean_x = sum(x) / len(x)
        mean_y = sum(y) / len(y)
        cov_num = sum((a - mean_x) * (b - mean_y) for (a, b) in zip(x, y)) / len(x)
        return cov_num
    elif opt == "correlation":
        x, y = list
        corr_num = pearson(x, y)
        return corr_num
    else:
        return None


def pearson(x, y):
    """Calculate the pearson correlation."""
    sum_x_sq = sum(xi * xi for xi in x)
    sum_y_sq = sum(yi * yi for yi in y)
    psum = sum(xi * yi for xi, yi in zip(x, y))
    num = psum - (sum(x) * sum(y) / len(x))
    den = pow(
        (sum_x_sq - pow(sum(x), 2) / len(x)) * (sum_y_sq - pow(sum(y), 2) / len(x)),
        0.5,
    )
    return num / den


dat = get_data("./example.txt")
print("average:", analyze_data(dat, "average"))
print("standard deviation:", analyze_data(dat, "standard deviation"))
print("covariance:", analyze_data(dat, "covariance"))
print("correlation:", analyze_data(dat, "correlation"))
