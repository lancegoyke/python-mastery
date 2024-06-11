def portfolio_cost(filename):
    # open file Data/portfolio.dat
    with open(filename) as f:
        # read data
        sum = 0
        warned = False
        for line in f:
            try:
                stock, shares, cost = line.split()
                shares_int = int(shares)
                cost_float = float(cost)
                sum += shares_int * cost_float
            except ValueError as e:
                print(f"Couldn't parse: {repr(line)}")
                print(f"Reason: {e}")

        # output
        return sum


if __name__ == "__main__":
    print(portfolio_cost("Data/portfolio3.dat"))
