import indicators
import pandas as pd
import warnings


def main():
    warnings.filterwarnings("ignore")
    
    data = pd.read_csv("all_data.csv")
    data = indicators.ease_of_movement(data)
    data = indicators.acc_dist(data)
    data = indicators.on_balance_volume(data)
    data = indicators.price_volume_trend(data)
    data = indicators.average_true_range(data)
    data = indicators.bollinger_bands(data)
    data.to_csv("updatedwithti.csv")
    
    
if __name__ == "__main__":
    main()
