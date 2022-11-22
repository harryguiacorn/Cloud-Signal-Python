from src.mvc.DataKijunSignalMVC import Control, Model, View

def main(fetchDailyDate = True, fetchWeeklyData = False):
    if fetchDailyDate:
        _model = Model('data/nasdaq100/d/', 'asset_list/Nasdaq100.csv')
        _control = Control(_model, View())
        _control.main()    
    if fetchWeeklyData:
        _model = Model('data/nasdaq100/w/', 'asset_list/Nasdaq100.csv')
        _control = Control(_model, View())
        _control.main()

if __name__ == "__main__":
    main()