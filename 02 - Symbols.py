from datetime import date, datetime
from backtrader import Cerebro, TimeFrame
from BackTraderAlor.ALStore import ALStore  # Хранилище Alor
from my_config.Config import Config  # Файл конфигурации
import Strategy as ts  # Торговые системы

# Несколько тикеров для нескольких торговых систем по одному временнОму интервалу
if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    symbols = ('MOEX.SBER', 'MOEX.GAZP', 'MOEX.LKOH', 'MOEX.GMKN',)  # Кортеж тикеров
    store = ALStore(UserName=Config.UserName, RefreshToken=Config.RefreshToken, Boards=Config.Boards, Accounts=Config.Accounts)  # Хранилище Alor
    cerebro = Cerebro(stdstats=False)  # Инициируем "движок" BackTrader. Стандартная статистика сделок и кривой доходности не нужна

    cerebro.broker.setcash(3000000)  # Устанавливаем сколько денег
    cerebro.broker.setcommission(commission=0.01)  # Установить комиссию

    for symbol in symbols:  # Пробегаемся по всем тикерам
        # data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, compression=1, fromdate=date.today(), LiveBars=False)  # Исторические и новые бары тикера с начала сессии
        data = store.getdata(dataname=symbol, timeframe=TimeFrame.Minutes, compression=15, fromdate=datetime(2021, 10, 4), LiveBars=False)  # Исторические и новые бары тикера с начала сессии
        cerebro.adddata(data)  # Добавляем тикер
    # cerebro.addstrategy(ts.PrintStatusAndBars, name="One Ticker", symbols=('MOEX.SBER',))  # Добавляем торговую систему по одному тикеру
    # cerebro.addstrategy(ts.PrintStatusAndBars, name="Two Tickers", symbols=('MOEX.GAZP', 'MOEX.LKOH',))  # Добавляем торговую систему по двум тикерам
    cerebro.addstrategy(ts.PrintStatusAndBars, name="All Tickers")  # Добавляем торговую систему по всем тикерам

    results = cerebro.run()  # Запуск торговой системы
    print('Стоимость портфеля: %.2f' % cerebro.broker.getvalue())
    print('Свободные средства: %.2f' % cerebro.broker.get_cash())
